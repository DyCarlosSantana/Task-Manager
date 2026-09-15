from .modelo import Tarefa, ListaTarefas
from .persistencia import salvar_tarefas, carregar_tarefas

__all__ = ["Tarefa", "ListaTarefas", "salvar_tarefas", "carregar_tarefas"]