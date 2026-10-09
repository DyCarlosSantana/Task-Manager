# - `TarefaNaoEncontrada(Exception)` — quando título ou índice não corresponde a nenhuma tarefa.
# - `IndiceInvalido(Exception)` — quando o índice está fora dos limites (ex: negativo, maior que o tamanho).
# - `ArquivoInvalido(Exception)` — opcional, para quando a persistência falha de forma irrecuperável.

class TarefaNaoEncontrada(Exception):
    """Levantada quando uma tarefa não é encontrada (por título ou índice)."""
    pass

class IndiceInvalido(Exception):
    """Levantada quando o índice passado está fora do intervalo válido."""
    pass

class ArquivoInvalido(Exception):
    """Levantanda quando o arquivo de destino (path) é invalido"""
    pass
