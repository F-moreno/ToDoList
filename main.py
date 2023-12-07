import os
from modulos import modulo1
os.system("clear" if os.name == "posix" else "cls")

#Carregando dados
qtd_tarefas = modulo1.qtd_tarefas()
op =-1
#Primeira tela

while op:
    print("*"*16,"ToDo List","*"*16)
    print(f"Você possui {qtd_tarefas} para realizar!")
    modulo1.exibe_menu(modulo1.menu)
    op = int(input())

    try:
        op = modulo1.callback(op)
    except:
        pass
    