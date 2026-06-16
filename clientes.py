import pandas as pd

from sqlalchemy import text

from conexao import engine 

def listar_clientes():
    consulta = """
    SELECT * FROM 
    Clientes ORDER BY Id"""   

    df = pd.read_sql(consulta,engine)

    print("\nClientes Cadastrados: ")
    print(df)

# Cria uma função para cadastrar um novo cliente.
def cadastrar_cliente():

    # Pede o nome do cliente pelo terminal.
    nome = input("Digite o nome do cliente: ")

    # Pede a cidade do cliente pelo terminal.
    cidade = input("Digite a cidade do cliente: ")

    # Remove espaços no começo e no fim do nome.
    # Exemplo: "  Thiago  " vira "Thiago".
    nome = nome.strip()

    # Remove espaços no começo e no fim da cidade.
    # Exemplo: "  São Paulo  " vira "São Paulo".
    cidade = cidade.strip()

    # Verifica se o nome ficou vazio.
    # Isso acontece se o usuário apertar Enter sem digitar nada.
    if nome == "":

        # Mostra uma mensagem de erro.
        print("\nErro: o nome não pode ficar vazio.")

        # Encerra a função aqui.
        # Nada será enviado para o banco.
        return

    # Verifica se a cidade ficou vazia.
    if cidade == "":

        # Mostra uma mensagem de erro.
        print("\nErro: a cidade não pode ficar vazia.")

        # Encerra a função aqui.
        # Nada será enviado para o banco.
        return

    # Guarda o comando SQL de inserção.
    comando = """
    INSERT INTO Clientes (Nome, Cidade)
    VALUES (:nome, :cidade)
    """

    # Cria um dicionário com os valores que serão enviados para o SQL.
    dados = {
        "nome": nome,
        "cidade": cidade
    }

    try:
        with engine.begin() as conn:

            conn.execute(text(comando),dados)
            print ("\nCliente cadastrado com sucesso!")

    except Exception as erro:
        print(f"\n Erro ao cadastrar cliente: {erro}")

# Cria uma função para atualizar a cidade de um cliente.
def atualizar_cliente():

    # Pede o ID do cliente que será atualizado.
    id_cliente = ler_id_cliente()

    # Pede a nova cidade do cliente.
    nova_cidade = input("Digite a nova cidade: ")

    # Guarda o comando SQL de atualização.
    comando = """
    UPDATE Clientes
    SET Cidade = :cidade
    WHERE Id = :id
    """

    # Cria um dicionário com os valores enviados para o SQL.
    dados = {
        "cidade": nova_cidade,
        "id": id_cliente
    }

    # Abre uma transação com o banco.
    with engine.begin() as conn:

        # Executa o UPDATE e guarda o resultado.
        resultado = conn.execute(text(comando), dados)

    # Exibe quantos registros foram atualizados.
    print(f"\n{resultado.rowcount} registro(s) atualizado(s).")


# Cria uma função para excluir um cliente.
def excluir_cliente():

    # Pede o ID do cliente que será excluído.
    id_cliente = ler_id_cliente()

    # Guarda o comando SQL de exclusão.
    comando = """
    DELETE FROM Clientes
    WHERE Id = :id
    """

    # Cria um dicionário com o ID enviado para o SQL.
    dados = {
        "id": id_cliente
    }

    # Abre uma transação com o banco.
    with engine.begin() as conn:

        # Executa o DELETE e guarda o resultado.
        resultado = conn.execute(text(comando), dados)

    # Exibe quantos registros foram excluídos.
    print(f"\n{resultado.rowcount} registro(s) excluído(s).")


def ler_id_cliente():

    while True:

        valor = input("Digite o Id do cliente: ")

        if valor.isdigit(): #Verifica se o valor digitado contém apenas números.
           return int(valor) #Converte o texto digitado para numero inteiro e retorna 

        print ("ID inválido. Digite apenas números.")
