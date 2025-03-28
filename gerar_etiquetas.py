import pandas as pd
from fpdf import FPDF
import unicodedata
import os
import sys

# Corrige o caminho para funcionar com .exe (PyInstaller --onefile)
if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(base_dir, "pedidos.xlsx")
output_path = os.path.join(base_dir, "etiquetas.pdf")

def limpar_texto(texto):
    if pd.isnull(texto):
        return ""
    texto = str(texto).replace("–", "-")
    texto = unicodedata.normalize('NFKD', texto).encode('latin-1', 'ignore').decode('latin-1')
    return texto

# Lê o Excel da aba "Etiqueta" da mesma pasta do script
df = pd.read_excel(input_path, sheet_name="Etiqueta")

class EtiquetaPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='L', unit='mm', format=(30, 90))
        self.set_auto_page_break(False)

    def add_etiqueta(self, pedido, nfe, cliente, obs, endereco):
        self.add_page()

        self.set_font("Arial", "B", 9)
        self.set_xy(2, 2)
        self.cell(45, 5, f"Nº PEDIDO: {pedido}", ln=0)
        self.cell(0, 5, f"Nº NFe: {nfe}", ln=1)

        self.set_xy(2, 7)
        self.set_font("Arial", "", 9)
        self.cell(0, 5, cliente, ln=1)

        self.set_xy(2, 12)
        self.set_font("Arial", "B", 8)
        self.cell(0, 5, obs.upper(), ln=1)

        self.set_xy(2, 18)
        self.set_font("Arial", "", 8)
        self.multi_cell(80, 4, endereco)

pdf = EtiquetaPDF()

for _, row in df.iterrows():
    pedido = limpar_texto(str(row['Observacao'])[:6])
    cliente = limpar_texto(row['Observacao'].split('-')[1].strip() if '-' in str(row['Observacao']) else '')
    endereco = f"{row['Logradouro']}, {row['Numero']} - {row['Complemento']} - {row['Bairro']} {row['Cidade']}/{row['Estado']} - CEP: {row['CEP']}"
    
    pdf.add_etiqueta(
        pedido=pedido,
        nfe=limpar_texto(row['NrDocumento']),
        cliente=cliente,
        obs=limpar_texto(f"OBS: {row['DsObservacao']}" if pd.notnull(row['DsObservacao']) else "OBS:"),
        endereco=limpar_texto(endereco),
    )

pdf.output(output_path)
print("PDF gerado com sucesso na mesma pasta!")