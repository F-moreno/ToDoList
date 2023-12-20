import logging
from modulos.classes import Lista
from modulos.classes import Tarefa

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="app.log", level=logging.DEBUG, format=LOG_FORMAT)
log = logging.getLogger()


# Decorator para gerenciar o log
def logger(_function):
    def wrapper(*args, **kwargs):
        log.info(str(_function).split()[1].replace("_", " ").capitalize())
        return _function(*args, **kwargs)

    return wrapper


def qtd_tarefas():
    """Retorna a quantidade de tarefas existentes"""
    return 0


@logger
def exibe_menu(_funcoes):
    """Exibe menu de acordo com a lista de funções passada."""
    for i in range(1, len(_funcoes)):  # percorre a lista de funcoes
        print(
            f"[{i}] - {str(_funcoes[i]).split()[1].replace('_',' ').capitalize()}"
        )  # exibe todas as funççoes com exceção do indice 0
    print(
        f"[0] - {str(_funcoes[0]).split()[1].replace('_',' ').capitalize()}"
    )  # Exibe a função de indice 0


@logger
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
