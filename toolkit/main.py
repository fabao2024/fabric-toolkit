from . import utils
from . import commands

def selecionar_idioma():
    utils.limpar_tela()
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

def main():
    lang = selecionar_idioma()
    lang_config = utils.load_translation(lang)
    print(f"\n✅ Idioma definido como: {lang_config['idioma_nome'].upper()}\n")

    while True:
        print(lang_config["menu"])
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            commands.entrada_manual(lang_config)
        elif opcao == "2":
            commands.transcrever_video_youtube(lang_config)
        elif opcao == "3":
            commands.scrape_site(lang_config)
        elif opcao == "4":
            commands.listar_padroes(lang_config)
        elif opcao == "5":
            commands.limpar_contexto(lang_config)
        elif opcao == "6":
            commands.limpar_sessao(lang_config)
        elif opcao == "0":
            break
        else:
            print(lang_config["mensagens"]["opcao_invalida"])

        input(lang_config["mensagens"]["pressione_enter"])
        utils.limpar_tela()

if __name__ == "__main__":
    main()
