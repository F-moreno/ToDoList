class TarefaConcluidaError(Exception):
    """Erro para indicar que a tarefa foi concluida"""

    pass


class Tarefa:
    def __init__(self, titulo: str, data: str, descricao: str, estado: int = 0) -> None:
        self.titulo = titulo
        self.data = data
        self.descricao = descricao
        self.estado = estado

    def mudar_estado(self) -> None:
        try:
            if self.estado < 2:
                self.estado += 1
            else:
                raise TarefaConcluidaError("A tarefa ja esta concluida!")
        except TarefaConcluidaError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

    def __str__(self) -> str:
        return (
            f"Tarefa: {self.titulo} | Iniciada em: {self.data} | Estado: {self.estado}"
        )


class Lista:
    def __init__(
        self, titulo: str, autor: str, tarefas: list[Tarefa] = [Tarefa]
    ) -> None:
        self.titulo = titulo
        self.autor = autor
        self.tarefas = tarefas
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> Tarefa:
        if self.index < len(self.tarefas):
            _tarefa = self.tarefas[self.index]
            self.index += 1
            return _tarefa
        else:
            self.index = 0
            raise StopIteration
