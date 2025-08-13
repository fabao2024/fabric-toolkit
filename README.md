🌍 Disponível em: [Português](README.md) | [English](README_en.md)

# 🧠 Fabric Toolkit

**Fabric Toolkit** é uma interface de linha de comando (CLI) interativa baseada no [projeto original Fabric](https://github.com/danielmiessler/fabric), idealizado por [Daniel Miessler](https://github.com/danielmiessler). Esta ferramenta foi criada para facilitar a vida de pesquisadores, criadores de conteúdo e entusiastas de IA generativa, oferecendo uma maneira simples e rápida de interagir com os recursos do Fabric sem precisar lembrar comandos complexos.

---

## 🚀 Funcionalidades

| Opção | Funcionalidade                           | Descrição |
|-------|-------------------------------------------|-----------|
| 1     | Input manual + `extract_wisdom`           | Digite qualquer prompt manualmente e veja a resposta da IA com insights inteligentes. |
| 2     | Transcrição de vídeo do YouTube           | Insira a URL de um vídeo e o Fabric irá transcrever e extrair insights com o padrão `extract_wisdom`. |
| 3     | Scrape de site (URL)                      | Forneça uma URL e obtenha um resumo inteligente do conteúdo do site. |
| 4     | Listar padrões disponíveis                | Exibe todos os padrões (skills) disponíveis no Fabric. |
| 5     | Limpar contexto                           | Remove o contexto atual da sessão Fabric. |
| 6     | Limpar sessão                             | Inicia uma nova sessão do zero. |

---

## 🌐 Idioma

Ao iniciar, você poderá escolher entre:

- 🇧🇷 Português (pt-BR)
- 🇺🇸 English (EN)

Os menus e mensagens seguirão o idioma escolhido, porém os resultados da IA serão sempre retornados em inglês (por padrão).

---

## 🔧 Estrutura do Projeto

Este projeto é um toolkit baseado em Python que envolve o binário original `fabric` em Go. Ele fornece duas interfaces principais:

1.  **CLI Interativa:** Uma interface de linha de comando simples e baseada em menus para facilitar a interação com o Fabric.
2.  **UI Web com Streamlit:** Uma interface baseada na web para interações mais visuais (detalhes a serem adicionados).

## 📦 Instalação e Uso

### Pré-requisitos

- Go (para compilar o binário `fabric`)
- Python 3
- `yt-dlp` (para transcrição de vídeo)

### Compilando o binário `fabric`

Antes de usar o toolkit, você precisa compilar o binário `fabric` em Go:

```bash
go build .
```

### Executando a CLI Interativa

1.  Clone o repositório:
    ```bash
    git clone https://github.com/fabao2024/fabric-toolkit.git
    cd fabric-toolkit
    ```
2.  Crie um ambiente virtual e instale as dependências:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  Execute a aplicação CLI:
    ```bash
    python3 -m toolkit.main
    ```

## ⚙️ Configuração

Você pode configurar o modelo de IA usado pelo toolkit editando o arquivo `toolkit/config.py`.

```python
# toolkit/config.py
AI_MODEL = "gpt-4o" # Altere para o modelo desejado
```

🧑‍💻 Autor da Ferramenta
Este projeto foi idealizado por Daniel Miessler e adaptado por fabao2024 para facilitar o uso por meio de um menu interativo CLI com suporte multilíngue.

📄 Licença
Este projeto está licenciado sob a Licença MIT.
