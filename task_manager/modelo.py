from datetime import datetime
from rich.panel import Panel
from rich.traceback import install
install()

class Tarefa:
    def __init__(self, titulo:str, descricao:str, concluida:bool):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False
        self.data_criacao = self.data_atual()
        
    def data_atual(self):
        agora = datetime.now()
        return agora.strftime("%d/%m/%Y às %H:%M")
    
    def marcar_concluida(self):
        pass
    
    def reabrir(self):
        pass
    
    def exibir_tarefa(self):
        pass
    

class ListaTarefas:
    def __init__(self):
        pass