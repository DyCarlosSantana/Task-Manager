from datetime import datetime

class Tarefa:
    def __init__(self, titulo:str, descricao:str, concluida:bool=False):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida
        self.data_criacao = Tarefa.data_atual()
        
    @staticmethod
    def data_atual():
        agora = datetime.now()
        return agora.strftime("%d/%m/%Y às %H:%M")
    
    def marcar_concluida(self):
        self.concluida = True
    
    def reabrir(self):
        self.concluida = False
    
    def exibir_tarefa(self):
        estado = "[X]" if self.concluida else "[ ]"
        return f"{estado} {self.titulo} - {self.descricao} (criado em {self.data_criacao})"
    

class ListaTarefas:
    def __init__(self):
        self.tarefas = []
        
    def adicionar_tarefa(self, nova_tarefa):
        self.tarefas.append(nova_tarefa)
    
    def __iter__(self):
        return iter(self.tarefas)
    
    def remover_tarefa(self, titulo:str):
        for index, i in enumerate(self.tarefas): 
            tarefa_atual = i
            if titulo == tarefa_atual.titulo:
                return self.tarefas.pop(index)
        return None
    
    def __len__(self):
        return len(self.tarefas)
        
    def listar_todas(self):
        listagem = []
        for tarefa in self.tarefas:
            listagem.append(tarefa.exibir_tarefa())
        return listagem
            
    def buscar(self, titulo): #base
        for tarefa in self.tarefas:
            tarefa_atual = tarefa
            if titulo in tarefa_atual.titulo:
                return tarefa_atual.exibir_tarefa()
        return None
    
    def marcar_concluida(self, titulo):
        for tarefa in self.tarefas:
            tarefa_atual = tarefa
            if titulo in tarefa_atual.titulo:
                return tarefa_atual.marcar_concluida()
        return None