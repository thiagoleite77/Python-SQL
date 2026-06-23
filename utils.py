# Importa a função text para transformar strings em comandos SQL.
from sqlalchemy import text

# Importa o objeto de conexão criado em conexao.py.
from conexao import engine


# Cria uma função genérica para executar comandos SQL.
def executar_comando(comando, dados):

    # Tenta executar o comando.
    try:

        # Abre uma transação.
        with engine.begin() as conn:

            # Executa o comando SQL.
            resultado = conn.execute(text(comando), dados)

        # Retorna a quantidade de registros afetados.
        return resultado.rowcount

    # Captura qualquer erro.
    except Exception as erro:

        # Exibe a mensagem de erro.
        print(f"\nErro: {erro}")

        # Retorna zero para indicar falha.
        return 0