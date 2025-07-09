import os
import subprocess
from datetime import datetime
from fpdf import FPDF

# Criar diretório de saída se não existir
os.makedirs("fabric_outputs", exist_ok=True)

def executar_comando(cmd):
    resultado = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return resultado.stdout.strip(), resultado.stderr.strip(), resultado.returncode

def salvar_saida(nome_base, conteudo):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_txt = f"fabric_outputs/{nome_base}_{timestamp}.txt"
    nome_md = f"fabric_outputs/{nome_base}_{timestamp}.md"
    nome_pdf = f"fabric_outputs/{nome_base}_{timestamp}.pdf"

    with open(nome_txt, "w") as f:
        f.write(conteudo)
    with open(nome_md, "w") as f:
        f.write(conteudo)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for linha in conteudo.split("\n"):
        pdf.multi_cell(0, 10, linha)
    pdf.output(nome_pdf)

    return nome_txt, nome_md, nome_pdf

def transcrever_video_youtube():
    url = input("\n\U0001F4FA Cole a URL do vídeo do YouTube:\n> ").strip()
    print("\n\U0001F9E0 RESPOSTA DA IA:\n")
    transcript_cmd = f"fabric --youtube={url} --model gpt-4o -sp extract_wisdom -o transcript.txt"
    saida, erro, codigo = executar_comando(transcript_cmd)

    if codigo == 0:
        with open("transcript.txt") as f:
            conteudo = f.read()
        print(conteudo)
        txt, md, pdf = salvar_saida("resumo", conteudo)
        print(f"\n\U0001F4BE Resultado salvo em:\n- {md}\n- {txt}\n- {pdf}\n")
    else:
        print(f"\n❌ yt-dlp failed: exit status {codigo}, stderr:\n\n{erro}\n")

def entrada_manual():
    texto = input("\nDigite seu prompt para o Fabric:\n> ")
    cmd = f"fabric --model gpt-4o -sp extract_wisdom -v=#input:'{texto}'"
    saida, erro, codigo = executar_comando(cmd)
    if codigo == 0:
        print("\n\U0001F9E0 RESPOSTA DA IA:\n")
        print(saida)
        txt, md, pdf = salvar_saida("resposta_manual", saida)
        print(f"\n\U0001F4BE Resultado salvo em:\n- {md}\n- {txt}\n- {pdf}\n")
    else:
        print(f"Erro ao executar o comando Fabric:\n{erro}")

def scrape_site():
    url = input("\nDigite a URL do site para extrair conteúdo:\n> ")
    cmd = f"fabric --model gpt-4o -u {url} -sp extract_wisdom"
    saida, erro, codigo = executar_comando(cmd)
    if codigo == 0:
        print("\n\U0001F9E0 RESPOSTA DA IA:\n")
        print(saida)
        txt, md, pdf = salvar_saida("resumo_site", saida)
        print(f"\n\U0001F4BE Resultado salvo em:\n- {md}\n- {txt}\n- {pdf}\n")
    else:
        print(f"Erro ao executar Fabric no site:\n{erro}")

def listar_padroes():
    cmd = "fabric --listpatterns"
    saida, erro, codigo = executar_comando(cmd)
    if codigo == 0:
        print("\n\U0001F3A8 PADRÕES DISPONÍVEIS:\n")
        print(saida)
    else:
        print(f"Erro ao listar padrões:\n{erro}")

def limpar_contexto():
    executar_comando("fabric --wipecontext")
    print("\nContexto limpo.")

def limpar_sessao():
    executar_comando("fabric --wipesession")
    print("\nSessão limpa.")

def main():
    while True:
        print("""
\U0001F9E0 FABRIC TOOLKIT - MENU
-------------------------
1. Input manual + extract_wisdom
2. Transcrição de vídeo do YouTube
3. Scrape de site (URL)
4. Listar padrões (skills)
5. Limpar contexto
6. Limpar sessão
0. Sair
""")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1": entrada_manual()
        elif opcao == "2": transcrever_video_youtube()
        elif opcao == "3": scrape_site()
        elif opcao == "4": listar_padroes()
        elif opcao == "5": limpar_contexto()
        elif opcao == "6": limpar_sessao()
        elif opcao == "0": break
        else: print("Opção inválida.")

if __name__ == "__main__":
    main()
