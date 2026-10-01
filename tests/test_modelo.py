import pytest
from task_manager import Tarefa

# Teste para sem titulo
def test_sem_titulo():
    with pytest.raises(ValueError):
        Tarefa("", "Descrição <sem titulo>")
        
def test_setter_sem_titulo():
    with pytest.raises(ValueError):
        tarefa = Tarefa("", "Descrição <sem titulo>")
        tarefa.titulo = ""

# Testando __str__
def test_str():
    tarefa = Tarefa("Titulo", "Descrição")
    resultado = str(tarefa)
    assert "Titulo" in resultado
    assert "Descrição" in resultado
    
def test_repr():
    tarefa = Tarefa("Titulo", "Descrição")
    resultado = repr(tarefa)
    assert "Titulo" in resultado
    assert "Descrição" in resultado
    assert "False" in resultado

def test_setter_sem_titulo():
    with pytest.raises(ValueError):
        tarefa = Tarefa("Titulo <sem descrição>", "")
        tarefa.descricao = ""
        
# Teste para verificar se a função marca como concluido
def test_marcar_concluida(lista_tres_tarefas):
    lista_tres_tarefas.marcar_concluida("A")
    lista_tres_tarefas.marcar_concluida("B")
    lista_tres_tarefas.marcar_concluida("C")
    assert all(t.concluida is True for t in lista_tres_tarefas)
    
# Teste para verificar se a função reabre as tarefas como NÂO concluidas
def test_reabrir(lista_tres_tarefas):
    for t in lista_tres_tarefas: # Conclui as tarefas para que recebam True
        t.marcar_concluida()
    for t in lista_tres_tarefas: # Reabre elas usando a função "reabrir" da Classe Tarefa
        t.reabrir()
    assert all( not t.concluida for t in lista_tres_tarefas)

# Verificar Concluida recebendo True
def test_verificacao_concluida():
    tarefa = Tarefa("Titulo", "Descrição", True)
    assert tarefa.concluida is True

# Teste para alteração de titulo (setter)
def test_setter_titulo():
    tarefa = Tarefa("Titulo", "Descrição")
    tarefa.titulo = "Novo titulo"
    assert tarefa.titulo == "Novo titulo"
    
# Teste para alteração de descrição (setter)
def test_setter_descricao():
    tarefa = Tarefa("Titulo", "Descrição")
    tarefa.descricao = "Nova descrição"
    assert tarefa.descricao == "Nova descrição"