import os
from modulos import funcoes as function


def limpatela():
    os.system("clear" if os.name == "posix" else "cls")


def cabecalho(nome: str, qtd_tarefas: str):
    print("*" * 16, f"{nome}", "*" * 16)
    print(f"Você possui {qtd_tarefas} para realizar!")


# Carregando dados
lista_tarefas = function.cria_lista(
    "Minha Lista", "Fernando"
)  # Solicita a criação de uma nova lista
op = -1
# Primeira tela

while op:
    limpatela()  # Limpar o terminal antes de qualquer coisa
    cabecalho(
        lista_tarefas.titulo, f"{lista_tarefas}"
    )  # Inicia inserindo o cabeçalho, definido assim permite mudanças caso exista um nome da lista futuramente
    function.exibe_menu(
        function.menu
    )  # Desta forma a manutenção e a adição de novas funcionalidades limita-se ao bloco de funcoes

    try:
        op = int(input())
        if op < 0 or op >= len(function.menu):
            raise Exception("Opção invalida!")
    except Exception as e:
        print(f"{e}")
    except ValueError as e:
        print("Apenas numeros inteiros.")
    else:
        function.callback(op, function.menu, lista_tarefas)
    finally:
        input("Pressione Enter.")
