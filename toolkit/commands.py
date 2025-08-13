from . import utils
from . import config

def _run_fabric_command(command_list, lang_config):
    """A helper function to run a fabric command and print the output."""
    saida, erro, codigo = utils.executar_comando(command_list)
    if codigo == 0:
        print(lang_config["mensagens"]["resposta_ia"])
        print(saida)
    else:
        print(lang_config["mensagens"]["erro_execucao"], erro)

def entrada_manual(lang_config):
    print(lang_config["explicacoes"]["1"])
    texto = input(lang_config["perguntas"]["prompt"])
    cmd_list = ["fabric", "--model", config.AI_MODEL, "-sp", "extract_wisdom", "-v", f"#lang:{lang_config['lang_code']} #input:{texto}"]
    _run_fabric_command(cmd_list, lang_config)

def transcrever_video_youtube(lang_config):
    print(lang_config["explicacoes"]["2"])
    url = input(lang_config["perguntas"]["url_video"])
    cmd_list = ["fabric", f"--youtube={url}", "--model", config.AI_MODEL, "-sp", "extract_wisdom", "-v", f"#lang:{lang_config['lang_code']}"]
    _run_fabric_command(cmd_list, lang_config)

def scrape_site(lang_config):
    print(lang_config["explicacoes"]["3"])
    url = input(lang_config["perguntas"]["url_site"])
    cmd_list = ["fabric", "--model", config.AI_MODEL, "-u", url, "-sp", "extract_wisdom", "-v", f"#lang:{lang_config['lang_code']}"]
    _run_fabric_command(cmd_list, lang_config)

def listar_padroes(lang_config):
    print(lang_config["explicacoes"]["4"])
    cmd_list = ["fabric", "--listpatterns"]
    saida, erro, codigo = utils.executar_comando(cmd_list)
    print("\n🎨")
    print(saida if codigo == 0 else erro)

def limpar_contexto(lang_config):
    print(lang_config["explicacoes"]["5"])
    utils.executar_comando(["fabric", "--wipecontext"])
    print(lang_config["mensagens"]["limpou_contexto"])

def limpar_sessao(lang_config):
    print(lang_config["explicacoes"]["6"])
    utils.executar_comando(["fabric", "--wipesession"])
    print(lang_config["mensagens"]["limpou_sessao"])
