import json
import pytest
from task_manager import Tarefa, ListaTarefas
from task_manager import salvar_tarefas, carregar_tarefas

def test_salvar_lista_vazia(tmp_path):
    caminho = tmp_path / "tarefas.json"
    salvar_tarefas([], caminho)
    resultado = carregar_tarefas(caminho)
    assert resultado == []

# deve testar se o erro FileNotFoundError é detectado
def test_salvar_tarefa_diretorio_inexistente(tmp_path):
    with pytest.raises(FileNotFoundError):
        caminho_inexistente = tmp_path / "subpasta_que_nao_existe" / "arquivo.json"
        salvar_tarefas([], caminho_inexistente)
    
def test_round_trip_uma_tarefa(tmp_path):
    caminho = tmp_path / "tarefa.json"
    tarefa = Tarefa("Titulo", "Descrição")
    lista = ListaTarefas()
    lista.adicionar_tarefa(tarefa)
    lista.salvar_em_arquivo(caminho)
    carregados = carregar_tarefas(caminho)
    assert carregados[0].titulo == "Titulo"
    assert carregados[0].descricao == "Descrição"
    assert carregados[0].concluida is False

def test_round_trip_lista_tarefas(tmp_path, lista_tres_tarefas):
    caminho = tmp_path / "tarefa.json"
    lista_tres_tarefas.salvar_em_arquivo(caminho)
    carregados = carregar_tarefas(caminho)
    assert len(carregados) == 3
    
def test_preservar_concluida(tmp_path):
    caminho = tmp_path / "tarefa.json"
    tarefa = Tarefa("Titulo", "Descrição", True)
    lista = ListaTarefas()
    lista.adicionar_tarefa(tarefa)
    lista.salvar_em_arquivo(caminho)
    carregados = carregar_tarefas(caminho)
    assert carregados[0].concluida is True
    
def test_caminho_inexistente(tmp_path):
    caminho_inexistente = tmp_path / "arquivo_inexistente.json"
    carregados = carregar_tarefas(caminho_inexistente)
    assert carregados == []
    
def test_json_corrompido(tmp_path):
    caminho = tmp_path / "corrompido.json"
    caminho.write_text("{arquivo corrompido", encoding="utf-8")
    carregados = carregar_tarefas(caminho)
    assert carregados == []