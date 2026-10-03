import json
from .modelo import Tarefa
    
# Criação dos métodos e verificação
def salvar_tarefas(lista_de_objetos, caminho_arquivo):
    try:
        lista_de_dicionarios = []
        lista_de_dicionarios = [obj.to_dict() for obj in lista_de_objetos]
        
        with open(caminho_arquivo, "w", encoding="utf-8") as file:
            json.dump(lista_de_dicionarios, file)
    except FileNotFoundError:
        raise FileNotFoundError("Diretorio não encontrado")
    
    
def carregar_tarefas(caminho_arquivo):
    try:
        lista_de_dicionarios = []
        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            lista_de_dicionarios = json.load(file)
        
        lista_de_objetos = [Tarefa.from_dict(dicionario) for dicionario in lista_de_dicionarios]
            
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    else:
        return lista_de_objetos

