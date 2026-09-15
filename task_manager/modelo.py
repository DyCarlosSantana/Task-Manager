from datetime import datetime

class Tarefa:
    def __init__(self, titulo:str, descricao:str, concluida:bool=False, data_criacao=None):
        self._titulo = titulo
        self._descricao = descricao
        self._concluida = concluida
        self.data_criacao = data_criacao or Tarefa.data_atual()
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def descricao(self):
        return self._descricao
    
    @property
    def concluida(self):
        return self._concluida
    
    @titulo.setter
    def titulo(self, novo_titulo):
        if not novo_titulo.strip():
            raise ValueError("Titulo não pode ser vazio!") # Pesquisar mais sobre raise
        self._titulo = novo_titulo

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
        self._concluida = True
    
    def reabrir(self):
        self._concluida = False
    
    # -- Conversão --
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "concluida": self.concluida,
            "data_criacao": self.data_criacao
        } # Atributo .__dict__ tbm pode ser usado para conversão
    
    @classmethod
    def from_dict(cls, dados_obj): #converte dict para obj
        return cls(
            titulo=dados_obj.get("titulo"),
            descricao=dados_obj.get("descricao"),
            concluida=dados_obj.get("concluida"),
            data_criacao=dados_obj.get("data_criacao")
        )

    # -- Métodos especiais (dunder methods)
    def __str__(self):
        estado = "[X]" if self.concluida else "[ ]"
        return f"{estado} {self.titulo} - {self.descricao} (criado em {self.data_criacao})"
    
    def __repr__(self):
        return f"Tarefa(titulo='{self.titulo}', descrição='{self.descricao}', concluida={self.concluida})"
    
class ListaTarefas:
    def __init__(self):
        self.tarefas = []
        
    def __iter__(self):
        return iter(self.tarefas)
    
    def __len__(self):
        return len(self.tarefas)
    
    def adicionar_tarefa(self, nova_tarefa):
        self.tarefas.append(nova_tarefa)
        
    def remover_tarefa(self, titulo:str):  # sourcery skip: use-next
        for index, tarefa in enumerate(self.tarefas): 
            if titulo == tarefa.titulo:
                return self.tarefas.pop(index)
        return None
    
    def salvar_em_arquivo(self, caminho):
        from task_manager import salvar_tarefas
        salvar_tarefas(self.tarefas, caminho)
    
    def carregar_do_arquivo(self, caminho):
        from task_manager import carregar_tarefas
        self.tarefas = carregar_tarefas(caminho)
    
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