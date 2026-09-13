from task_manager.modelo import Tarefa, ListaTarefas
from pathlib import Path


path = Path(__file__).parent / "dados/arquivo_tarefas.json"
if not path.exists():
    path.parent.mkdir(exist_ok=True)
    path.touch()
else:
    print("Arquivo encontrado!")
    
# Instanciando os objetos (tarefa) com Tarefa
tarefa_01 = Tarefa("Resolver implementações", "Resolver implementações dos métodos de Tarefa e ListaTarefa", False)
tarefa_02 = Tarefa("Incrição Concurso", "Me inscruver para concurso da Transpetro", False)
tarefa_03 = Tarefa("Estudar Inglês", "Iniciar estudos de inglês pelo curso que foi comprado, e com o apoio da IA", False)
tarefa_04 = Tarefa("Posts Loja", "Fazer os posts pendentes no instagram da loja", False)
tarefa_05 = Tarefa("Treino Completo", "Concluir uma semana inteira de treinar (segunda à sexta)", True)
tarefa_extra = Tarefa("Tomar creatina", "Tomar suplemento diariamente", False)

# Instanciando a lista com ListaTarefa, adicinando tarefas, testando len() e o método listar_todas()
lista_de_tarefas = ListaTarefas()

# Carregando os dados se arquivos_tarefas.json
lista_de_tarefas.carregar_do_arquivo(path)
# Manipulando os dados (adicionando/removendo)
lista_de_tarefas.adicionar_tarefa(tarefa_01)
lista_de_tarefas.adicionar_tarefa(tarefa_02)
lista_de_tarefas.adicionar_tarefa(tarefa_03)
lista_de_tarefas.adicionar_tarefa(tarefa_04)
lista_de_tarefas.adicionar_tarefa(tarefa_05)
lista_de_tarefas.adicionar_tarefa(tarefa_extra)
# Salvando os dados
lista_de_tarefas.salvar_em_arquivo(path)

lista_atualizada = lista_de_tarefas.listar_todas()
print(lista_atualizada)