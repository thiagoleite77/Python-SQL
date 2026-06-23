import pandas as pd

from sqlalchemy import text

from conexao import engine 

from utils import executar_comando

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

    registros = executar_comando(comando, dados)
    print(f"\n{registros} Cliente inserido com sucesso")

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

    registros = executar_comando(comando, dados)
    print(f"\n{registros} registro(s) atualizado(s)")


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
    registros = executar_comando(comando, dados)
    print(f"\n{registros} cliente excluido")

def ler_id_cliente():

    while True:

        valor = input("Digite o Id do cliente: ")

        if valor.isdigit(): #Verifica se o valor digitado contém apenas números.
           return int(valor) #Converte o texto digitado para numero inteiro e retorna 

        print ("ID inválido. Digite apenas números.")

# Cria uma função para buscar clientes pelo nome.
def buscar_cliente_por_nome():

    # Pede ao usuário uma parte do nome que ele quer pesquisar.
    nome = input("Digite o nome ou parte do nome do cliente: ").strip()

    # Verifica se o usuário não digitou nada.
    if nome == "":

        # Mostra mensagem de erro.
        print("\nErro: informe um nome para pesquisar.")

        # Encerra a função.
        return

    # Cria a consulta SQL com filtro usando LIKE.
    consulta = """
    SELECT *
    FROM Clientes
    WHERE Nome LIKE :nome
    ORDER BY Id
    """

    # Cria o dicionário com o parâmetro.
    # O % antes e depois permite buscar o texto em qualquer parte do nome.
    dados = {
        "nome": f"%{nome}%"
    }

    try:

        # Abre uma conexão com o banco.
        with engine.connect() as conn:

            # Executa a consulta usando text() para o SQLAlchemy entender o parâmetro :nome.
            df = pd.read_sql(text(consulta), conn, params=dados)

        # Verifica se a tabela voltou vazia.
        if df.empty:

            # Mostra mensagem caso nenhum cliente seja encontrado.
            print("\nNenhum cliente encontrado.")

        else:

            # Mostra os clientes encontrados.
            print("\nClientes encontrados:")
            print(df)

    except Exception as erro:

        # Mostra a mensagem do erro sem quebrar o sistema.
        print(f"\nErro ao buscar cliente: {erro}")

def buscar_cliente_por_cidade():

    cidade = input ("Digite a cidade ou parte da cidade:").strip()
    
    if cidade ==""
    print("\nErro: informe uma cidade para pesquisar.")
    return

    consulta = """
    SELECT * 
    FROM Clientes
    WHERE Cidade LIKE : cidade
    ORDER BY id
    """
    
    dados = {
        "cidade" : f"%{cidade}%"
    }
    
    try:
        
        with engine.connect() as conn:
            df = pd.read_sql(text(consulta), conn, params=dados)
            
        if df.empty:
            print("\nNenhum cliente encontrado.")
        else:
            print("\nClientes encpontrados: ")
            print(df)
    
    except Exception as erro:
        print("\nErro ao buscar cliente por cidade: {erro}")
            
    