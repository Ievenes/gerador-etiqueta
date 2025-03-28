### 🏷️ Gerador de Etiquetas em PDF

Gera etiquetas padronizadas em PDF com base em dados do Excel. Simples, rápido e portátil — ideal para logística e expedição.

📁 Estrutura do Projeto

```graphql

📦 EtiquetasApp/
├── gerar_etiquetas.exe   # Executável gerado com PyInstaller
├── gerar_etiquetas.py    # Código-fonte principal
├── pedidos.xlsx           # Planilha com os dados de entrada
└── etiquetas.pdf          # PDF gerado com as etiquetas
```

### 📋 Requisitos

Se for executar via Python:

- Python 3.11+

- Bibliotecas:

- pandas

- fpdf

- unicodedata (padrão)

- openpyxl (para leitura de .xlsx)

Instalar as dependências:

```bash
pip install pandas fpdf openpyxl
```

### ⚙️ Como usar

✅ Modo 1: Rodando o .exe
Coloque o arquivo pedidos.xlsx na mesma pasta do gerar_etiquetas.exe.

Dê dois cliques no gerar_etiquetas.exe.

O arquivo etiquetas.pdf será gerado automaticamente na mesma pasta.

✅ Modo 2: Rodando o código .py

```bash
python gerar_etiquetas.py
```

### 📄 Formato esperado do Excel

- Nome da aba: Etiqueta

- Colunas obrigatórias:

  - Observacao

  - NrDocumento

  - DsObservacao

  - Logradouro

  - Numero

  - Complemento

  - Bairro

  - Cidade

  - Estado

  - CEP

### 🧠 O que o script faz?

- Lê os dados da aba Etiqueta do Excel.

- Extrai informações como número do pedido, nota fiscal, cliente, observações e endereço.

- Gera um PDF com etiquetas no formato 30x90mm, prontas para impressão.

🛠️ Compilando novamente (opcional)
Para gerar o .exe:

```bash
pyinstaller --onefile --noconsole gerar_etiquetas.py
```

O PDF será gerado mesmo que o .exe esteja em uma subpasta — desde que o pedidos.xlsx esteja junto.

### ✅ Resultado

Ao final, você terá um etiquetas.pdf como este:

```yaml
-----------------------------
| Nº PEDIDO: 123456   Nº NFe: 987654
| Cliente: Fulano de Tal
| OBS: URGENTE - ENTREGAR HOJE
| Rua das Flores, 123 - Casa 2
| Bairro Centro - São Paulo/SP
| CEP: 01234-567
-----------------------------
```

### 💬 Contato

Desenvolvido por Lucas Ievenes Ratti
🔗 Analista de Dados na EFF Dental | Automatizando o dia a dia com código 🚀

Linkedin: <https://www.linkedin.com/in/lucas-ievenes/>
