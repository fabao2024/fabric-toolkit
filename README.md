# 🧠 Fabric Toolkit

**Fabric Toolkit** é uma interface de linha de comando (CLI) interativa baseada no [projeto original Fabric](https://github.com/danielmiessler/fabric), idealizado por [Daniel Miessler](https://danielmiessler.com/). Esta ferramenta foi criada para facilitar a vida de pesquisadores, criadores de conteúdo e entusiastas de IA generativa, oferecendo uma maneira simples e rápida de interagir com os recursos do Fabric sem precisar lembrar comandos complexos.

---

## 🚀 Funcionalidades

| Opção | Funcionalidade | Descrição |
|-------|----------------|-----------|
| 1 | Input manual + `extract_wisdom` | Digite qualquer prompt manualmente e veja a resposta da IA com insights inteligentes. |
| 2 | Transcrição de vídeo do YouTube | Insira a URL de um vídeo e o Fabric irá transcrever e extrair insights com o padrão `extract_wisdom`. |
| 3 | Scrape de site (URL) | Forneça uma URL e obtenha um resumo inteligente do conteúdo do site. |
| 4 | Listar padrões disponíveis | Exibe todos os padrões (skills) disponíveis no Fabric. |
| 5 | Limpar contexto | Remove o contexto atual da sessão Fabric. |
| 6 | Limpar sessão | Inicia uma nova sessão do zero. |

---

## 🌐 Idioma

Ao iniciar, você poderá escolher entre:

- 🇧🇷 **Português (PT-BR)**
- 🇺🇸 **English (EN)**

> Todas as instruções e mensagens da ferramenta serão adaptadas ao idioma escolhido. As respostas da IA, no entanto, permanecem em **inglês** para manter a fidelidade ao padrão do Fabric.

---

## 📦 Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/fabao2024/fabric-toolkit.git
cd fabric-toolkit
2. (Opcional) Crie um ambiente virtual:
bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate
3. Instale as dependências:
bash
Copiar
Editar
pip install -r requirements.txt
4. Instale o Fabric CLI:
bash
Copiar
Editar
curl -fsSL https://raw.githubusercontent.com/danielmiessler/fabric/main/install.sh | sh
5. Execute o toolkit:
bash
Copiar
Editar
python3 fabric_toolkit.py
📁 Estrutura do Projeto
bash
Copiar
Editar
fabric/
├── fabric_toolkit.py         # Script principal do menu interativo
├── fabric_outputs/           # Resultados gerados pela IA (respostas e transcrições)
├── requirements.txt          # Dependências do projeto (FPDF, etc.)
└── README.md                 # Este arquivo
✍️ Exemplo de uso
Execute o script e escolha uma opção do menu.

Por exemplo: Opção 3 - Scrape de site

Digite a URL: https://www.example.com

Resultado: Resumo inteligente gerado pela IA diretamente no terminal (sem salvar arquivos, caso configurado).

🙌 Créditos
Este projeto é uma adaptação prática e educacional do repositório oficial de Daniel Miessler:

🔗 github.com/danielmiessler/fabric

📚 Saiba mais
📘 Artigo no Medium explicando todo o projeto:
👉 Leia o artigo no Medium (substituir pelo link real quando publicado)

📦 Repositório oficial:
👉 github.com/fabao2024/fabric-toolkit

🧪 Requisitos
Python 3.7+

Linux ou WSL2

fabric instalado e funcionando corretamente

Dependências listadas no requirements.txt

🧑‍💻 Autor
Fabio Pettian
LinkedIn | GitHub
