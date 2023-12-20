import os
from modulos import funcoes as func


def limpatela():
    os.system("clear" if os.name == "posix" else "cls")


def cabecalho():
    print("*" * 16, "ToDo List", "*" * 16)
    print(f"Você possui {qtd_tarefas} para realizar!")


# Carregando dados
qtd_tarefas = func.qtd_tarefas()
op = -1
# Primeira tela

while op:
    limpatela()
    cabecalho()
    func.exibe_menu(func.menu)
    op = int(input())

    try:
        op = func.callback(op, func.menu)
    except:
        pass
