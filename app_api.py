# Importa o Flask para criar a API.
from flask import Flask, jsonify, request

# Importa o pandas para consultar dados do banco.
import pandas as pd

# Importa text para executar SQL com parâmetros.
from sqlalchemy import text

# Importa a conexão com o banco.
from conexao import engine


# Cria a aplicação Flask.
app = Flask(__name__)

#Rota inicial da API
@app.route("/")
def home():
    return"""
<h1> PYTHON SQL API</h1>

<p>Rotas disponíveis:</p>

<ul>
    <li>/clientes<li>
</ul>
"""

# Cria uma rota GET para listar clientes.
@app.route("/clientes", methods=["GET"])
def listar_clientes_api():

    # Define a consulta SQL.
    consulta = """
    SELECT *
    FROM Clientes
    ORDER BY Id
    """

    # Abre conexão com o banco.
    with engine.connect() as conn:

        # Executa a consulta e guarda em DataFrame.
        df = pd.read_sql(text(consulta), conn)

    # Converte o DataFrame para lista de dicionários e retorna JSON.
    return jsonify(df.to_dict(orient="records"))


# Cria uma rota POST para cadastrar cliente.
@app.route("/clientes", methods=["POST"])
def cadastrar_cliente_api():

    # Lê o JSON enviado na requisição.
    dados_recebidos = request.get_json()

    # Pega o nome enviado no JSON.
    nome = dados_recebidos.get("nome", "").strip()

    # Pega a cidade enviada no JSON.
    cidade = dados_recebidos.get("cidade", "").strip()

    # Valida se nome veio vazio.
    if nome == "":
        return jsonify({"erro": "Nome é obrigatório"}), 400

    # Valida se cidade veio vazia.
    if cidade == "":
        return jsonify({"erro": "Cidade é obrigatória"}), 400

    # Define o comando SQL.
    comando = """
    INSERT INTO Clientes (Nome, Cidade)
    VALUES (:nome, :cidade)
    """

    # Define os parâmetros.
    dados = {
        "nome": nome,
        "cidade": cidade
    }

    # Executa o INSERT dentro de uma transação.
    with engine.begin() as conn:
        conn.execute(text(comando), dados)

    # Retorna mensagem de sucesso.
    return jsonify({"mensagem": "Cliente cadastrado com sucesso"}), 201


# Inicia a API.
if __name__ == "__main__":

    # Executa o servidor Flask em modo debug.
    app.run(debug=True)