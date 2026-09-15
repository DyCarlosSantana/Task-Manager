from pathlib import Path
from task_manager import Tarefa, ListaTarefas

caminho = Path(__file__).parent / "dados" / "arquivo_tarefas.json"

lista = ListaTarefas()
lista.carregar_do_arquivo(caminho)

if len(lista) == 0:
    lista.adicionar_tarefa(Tarefa("Primeira tarefa", "Descrição"))
    lista.adicionar_tarefa(Tarefa("Segunda tarefa", "Descrição"))
else:
    print(f"Carregadas {len(lista)} tarefas do arquivo.")

# Exemplo de manipulação
lista.adicionar_tarefa(Tarefa("Nova tarefa", "Descrição"))
lista.adicionar_tarefa(Tarefa("Teste de persistencia ", "Adicionada nesta execução"))
lista.marcar_concluida("Primeira")

lista.salvar_em_arquivo(caminho)
print(lista.listar_todas())