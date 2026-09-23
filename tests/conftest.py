import pytest
from task_manager import Tarefa, ListaTarefas

@pytest.fixture
def lista_tres_tarefas():
    lista = ListaTarefas()
    lista.adicionar_tarefa(Tarefa("A", "Descrição A"))
    lista.adicionar_tarefa(Tarefa("B", "Descrição B"))
    lista.adicionar_tarefa(Tarefa("C", "Descrição C"))
    return lista

@pytest.fixture
def lista():
    lista = ListaTarefas()
    return lista