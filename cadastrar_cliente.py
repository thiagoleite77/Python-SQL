# ==================================
# IMPORTAÇÕES
# ==================================

from sqlalchemy import create_engine, text

# ==================================
# CONFIGURAÇÕES DO BANCO
# ==================================

servidor = "CE080\\SQL2022"
banco = "EstudoPythonSQL"

conexao = (
    f"mssql+pyodbc://@{servidor}/{banco}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(conexao)
# ==================================
# ENTRADA DE DADOS
# ==================================

#Solicita o nome ao usuário
nome = input("Digite o nome do cliente: ")

#Solicita a cidade do usuário
cidade = input("Digite a cidade do cliente: ")


# ==================================
# COMANDO SQL
# ==================================

comando = """
INSERT INTO Clientes(Nome, Cidade)
VALUES (:nome, :cidade)
"""
dados = {
    "nome": nome,
    "cidade": cidade
}


# ==================================
# COMANDO SQL
# ==================================

with engine.begin()as conn:
    resultado = conn.execute(text(comando),dados)
    print("\nCliente cadatrado com sucesso!")
