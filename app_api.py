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


# Rota inicial da API.
@app.route("/")
def home():
    return """
    <h1>PYTHON SQL API</h1>

    <p>Rotas disponíveis:</p>

    <ul>
        <li>GET /clientes</li>
        <li>GET /clientes/&lt;id&gt;</li>
        <li>POST /clientes</li>
        <li>PUT /clientes/&lt;id&gt;</li>
        <li>DELETE /clientes/&lt;id&gt;</li>
    </ul>
    """


# Lista todos os clientes. =========================GET
@app.route("/clientes", methods=["GET"])
def listar_clientes_api():
    consulta = """
    SELECT *
    FROM Clientes
    ORDER BY Id
    """

    with engine.connect() as conn:
        df = pd.read_sql(text(consulta), conn)

    return jsonify(df.to_dict(orient="records"))


# Busca cliente por ID.================================= GET ID
@app.route("/clientes/<int:id>", methods=["GET"])
def buscar_cliente_por_id(id):
    consulta = """
    SELECT *
    FROM Clientes
    WHERE Id = :id
    """

    dados = {"id": id}

    with engine.connect() as conn:
        df = pd.read_sql(text(consulta), conn, params=dados)

    if df.empty:
        return jsonify({"erro": "Cliente não encontrado"}), 404

    return jsonify(df.to_dict(orient="records")[0])


# Cadastra cliente. =============================================== POST
@app.route("/clientes", methods=["POST"])
def cadastrar_cliente_api():
    dados_recebidos = request.get_json()

    if dados_recebidos is None:
        return jsonify({"erro": "Envie um JSON válido"}), 400

    nome = dados_recebidos.get("nome", "").strip()
    cidade = dados_recebidos.get("cidade", "").strip()

    if nome == "":
        return jsonify({"erro": "Nome é obrigatório"}), 400

    if cidade == "":
        return jsonify({"erro": "Cidade é obrigatória"}), 400

    comando = """
    INSERT INTO Clientes (Nome, Cidade)
    VALUES (:nome, :cidade)
    """

    dados = {"nome": nome, "cidade": cidade}

    with engine.begin() as conn:
        conn.execute(text(comando), dados)

    return jsonify({"mensagem": "Cliente cadastrado com sucesso"}), 201


# Atualiza cliente. ======================================PUT
@app.route("/clientes/<int:id>", methods=["PUT"])
def atualizar_cliente(id):
    dados_recebidos = request.get_json()

    if dados_recebidos is None:
        return jsonify({"erro": "Envie um JSON válido"}), 400

    nome = dados_recebidos.get("nome", "").strip()
    cidade = dados_recebidos.get("cidade", "").strip()

    if nome == "":
        return jsonify({"erro": "Nome é obrigatório"}), 400

    if cidade == "":
        return jsonify({"erro": "Cidade é obrigatória"}), 400

    comando = """
    UPDATE Clientes
    SET Nome = :nome,
        Cidade = :cidade
    WHERE Id = :id
    """

    dados = {"nome": nome, "cidade": cidade, "id": id}

    with engine.begin() as conn:
        resultado = conn.execute(text(comando), dados)

    if resultado.rowcount == 0:
        return jsonify({"erro": "Cliente não encontrado"}), 404

    return jsonify({"mensagem": "Cliente atualizado com sucesso"})


# Exclui cliente. ============================================== DELETE
@app.route("/clientes/<int:id>", methods=["DELETE"])
def excluir_cliente(id):
    comando = """
    DELETE FROM Clientes
    WHERE Id = :id
    """

    dados = {"id": id}

    with engine.begin() as conn:
        resultado = conn.execute(text(comando), dados)

    if resultado.rowcount == 0:
        return jsonify({"erro": "Cliente não encontrado"}), 404

    return jsonify({"mensagem": "Cliente excluído com sucesso"})


# Inicia a API.
if __name__ == "__main__":
    app.run(debug=True)
