agenda = {}  # Dicionário para armazenar os contatos

def cadastrar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o e-mail do contato: ")

    if nome in agenda:
        print("Contato já existe na agenda.")
    else:
        agenda[nome] = {"Telefone": telefone, "E-mail": email}
        print("Contato cadastrado com sucesso.")

def pesquisar_contato():
    nome = input("Digite o nome para pesquisa: ")
    if nome in agenda:
        print(f"\nNome: {nome}\nTelefone: {agenda[nome]['Telefone']}\nE-mail: {agenda[nome]['E-mail']}")
    else:
        print("Contato não encontrado.")

def listar_contatos():
    if not agenda:
        print("A agenda está vazia.")
    else:
        print("\nLista de contatos:")
        for nome, detalhes in agenda.items():
            print(f"Nome: {nome}\nTelefone: {detalhes['Telefone']}\nE-mail: {detalhes['E-mail']}\n")

def alterar_contato():
    nome = input("Digite o nome do contato que deseja alterar: ")
    if nome in agenda:
        telefone = input("Digite o novo telefone: ")
        email = input("Digite o novo e-mail: ")
        agenda[nome] = {"Telefone": telefone, "E-mail": email}
        print("Contato alterado com sucesso.")
    else:
        print("Contato não encontrado.")

def excluir_contato():
    nome = input("Digite o nome do contato que deseja excluir: ")
    if nome in agenda:
        del agenda[nome]
        print("Contato excluído com sucesso.")
    else:
        print("Contato não encontrado.")

def main():
    while True:
        print("\nMenu:")
        print("a - Cadastrar Contato")
        print("b - Pesquisar Contato")
        print("c - Listar Contatos")
        print("d - Alterar Contato")
        print("e - Excluir Contato")
        print("n - Sair")

        opcao = input("Escolha uma opção: ").lower()

        if opcao == "a":
            cadastrar_contato()
        elif opcao == "b":
            pesquisar_contato()
        elif opcao == "c":
            listar_contatos()
        elif opcao == "d":
            alterar_contato()
        elif opcao == "e":
            excluir_contato()
        elif opcao == "n":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
