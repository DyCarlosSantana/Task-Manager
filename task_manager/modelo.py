from datetime import datetime

class Tarefa:
    def __init__(self, titulo:str, descricao:str, concluida:bool=False):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida
        self.data_criacao = self.data_atual()
        
    def data_atual(self):
        agora = datetime.now()
        return agora.strftime("%d/%m/%Y às %H:%M")
    
    def marcar_concluida(self):
        self.concluida = True
    
    def reabrir(self):
        self.concluida = False
    
    def exibir_tarefa(self):
        estado = "[ ]" if self.concluida == False else estado = "[X]"
        return f"{estado} {self.titulo} - {self.descricao} (criado em {self.data_criacao})"
    

class ListaTarefas:
    def __init__(self, tarefas=None):
        if tarefas is None:
            self.tarefas = []
        
    def adicionar_tarefa(self, nova_tarefa):
        self.tarefas.append(nova_tarefa)
    
    def remover_tarefa(self, titulo:str):
        for i in self.tarefas: 
            tarefa_atual = i
            if titulo in tarefa_atual:
                tarefa_removida = self.tarefas.pop(tarefa_atual, "Não encontrado")
        return tarefa_removida
    
    def listar_todas(self):
        for _ in self.tarefas:
            listagem += self.exibir_tarefa()
        return listagem
            
    def buscar(self, titulo): #base
        for i in self.tarefas:
            tarefa_atual = i
            if titulo in tarefa_atual:
                self.exibir_tarefa(tarefa_atual)
            else:
                return "Não encontrado"
    
    def marcar_concluida(self, titulo):
        for i in self.tarefas:
            tarefa_atual = i
            if titulo in tarefa_atual:
                self.marcar_concluida(tarefa_atual)