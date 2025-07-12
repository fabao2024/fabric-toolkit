import os
import subprocess
from datetime import datetime

# Funções utilitárias
def executar_comando(cmd):
    resultado = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return resultado.stdout.strip(), resultado.stderr.strip(), resultado.returncode

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

# Idiomas disponíveis
IDIOMAS = {
    "pt": {
        "lang_code": "pt",
        "idioma_nome": "Português",
        "menu": "🧠 FABRIC TOOLKIT - MENU\n-------------------------\n"
                "1. Input manual + extract_wisdom\n"
                "2. Transcrição de vídeo do YouTube\n"
                "3. Scrape de site (URL)\n"
                "4. Listar padrões (skills)\n"
                "5. Limpar contexto\n"
                "6. Limpar sessão\n"
                "0. Sair",
        "explicacoes": {
            "1": "✏️ Opção 1: Input manual\nVocê digita uma pergunta ou comando e a IA responde com base no padrão 'extract_wisdom'.",
            "2": "🎥 Opção 2: Transcrição de vídeo\nVocê fornece uma URL de vídeo do YouTube e a IA irá transcrevê-lo e resumi-lo.",
            "3": "🌐 Opção 3: Scrape de site (URL)\nVocê fornece uma URL e o conteúdo textual será extraído e analisado pela IA.",
            "4": "🎨 Opção 4: Listar padrões\nA IA mostrará todos os padrões (skills) disponíveis atualmente.",
            "5": "🧹 Opção 5: Limpar contexto\nRemove o histórico de conversas da sessão atual.",
            "6": "🔄 Opção 6: Limpar sessão\nReinicia completamente a sessão da IA."
        },
        "perguntas": {
            "prompt": "\nDigite seu prompt para o Fabric:\n> ",
            "url_video": "\n🎥 Cole a URL do vídeo do YouTube:\n> ",
            "url_site": "\nDigite a URL do site:\n> "
        },
        "mensagens": {
            "resposta_ia": "\n🧠 RESPOSTA DA IA:\n",
            "erro_execucao": "Erro ao executar o comando Fabric:\n",
            "erro_yt": "\n❌ yt-dlp falhou:",
            "limpou_contexto": "\nContexto limpo.",
            "limpou_sessao": "\nSessão limpa.",
            "opcao_invalida": "Opção inválida.",
            "pressione_enter": "\nPressione Enter para continuar..."
        }
    },
    "en": {
        "lang_code": "en",
        "idioma_nome": "English",
        "menu": "🧠 FABRIC TOOLKIT - MENU\n-------------------------\n"
                "1. Manual input + extract_wisdom\n"
                "2. YouTube video transcription\n"
                "3. Website scraping (URL)\n"
                "4. List patterns (skills)\n"
                "5. Clear context\n"
                "6. Reset session\n"
                "0. Exit",
        "explicacoes": {
            "1": "✏️ Option 1: Manual input\nYou type a question or command, and the AI will respond based on the 'extract_wisdom' pattern.",
            "2": "🎥 Option 2: Video transcription\nYou provide a YouTube video URL, and the AI will transcribe and summarize it.",
            "3": "🌐 Option 3: Website scraping\nYou provide a URL, and the textual content will be extracted and analyzed by the AI.",
            "4": "🎨 Option 4: List patterns\nThe AI will show all available skills (patterns).",
            "5": "🧹 Option 5: Clear context\nThis removes the conversation history for the current session.",
            "6": "🔄 Option 6: Reset session\nFully restarts the AI session."
        },
        "perguntas": {
            "prompt": "\nEnter your prompt for Fabric:\n> ",
            "url_video": "\n🎥 Paste the YouTube video URL:\n> ",
            "url_site": "\nEnter the website URL:\n> "
        },
        "mensagens": {
            "resposta_ia": "\n🧠 AI RESPONSE:\n",
            "erro_execucao": "Error running Fabric command:\n",
            "erro_yt": "\n❌ yt-dlp failed:",
            "limpou_contexto": "\nContext cleared.",
            "limpou_sessao": "\nSession reset.",
            "opcao_invalida": "Invalid option.",
            "pressione_enter": "\nPress Enter to continue..."
        }
    }
}

# Selecionar idioma
def selecionar_idioma():
    limpar_tela()
    print("🌐 Selecione o idioma / Select your language:")
    print("1. Português (pt-BR)")
    print("2. English (EN)")
    escolha = input("Escolha (1 ou 2): ").strip()
    if escolha == "1":
        return "pt"
    elif escolha == "2":
        return "en"
    else:
        print("Opção inválida. Usando Português.")
        return "pt"

# Funções principais
def entrada_manual(config):
    print(config["explicacoes"]["1"])
    texto = input(config["perguntas"]["prompt"])
    cmd = f"fabric --model gpt-4o -sp extract_wisdom -v='#lang:{config['lang_code']} #input:{texto}'"
    saida, erro, codigo = executar_comando(cmd)
    if codigo == 0:
        print(config["mensagens"]["resposta_ia"])
        print(saida)
    else:
        print(config["mensagens"]["erro_execucao"], erro)

def transcrever_video_youtube(config):
    print(config["explicacoes"]["2"])
    url = input(config["perguntas"]["url_video"])
    cmd = f"fabric --youtube={url} --model gpt-4o -sp extract_wisdom -v='#lang:{config['lang_code']}'"
    saida, erro, codigo = executar_comando(cmd)
    if codigo == 0:
        print(config["mensagens"]["resposta_ia"])
        print(saida)
    else:
        print(config["mensagens"]["erro_yt"], erro)

def scrape_site(config):
    print(config["explicacoes"]["3"])
    url = input(config["perguntas"]["url_site"])
    cmd = f"fabric --model gpt-4o -u {url} -sp extract_wisdom -v='#lang:{config['lang_code']}'"
    saida, erro, codigo = executar_comando(cmd)
    if codigo == 0:
        print(config["mensagens"]["resposta_ia"])
        print(saida)
    else:
        print(config["mensagens"]["erro_execucao"], erro)

def listar_padroes(config):
    print(config["explicacoes"]["4"])
    cmd = "fabric --listpatterns"
    saida, erro, codigo = executar_comando(cmd)
    print("\n🎨")
    print(saida if codigo == 0 else erro)

def limpar_contexto(config):
    print(config["explicacoes"]["5"])
    executar_comando("fabric --wipecontext")
    print(config["mensagens"]["limpou_contexto"])

def limpar_sessao(config):
    print(config["explicacoes"]["6"])
    executar_comando("fabric --wipesession")
    print(config["mensagens"]["limpou_sessao"])

# Menu principal
def main():
    lang = selecionar_idioma()
    config = IDIOMAS[lang]
    print(f"\n✅ Idioma definido como: {config['idioma_nome'].upper()}\n")
    
    while True:
        print(config["menu"])
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1": entrada_manual(config)
        elif opcao == "2": transcrever_video_youtube(config)
        elif opcao == "3": scrape_site(config)
        elif opcao == "4": listar_padroes(config)
        elif opcao == "5": limpar_contexto(config)
        elif opcao == "6": limpar_sessao(config)
        elif opcao == "0": break
        else: print(config["mensagens"]["opcao_invalida"])

        input(config["mensagens"]["pressione_enter"])
        limpar_tela()

if __name__ == "__main__":
    main()
