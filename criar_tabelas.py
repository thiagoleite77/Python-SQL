from sqlalchemy import text

from conexao import engine

comando = """
CREATE TABLE Pedidos(
    --identificador único do pedido
    Id INT IDENTITY (1,1) PRIMARY KEY,
    
    --Referência ao cliente
    ClienteID INT NOT NULL,
    
    --Nome do Produto
    Produto NVARCHAR(100) NOT NULL,
    
    --Quantidade comprada
    Quantidade INT NOT NULL,
    
    --Valor unitário do produto.
    ValorUnitario DECIMAL (10,2) NOT NULL,
    
    --Data de Criação do pedido.
    DataPedido DATETIME DEFAULT GETDATE(),
    
    -- Cria a chave estrangeira.
    CONSTRAINT FK_Pedidos_Clientes
    FOREIGN KEY (CLienteId)
    REFERENCES Clientes(Id)  
)
"""

try:
    with engine.begin() as conn:
        
        conn.execute(text(comando))
    print("Tabela de pedidos criada com sucesso")

except Exception as erro:
    print(f"Erro ai criar tabela: {erro}")
