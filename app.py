# ==================================
# IMPORTAÇÕES
# ==================================

# Importa o pandas para ler dados do banco em formato de tabela.
import pandas as pd

# Importa create_engine para conectar no banco.
# Importa text para executar comandos SQL com segurança.
from sqlalchemy import create_engine, text

# ==================================
# CONFIGURAÇÕES DO BANCO
# ==================================

# Nome do servidor SQL Server.
servidor = "CE080\\SQL2022"

# Nome do banco de dados.
banco = "EstudoPythonSQL"

# ==================================
# CONEXÃO COM O BANCO
# ==================================

# Monta a string de conexão com SQL Server.
conexao = (
    f"mssql+pyodbc://@{servidor}/{banco}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# Cria o objeto de conexão.
engine = create_engine(conexao)
# ==================================
# MENU PRINCIPAL
# ==================================

#Exibe as opções para o usuário