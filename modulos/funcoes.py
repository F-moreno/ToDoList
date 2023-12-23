import logging, os
from functools import wraps
from modulos.classes import Lista
from modulos.classes import Tarefa

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="app.log", level=logging.DEBUG, format=LOG_FORMAT)
log = logging.getLogger()


def limpaTela():
    os.system("clear" if os.name == "posix" else "cls")


# Decorator para gerenciar o log
def logger(_function):
    @wraps(_function)
    def wrapper(*args, **kwargs):
        msg = f"{str(_function.__name__).replace('_', ' ').capitalize():<20}"
        if _function(*args, **kwargs):
            msg += f'{" Success":<10}'
        else:
            msg += f'{" Failed":<10}'
        log.info(msg)

    return wrapper


def cria_lista(nome: str, autor: str) -> Lista:
    return Lista(nome, autor)


def carrega_lista():
    pass


def qtd_tarefas(lista: Lista) -> int:
    """Retorna a quantidade de tarefas existentes"""
    return f"{lista}"


@logger
def exibe_menu(_funcoes) -> int:
    """Exibe menu de acordo com a lista de funções passada."""
    try:
        for i in range(1, len(_funcoes)):  # percorre a lista de funcoes
            print(
                f"[{i}] - {str(_funcoes[i].__name__).replace('_',' ').capitalize()}"
            )  # exibe todas as funççoes com exceção do indice 0
        print(
            f"[0] - {str(_funcoes[0].__name__).replace('_',' ').capitalize()}"
        )  # Exibe a função de indice 0
        return 1
    except:
        return 0


def callback(op, funcoes, *arg, **kwargs):
    funcoes[op](*arg, **kwargs)


@logger
def sair(lista) -> int:
    return 1


@logger
def exibir_tarefas(lista) -> None:
    try:
        for tarefa in lista:
            print(f"{lista.index} - {tarefa}")
        return 1
    except:
        return 0


@logger
def adicionar_tarefas(lista: Lista) -> int:
    try:
        titulo = "tarefa 1"
        descricao = "descricao da tarefa 1"
        data = "25/05/2018"
        # titulo = input()
        # descricao = input()
        # data = input()
        tarefa = Tarefa(titulo, data, descricao)
        lista.tarefas.append(tarefa)
        return 1
    except:
        return 0


@logger
def remover_tarefa(lista: Lista) -> int:
    limpaTela()
    exibir_tarefas(lista)

    try:
        index = int(input("Qual tarefa deseja excluir?(ID): ")) - 1
        del lista.tarefas[index]
        return 1
    except:
        return 0


@logger
def iniciar_tarefa(lista: Lista) -> int:
    limpaTela()
    nao_existe = 1  # controlado para o caso de nao existir tarefas não inicializadas
    try:
        for tarefa in lista:
            if tarefa.indexEstado == 0:
                print(f"{lista.index} - {tarefa}")
                nao_existe = 0
        if nao_existe:
            raise Exception

        index = int(input("Qual tarefa deseja iniciar?(ID): ")) - 1

        if lista.tarefas[index].indexEstado == 0:
            lista.tarefas[index].mudar_estado()
        else:
            raise Exception
        return 1
    except:
        return 0


@logger
def finalizar_tarefa(lista: Lista) -> int:
    limpaTela()
    nao_existe = 1  # controlado para o caso de nao existir tarefas não inicializadas
    try:
        for tarefa in lista:
            if tarefa.indexEstado == 1:
                print(f"{lista.index} - {tarefa}")
                nao_existe = 0
        if nao_existe:
            raise Exception

        index = int(input("Qual tarefa deseja iniciar?(ID): ")) - 1
        if lista.tarefas[index].indexEstado == 1:
            lista.tarefas[index].mudar_estado()
        else:
            raise Exception
        return 1
    except:
        return 0


# iniciar tarefa, finalizar tarefa
menu = [
    sair,
    exibir_tarefas,
    adicionar_tarefas,
    remover_tarefa,
    iniciar_tarefa,
    finalizar_tarefa,
]

submenu = [sair, remover_tarefa]
