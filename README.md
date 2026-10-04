# Task Manager

> Gerenciador de tarefas em Python que estou usando para praticar orientação a objetos de forma séria: modelagem de classes, encapsulamento, persistência em arquivo e testes automatizados.

---

## Sobre o projeto

Diferente dos meus cadernos de estudo soltos, este repositório eu tratei como um projeto de verdade: separei o domínio da aplicação (`Tarefa`, `ListaTarefas`) da camada de persistência, e escrevi testes para cada peça antes de considerar algo "pronto". O foco aqui não é só "fazer funcionar", mas praticar decisões de design — por que usar `@property` em vez de atributo público, como validar dados no construtor, como separar responsabilidades entre modelo e armazenamento.

Ainda é um projeto em evolução: hoje ele funciona como uma biblioteca Python testável, mas a camada de interface (linha de comando) ainda está em aberto.

---

## Estrutura e organização do repositório

- **`task_manager/`** — o pacote principal:
  - `modelo.py` — as classes de domínio, `Tarefa` e `ListaTarefas`, com encapsulamento via `@property`, validações nos setters e métodos especiais (`__str__`, `__repr__`, `__iter__`, `__len__`).
  - `persistencia.py` — funções para salvar e carregar tarefas em JSON, com tratamento de erros (arquivo ausente, JSON corrompido).
  - `cli.py` — reservado para a futura interface de linha de comando (ainda não implementada).
- **`tests/`** — suíte de testes com `pytest`, cobrindo o modelo, a lista de tarefas e a persistência (incluindo casos de borda como JSON corrompido e diretório inexistente).
- **`main.py`** — um script de demonstração que carrega, manipula e salva tarefas, só para exercitar o pacote na prática.
- **`dados/`** — onde o arquivo JSON de tarefas é salvo em tempo de execução (ignorado pelo Git).


---

## Tecnologias

- **Python** puro para o pacote principal (sem dependências externas no código da aplicação)
- **pytest** e **pytest-cov** para os testes e cobertura
- **coverage** para medir a cobertura dos testes

---

## ▶ Como rodar

Instale as dependências de desenvolvimento:

```bash
pip install -r requeriment.txt
```

Execute o script de demonstração:

```bash
python main.py
```

Rode a suíte de testes:

```bash
pytest
```

---

## 🚧 Estado atual

Este projeto está em desenvolvimento ativo, como prática de orientação a objetos. No momento:

- O modelo de dados (`Tarefa`, `ListaTarefas`) e a persistência em JSON já estão implementados e cobertos por testes.
- A interface de linha de comando (`cli.py`) ainda está vazia — é o próximo passo natural para tornar o projeto utilizável fora de um script de exemplo.

Não pretendo detalhar aqui cada funcionalidade pontual que for adicionando — esta seção serve só para indicar o estágio geral do projeto.

---

## Autor ✍️

**Edy Carlos de Santana Souza**
[GitHub: @DyCarlosSantana](https://github.com/DyCarlosSantana)