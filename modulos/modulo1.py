def qtd_tarefas():
    return 0

def exibe_menu(_funcoes):
    for i in range(1,len(_funcoes)):
        print(f"[{i}] - {str(_funcoes[i]).split()[1].replace('_',' ').capitalize()}")
    print(f"[0] - {str(_funcoes[0]).split()[1].replace('_',' ').capitalize()}")

def callback(op):
    global funcoes
    return funcoes[op]()

def sair():
    return 0

def exibir_tarefas():
    return 1

def adicionar_tarefas():
    return 1

def remover():
    pass



menu=[sair,
         exibir_tarefas,
         adicionar_tarefas]

submenu=[sair,
         remover]