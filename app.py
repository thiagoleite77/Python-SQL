# ==================================
# IMPORTAÇÕES
# ==================================

# Importa o pandas para trabalhar com tabelas.
import pandas as pd

# Importa as funções necessárias do SQLAlchemy.
from sqlalchemy import create_engine, text


# ==================================
# CONFIGURAÇÕES DO BANCO DE DADOS
# ==================================

# Define o nome do servidor SQL Server.
servidor = "CE080\\SQL2022"

# Define o nome do banco de dados.
banco = "EstudoPythonSQL"


# ==================================
# STRING DE CONEXÃO
# ==================================

# Monta a string de conexão.
conexao = (
    f"mssql+pyodbc://@{servidor}/{banco}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# Cria o objeto de conexão.
engine = create_engine(conexao)


# ==================================
# LOOP PRINCIPAL DO SISTEMA
# ==================================

# O while True mantém o sistema em execução até o usuário escolher sair.
while True:

    # Exibe o menu.
    print("\n===== SISTEMA PYTHON + SQL =====")
    print("1 - Listar clientes")
    print("2 - Cadastrar cliente")
    print("3 - Atualizar cliente")
    print("4 - Excluir cliente")
    print("5 - Sair")

    # Recebe a opção digitada pelo usuário.
    opcao = input("\nEscolha uma opção: ")

    # O match-case funciona como o switch-case.
    match opcao:

        # ==========================
        # LISTAR CLIENTES
        # ==========================

        case "1":

            # Define a consulta SQL.
            consulta = """
            SELECT *
            FROM Clientes
            ORDER BY Id
            """

            # Executa a consulta e armazena o resultado.
            df = pd.read_sql(consulta, engine)

            # Exibe o resultado.
            print("\nClientes cadastrados:")
            print(df)

        # ==========================
        # CADASTRAR CLIENTE
        # ==========================

        case "2":

            # Solicita os dados do cliente.
            nome = input("Digite o nome do cliente: ")
            cidade = input("Digite a cidade do cliente: ")

            # Define o comando SQL.
            comando = """
            INSERT INTO Clientes (Nome, Cidade)
            VALUES (:nome, :cidade)
            """

            # Cria o dicionário com os parâmetros.
            dados = {
                "nome": nome,
                "cidade": cidade
            }

            # Executa o INSERT.
            with engine.begin() as conn:
                conn.execute(text(comando), dados)

            print("\nCliente cadastrado com sucesso!")

        # ==========================
        # ATUALIZAR CLIENTE
        # ==========================

        case "3":

            # Solicita os dados para atualização.
            id_cliente = int(input("Digite o ID do cliente: "))
            nova_cidade = input("Digite a nova cidade: ")

            # Define o comando SQL.
            comando = """
            UPDATE Clientes
            SET Cidade = :cidade
            WHERE Id = :id
            """

            # Cria o dicionário com os parâmetros.
            dados = {
                "cidade": nova_cidade,
                "id": id_cliente
            }

            # Executa o UPDATE.
            with engine.begin() as conn:
                resultado = conn.execute(text(comando), dados)

            print(f"\n{resultado.rowcount} registro(s) atualizado(s).")

        # ==========================
        # EXCLUIR CLIENTE
        # ==========================

        case "4":

            # Solicita o ID do cliente.
            id_cliente = int(input("Digite o ID do cliente que deseja excluir: "))

            # Define o comando SQL.
            comando = """
            DELETE FROM Clientes
            WHERE Id = :id
            """

            # Cria o dicionário com os parâmetros.
            dados = {
                "id": id_cliente
            }

            # Executa o DELETE.
            with engine.begin() as conn:
                resultado = conn.execute(text(comando), dados)

            print(f"\n{resultado.rowcount} registro(s) excluído(s).")

        # ==========================
        # SAIR DO SISTEMA
        # ==========================

        case "5":

            print("\nEncerrando o sistema...")
            break

        # ==========================
        # OPÇÃO INVÁLIDA
        # ==========================

        case _:

            print("\nOpção inválida. Tente novamente.")