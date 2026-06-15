# ==================================
# IMPORTAÇÕES
# ==================================

# Importa a biblioteca pandas e cria o apelido "pd".
# O pandas será usado para trabalhar com tabelas de dados.
import pandas as pd

# Importa a função create_engine da biblioteca SQLAlchemy.
# Ela será responsável por criar a conexão com o banco.
from sqlalchemy import create_engine


# ==================================
# CONFIGURAÇÕES DO BANCO DE DADOS
# ==================================

# Define o nome da instância do SQL Server.
# A dupla barra (\\) é necessária porque a barra invertida (\)
# possui significado especial no Python.
servidor = "CE080\\SQL2022"

# Define o nome do banco de dados.
banco = "EstudoPythonSQL"


# ==================================
# STRING DE CONEXÃO
# ==================================

# Cria a string de conexão que será usada pelo SQLAlchemy.
conexao = (
    # Define o tipo de banco de dados e a biblioteca de conexão.
    f"mssql+pyodbc://@{servidor}/{banco}"

    # Define o driver ODBC utilizado para acessar o SQL Server.
    "?driver=ODBC+Driver+17+for+SQL+Server"

    # Informa que será utilizada a autenticação do Windows.
    "&trusted_connection=yes"
)


# ==================================
# CRIAÇÃO DA CONEXÃO
# ==================================

# Cria o objeto de conexão.
engine = create_engine(conexao)

# Testa a conexão com o banco.
with engine.connect() as conn:
    print("Conexão realizada com sucesso!")


# ==================================
# CONSULTA SQL
# ==================================

# As três aspas permitem escrever um texto com várias linhas.
# O conteúdo desse texto é uma consulta SQL.
consulta = """
SELECT
    c.Nome,
    p.Produto,
    p.Quantidade,
    p.ValorUnitario,
    p.Quantidade * p.ValorUnitario AS ValorTotal
FROM Pedidos p
INNER JOIN Clientes c
    ON c.Id = p.ClienteId
"""


# ==================================
# EXECUÇÃO DA CONSULTA
# ==================================

# Executa a consulta SQL usando a conexão criada.
# O resultado é armazenado em um DataFrame.
df = pd.read_sql(consulta, engine)


# ==================================
# EXIBIÇÃO DOS DADOS
# ==================================

# Exibe a tabela retornada pela consulta.
print("\nResultado da consulta:")
print(df)


# ==================================
# ANÁLISE DOS DADOS COM PYTHON
# ==================================

# Soma todos os valores da coluna ValorTotal.
print("\nSoma dos pedidos:")
print(df["ValorTotal"].sum())

# Calcula a média dos valores da coluna ValorTotal.
print("\nMédia dos pedidos:")
print(df["ValorTotal"].mean())

# Retorna o maior valor da coluna ValorTotal.
print("\nMaior pedido:")
print(df["ValorTotal"].max())

# ==================================
# INSERÇÃO DE DADOS
# ==================================

#Importa a funcão texto do SQÇALcemy
#Ela permite executar comando SQL diretamente do Python

from sqlalchemy import text #text transforma uma string em um comando SQL executavel

#Define o comando SQL que sera executado. o que esta dentro das """ ´q oe eu vou executar dentro do banco
comando = """
INSERT INTO CLientes (Nome, Cidade)
VALUES(:nome, :cidade)
"""
#Cria um dicionário com os valores que serão enviados

dados = {
    "nome": "Ana costa",
    "cidade": "São paulo"
}

#Abre uma conexão com o banco
with engine.begin() as conn:
    
    #Executa o comando SQL usando os dados iformados.
    conn.execute(text(comando),dados)

    #exibe uma mensagem de conformação.
    print("\nCliente inserido com sucesso!")

from sqlalchemy import text

# ==================================
# ATUALIZAÇÃO DE DADOS (UPDATE)
# ==================================

from sqlalchemy import text

#Define a consulta SQL que será executada

comando_update = """
UPDATE Clientes
SET Cidade = :cidade
WHERE Id = :id
"""

#Define os valores que serão enviados para a consulta

dados_update = {
    "cidade": "São Caetano do Sul",
    "id": 1
}

#Abre uma conexão e inicia uma transação
with engine.begin() as conn:

    #Executa o comando SQL usando os valores definidos
    resultado = conn.execute(text(comando_update), dados_update)

    #Exibe quantas linhas foram alteradas.
    print(f"\n{resultado.rowcount}registro(s) atualizado(s)")

# ==================================
# EXCLUSÃO DE DADOS (DELETE)
# ==================================

# Define o comando SQL para excluir um cliente
comando_delete = """
DELETE FROM Clientes
WHERE Id = :id
"""
#Define qual cliente será excluido
dados_delete = {
    "id":4
}

#Abre uma transação
with engine.connect() as conn:
    #inicia uma transação manualmente.
    transacao = conn.begin()

    try:
        #executa o comando SQL
        resultado = conn.execute(text(comando_delete),dados_delete)
        # confirma a transação
        transacao.commit()
        #exibe a quantidade de registros excluídos
        print(f"\n{resultado.rowcount} registro(s) excluído(s). ")

    except Exception as erro:
        #Desfaz a transação em caso de erro
        transacao.rollback()

        #Exibe a mensagem de erro
        print(f"\nErro ao excluir registro:{erro}")