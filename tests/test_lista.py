import pytest
from task_manager import ListaTarefas, Tarefa

def test_lista_vazia(lista):
    assert len(lista) == 0
    
def test_adicionar_tarefa(lista):
    t = Tarefa("Titulo", "Descrição")
    lista.adicionar_tarefa(t)
    assert len(lista) == 1
    
def test_adicionar_duas_tarefa(lista):
    t1 = Tarefa("Titulo 01", "Descrição 01")
    t2 = Tarefa("Titulo 02", "Descrição 02")
    lista.adicionar_tarefa(t1)
    lista.adicionar_tarefa(t2)
    assert len(lista) == 2
    
def test_remover_tarefa(lista):
    t = Tarefa("Titulo", "Descrição")
    lista.adicionar_tarefa(t)
    removido = lista.remover_tarefa("Titulo")
    assert removido is t
    assert len(lista) == 0
    
def test_remover_tarefa_em_lista(lista_tres_tarefas):
    lista_tres_tarefas.remover_tarefa("A")
    lista_atual = [t.titulo for t in lista_tres_tarefas]
    assert lista_atual == ["B", "C"]
    
def test_remover_tarefa_inexistente(lista_tres_tarefas):
    removido = lista_tres_tarefas.remover_tarefa("D")
    assert removido is None
    
def test_buscar(lista_tres_tarefas):
    resultado = lista_tres_tarefas.buscar("B")
    assert "B" in resultado
    
def test_buscar_none(lista_tres_tarefas):
    resultado = lista_tres_tarefas.buscar("D")
    assert resultado is None
    
def test_marcar_concluida(lista):
    t = Tarefa("Titulo", "Descrição")
    lista.adicionar_tarefa(t)
    lista.marcar_concluida("Titulo")
    assert t.concluida is True
    
def test_marcar_concluida_inexistente(lista_tres_tarefas):
    lista_tres_tarefas.marcar_concluida("D")
    assert all(not t.concluida for t in lista_tres_tarefas)
    
def test_iteracao_preserva_ordem(lista_tres_tarefas):
    resultado = [t.titulo for t in lista_tres_tarefas]
    assert resultado == ["A", "B", "C"]