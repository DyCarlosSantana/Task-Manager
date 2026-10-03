import pytest
from task_manager import Tarefa

# Teste para sem titulo
def test_sem_titulo():
    with pytest.raises(ValueError):
        Tarefa("", "Descrição <sem titulo>")
        
def test_setter_titulo_vazio():
    with pytest.raises(ValueError):
        tarefa = Tarefa("Titulo Temporario", "Descrição <sem titulo>")
        tarefa.titulo = ""

def test_setter_descricao_vazia():
    with pytest.raises(ValueError):
        tarefa = Tarefa("Titulo <sem descrição>", "")
        tarefa.descricao = ""
        
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