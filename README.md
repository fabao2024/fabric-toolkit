# Fabric Toolkit

Este projeto é uma ferramenta de linha de comando interativa (CLI) construída com Python e Go que utiliza o poder do [fabric](https://github.com/danielmiessler/fabric) para interagir com modelos de linguagem via API e gerar resumos inteligentes.

## ✨ Funcionalidades

- Entrada manual com padrão `extract_wisdom`
- Resumo automático de vídeos do YouTube
- Scraping inteligente de sites
- Exportação para `.md`, `.txt` e `.pdf`
- Menu interativo com múltiplas opções

## 🛠️ Instalação

```bash
sudo apt install golang python3-venv
git clone https://github.com/fabao2024/fabric-toolkit.git
cd fabric-toolkit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
go build -o fabric && sudo mv fabric /usr/local/bin/

🚀 Execução

python3 fabric_toolkit.py

📋 Menu de opções
1. Entrada manual com Fabric

2. Transcrição e análise de vídeo do YouTube

3. Scraping de site

4. Listar padrões disponíveis (skills)

5. Limpar contexto

6. Limpar sessão

7. Sair

📁 Estrutura


fabric-toolkit/
├── fabric_toolkit.py
├── fabric_outputs/
├── requirements.txt
├── LICENSE
└── README.md

📄 Exemplo de saída
Arquivos gerados:

fabric_outputs/resumo_YYYYMMDD_HHMMSS.md

fabric_outputs/resumo_YYYYMMDD_HHMMSS.txt

fabric_outputs/resumo_YYYYMMDD_HHMMSS.pdf

🤝 Contribuições
Sinta-se livre para abrir uma issue ou pull request.

📜 Licença
MIT License

---

### ✔️ Agora, salve e finalize o conflito:

1. Substitua o conteúdo do `README.md` com o texto acima (usando qualquer editor de texto).
2. Depois no terminal, execute:

```bash
git add README.md
git commit -m "Resolvido conflito de merge no README.md"
git push origin main

