# 🧠 Fabric Toolkit

**Fabric Toolkit** is an interactive command-line interface (CLI) based on the [original Fabric project](https://github.com/danielmiessler/fabric), created by [Daniel Miessler](https://danielmiessler.com).  
This tool was built to simplify the lives of researchers, content creators, and AI enthusiasts by offering a fast and easy way to interact with Fabric’s resources—without the need to remember complex commands.

---

## 🚀 Features

| Option | Feature                             | Description |
|--------|-------------------------------------|-------------|
| 1      | Manual input + `extract_wisdom`     | Type any prompt manually and get an intelligent AI response with insights. |
| 2      | YouTube video transcription         | Provide a video URL and the tool will transcribe and extract insights using the `extract_wisdom` pattern. |
| 3      | Website scraping (URL)              | Enter a URL and receive an intelligent summary of the content. |
| 4      | List available patterns             | Displays all available Fabric patterns (skills). |
| 5      | Clear context                       | Resets the current Fabric session context. |
| 6      | Clear session                       | Starts a brand-new Fabric session from scratch. |

---

## 🌐 Language Selection

At startup, you can choose between:

- 🇧🇷 **Portuguese (pt-BR)**
- 🇺🇸 **English (EN)**

The interface adapts based on your selection.  
Note: All AI responses (insights, summaries, etc.) are returned in English regardless of interface language.

---

## 🔧 Project Structure

This project is a Python-based toolkit that wraps the original `fabric` Go binary. It provides two main interfaces:

1.  **Interactive CLI:** A simple, menu-driven command-line interface for easy interaction with Fabric.
2.  **Streamlit Web UI:** A web-based interface for more visual interactions (details to be added).

## 📦 Installation & Usage

### Prerequisites

- Go (to build the `fabric` binary)
- Python 3
- `yt-dlp` (for video transcription)

### Building the `fabric` binary

Before using the toolkit, you need to build the `fabric` Go binary:

```bash
go build .
```

### Running the Interactive CLI

1.  Clone the repository:
    ```bash
    git clone https://github.com/fabao2024/fabric-toolkit.git
    cd fabric-toolkit
    ```
2.  Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  Run the CLI application:
    ```bash
    python3 -m toolkit.main
    ```

## ⚙️ Configuration

You can configure the AI model used by the toolkit by editing the `toolkit/config.py` file.

```python
# toolkit/config.py
AI_MODEL = "gpt-4o" # Change to your desired model
```

🙌 Credits
This project is based on the brilliant work of Daniel Miessler and his Fabric project.

This customized version was created by Fabio Pettian with the goal of making Fabric more accessible to non-technical users, educators, content creators, and AI enthusiasts.

🔗 Related Links
🔧 GitHub Repo: github.com/fabao2024/fabric-toolkit

📰 Medium Article: Read the full story
