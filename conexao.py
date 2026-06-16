# Importa create_engine para criar a conexão com o SQL Server.

from sqlalchemy import create_engine

servidor = "CE080\\SQL2022"
banco = "EstudoPythonSQL"
conexao =  (
    f"mssql+pyodbc://@{servidor}/{banco}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

#Objeto de conexao

engine = create_engine(conexao)