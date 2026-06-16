# Importa as funções do arquivo clientes.py.
from clientes import listar_clientes, cadastrar_cliente, atualizar_cliente, excluir_cliente


def exibir_menu():
    print("\n===== SISTEMA PYTHON + SQL =====")
    print("1 - Listar clientes")
    print("2 - Cadastrar cliente")
    print("3 - Atualizar cliente")
    print("4 - Excluir cliente")
    print("5 - Sair")


while True:
    exibir_menu()

    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            listar_clientes()

        case "2":
            cadastrar_cliente()
        
        case "3":
            atualizar_cliente()
        
        case"4":
            excluir_cliente()

        case "5":
            print("\nEncerrando o sistema...")
            break

        case _:
            print("\nOpção inválida.")