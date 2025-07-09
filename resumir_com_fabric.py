import subprocess
import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

def extrair_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else url  # permite passar só o ID também

def baixar_transcricao(video_id):
    print(f"🔍 Buscando transcrição do vídeo: {video_id}...")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["pt", "en"])
    except TranscriptsDisabled:
        print("❌ Esse vídeo não tem transcrição disponível.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro ao obter transcrição: {e}")
        sys.exit(1)
    return transcript

def salvar_transcricao(transcript, path="transcript.txt"):
    with open(path, "w", encoding="utf-8") as f:
        for entry in transcript:
            f.write(entry["text"] + "\n")
    print(f"✅ Transcrição salva em {path}")
    return path

def enviar_para_fabric(path):
    print("🤖 Enviando para o fabric...")
    try:
        subprocess.run(["./fabric", "--model", "gpt-4o", "-sp", "extract_wisdom"], input=open(path, "rb").read())
    except FileNotFoundError:
        print("❌ Erro: comando 'fabric' não encontrado. Compile com:\n  go build -o fabric && sudo mv fabric /usr/local/bin/")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 resumir_com_fabric.py <url_do_video_ou_video_id>")
        sys.exit(1)

    url = sys.argv[1]
    video_id = extrair_video_id(url)
    transcript = baixar_transcricao(video_id)
    path = salvar_transcricao(transcript)
    enviar_para_fabric(path)
