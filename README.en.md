# 🧠 Fabric Toolkit

Fabric Toolkit is a Command-Line Interface (CLI) utility designed to enhance productivity by integrating artificial intelligence with practical functions. Built upon the [Fabric](https://github.com/danielmiessler/fabric) project created by **Daniel Miessler**, it simplifies and expands the use of AI prompts for content creators, researchers, and AI enthusiasts.

This version was extended and adapted by [Fabio Pettian](https://github.com/fabao2024) to make usage easier, multilingual, and with an improved interactive experience.

---

## 🌟 Features

- 🧾 Manual input prompt and AI analysis
- 📹 YouTube video transcription and summarization
- 🌐 Web scraping and analysis via URL
- 🎨 Listing of available AI prompt patterns (skills)
- 🧹 Wipe current AI context or session
- 🌍 Language selection: Portuguese (pt-BR) or English (EN)
- 📋 Interactive terminal menu with explanation for each function
- 📦 File output disabled by default – displays results only in the terminal

---

## 📸 Menu Options Overview

1. **Manual Input + extract_wisdom**
   - Provide a custom prompt, and the tool uses Fabric’s `extract_wisdom` pattern to analyze the input.
2. **YouTube Video Transcription**
   - Input a YouTube URL and receive a summarized transcription using AI.
3. **Web Scraping (URL)**
   - Paste a website URL and get a summarized insight from its content.
4. **List Skills**
   - Displays all available prompt patterns (skills) that can be used with Fabric.
5. **Clear Context**
   - Clears the current AI conversation context.
6. **Clear Session**
   - Clears the session to start a fresh AI interaction.

---

## 🚀 Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/fabao2024/fabric-toolkit.git
cd fabric-toolkit
2. Set up the environment (Python)
bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Run the script
bash
Copiar
Editar
python3 fabric_toolkit.py
📂 Project Structure
Copiar
Editar
fabric/
├── fabric_toolkit.py
├── fabric_outputs/
├── README.md
├── README.en.md
├── requirements.txt
└── ...
🔗 Related Projects
🤖 Daniel Miessler’s Fabric Project: The foundation of this toolkit.

📘 Read the full article on Medium: Learn how and why the Fabric Toolkit was created.

📁 Access the official repository

👨‍💻 Author
Developed and maintained by Fabio Pettian
Feel free to contribute, fork, or send feedback!

🪪 License
This project is under the MIT License – open for use, modification, and distribution.
