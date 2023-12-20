from modulos.classes import Lista
from modulos.classes import Tarefa


def qtd_tarefas():
    """Retorna a quantidade de tarefas existentes"""
    return 0


def exibe_menu(_funcoes):
    """Exibe menu de acordo com a lista de funções passada."""
    for i in range(1, len(_funcoes)):  # percorre a lista de funcoes
        print(
            f"[{i}] - {str(_funcoes[i]).split()[1].replace('_',' ').capitalize()}"
        )  # exibe todas as funççoes com exceção do indice 0
    print(
        f"[0] - {str(_funcoes[0]).split()[1].replace('_',' ').capitalize()}"
    )  # Exibe a função de indice 0


def callback(op, funcoes):
    return funcoes[op]()


def sair():
    return 0


def exibir_tarefas():
    return 1


def adicionar_tarefas():
    return 1


def remover():
    pass


menu = [sair, exibir_tarefas, adicionar_tarefas]

submenu = [sair, remover]
