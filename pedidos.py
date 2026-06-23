# Importa o pandas para trabalhar com tabelas.
import pandas as pd

# Importa a função text para executar consultas SQL.
from sqlalchemy import text

# Importa o objeto de conexão criado em conexao.py.
from conexao import engine


# Cria uma função para listar os pedidos.
def listar_pedidos():

    # Guarda a consulta SQL em uma variável.
    consulta = """
    SELECT
        c.Nome,
        p.Produto,
        p.Quantidade,
        p.ValorUnitario,
        p.Quantidade * p.ValorUnitario AS ValorTotal,
        p.DataPedido
    FROM Pedidos p
    INNER JOIN Clientes c
        ON c.Id = p.ClienteId
    ORDER BY p.Id
    """

    # Tenta executar a consulta.
    try:

        # Abre uma conexão com o banco de dados.
        with engine.connect() as conn:

            # Executa a consulta e armazena o resultado em um DataFrame.
            df = pd.read_sql(text(consulta), conn)

        # Verifica se o DataFrame retornou vazio.
        if df.empty:

            # Exibe uma mensagem caso não existam pedidos.
            print("\nNenhum pedido encontrado.")

        else:

            # Exibe o título da listagem.
            print("\nPedidos cadastrados:")

            # Exibe a tabela com os resultados.
            print(df)

    # Captura qualquer erro que ocorrer.
    except Exception as erro:

        # Exibe a mensagem de erro.
        print(f"\nErro ao listar pedidos: {erro}")

        # Importa a função executar_comando criada em utils.py.
from utils import executar_comando


# Cria uma função para cadastrar pedidos.
def cadastrar_pedido():

    # Pede o ID do cliente.
    cliente_id = int(input("Digite o ID do cliente: "))

    # Pede o nome do produto.
    produto = input("Digite o produto: ").strip()

    # Pede a quantidade.
    quantidade = int(input("Digite a quantidade: "))

    # Pede o valor unitário.
    valor_unitario = float(
        input("Digite o valor unitário: ").replace(",", ".")
    )

    # Verifica se o produto foi informado.
    if produto == "":

        print("\nErro: o produto não pode ficar vazio.")
        return

    # Cria o comando SQL.
    comando = """
    INSERT INTO Pedidos (
        ClienteId,
        Produto,
        Quantidade,
        ValorUnitario
    )
    VALUES (
        :cliente_id,
        :produto,
        :quantidade,
        :valor_unitario
    )
    """

    # Cria o dicionário de parâmetros.
    dados = {
        "cliente_id": cliente_id,
        "produto": produto,
        "quantidade": quantidade,
        "valor_unitario": valor_unitario
    }

    # Executa o comando SQL.
    registros = executar_comando(comando, dados)

    # Verifica se o INSERT funcionou.
    if registros > 0:
        print("\nPedido cadastrado com sucesso!")

        # Cria uma função para verificar se um cliente existe no banco.
def cliente_existe(cliente_id):

    # Consulta que procura um cliente pelo Id.
    consulta = """
    SELECT COUNT(*) AS Total
    FROM Clientes
    WHERE Id = :id
    """

    # Parâmetro enviado para o SQL.
    dados = {
        "id": cliente_id
    }

    # Abre conexão com o banco.
    with engine.connect() as conn:

        # Executa a consulta.
        df = pd.read_sql(text(consulta), conn, params=dados)

    # Retorna True se encontrou cliente.
    # Retorna False se não encontrou.
    return df.loc[0, "Total"] > 0