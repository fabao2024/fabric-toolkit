import os
import subprocess
import json

def load_translation(lang):
    """Loads the translation file for the given language."""
    try:
        with open(f"toolkit/locales/{lang}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Translation file for '{lang}' not found. Defaulting to English.")
        with open("toolkit/locales/en.json", "r", encoding="utf-8") as f:
            return json.load(f)

def executar_comando(cmd_list):
    """Executes a command and returns the output, error, and return code."""
    resultado = subprocess.run(cmd_list, capture_output=True, text=True)
    return resultado.stdout.strip(), resultado.stderr.strip(), resultado.returncode

def limpar_tela():
    """Clears the console screen."""
    os.system('clear' if os.name == 'posix' else 'cls')
