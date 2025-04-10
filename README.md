# 🚀 Meu App Python

Um aplicativo criado para integrar uma Steam Deck para abrir uma porta de maneira remota.
OBS: App criado para uso interno de um cliente que utilize um sistema de controle de acesso em nuvem.

## 🛠️ Requisitos

- Python 3.7 ou superior
- `pip` instalado

## 📦 Instalação

1. Clone o repositório:

`git clone https://github.com/vagnerdemelo/openRemoteDoorMK.git`
`cd openRemoteDoorMK`

2. Crie um ambiente virtual (opcional, mas recomendado):

`python -m venv venv`
`source venv/bin/activate`  # no Linux/macOS
`venv\Scripts\activate`      # no Windows

3. Instale as dependencias:

`pip install -r requirements.txt`

4. Execute com:

`python main.py`



🖼️ Gerando Executável (opcional):

`pip install pyinstaller`
`pyinstaller --noconsole --onefile main.py`
