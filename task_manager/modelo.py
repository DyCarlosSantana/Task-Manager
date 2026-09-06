from datetime import datetime

class Tarefa:
    def __init__(self, titulo:str, descricao:str, concluida:bool=False):
        self._titulo = titulo
        self._descricao = descricao
        self.concluida = concluida
        self.data_criacao = Tarefa.data_atual()
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, novo_titulo):
        if not novo_titulo.strip():
            raise ValueError("Titulo não pode ser vazio!") # Pesquisar mais sobre raise
        self._titulo = novo_titulo

    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, nova_descricao):
        if not nova_descricao.strip():
            raise ValueError("Adicione uma descrição a Tarefa!")
        self._descricao = nova_descricao
    
    @staticmethod
    def data_atual():
        agora = datetime.now()
        return agora.strftime("%d/%m/%Y às %H:%M")
    
    def marcar_concluida(self):
        self.concluida = True
    
    def reabrir(self):
        self.concluida = False
    
    def __str__(self):
        estado = "[X]" if self.concluida else "[ ]"
        return f"{estado} {self.titulo} - {self.descricao} (criado em {self.data_criacao})"
    
    def __repr__(self):
        return f"Tarefa(titulo={self.titulo}, descrição={self.descricao}, concluida={self.concluida})"
    
    
class ListaTarefas:
    def __init__(self):
        self.tarefas = []
        
    def adicionar_tarefa(self, nova_tarefa):
        self.tarefas.append(nova_tarefa)
    
    def __iter__(self):
        return iter(self.tarefas)
    
    def remover_tarefa(self, titulo:str):  # sourcery skip: use-next
        for index, tarefa in enumerate(self.tarefas): 
            if titulo == tarefa.titulo:
                return self.tarefas.pop(index)
        return None
    
    def __len__(self):
        return len(self.tarefas)
        
    def listar_todas(self):
        return [str(tarefa) for tarefa in self.tarefas]
            
    def buscar(self, titulo): #base  # sourcery skip: use-next
        for tarefa in self.tarefas:
            if titulo in tarefa.titulo:
                return str(tarefa)
        return None
    
    def marcar_concluida(self, titulo):  # sourcery skip: use-next
        for tarefa in self.tarefas:
            if titulo in tarefa.titulo:
                return tarefa.marcar_concluida()
        return None