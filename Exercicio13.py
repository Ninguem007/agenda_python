agenda = []
while True:
    print("1 - Cadastro")
    print("2 - Pesquisa pelo nome")
    print("3 - Listar")
    print("4 - Alterar")
    print("5 - Excluir")
    print("6 - Sair")
    opcao = int(input("Informe a opção: "))

    if opcao == 1:
        pessoa = {}
        pessoa["Nome"] = input("Informe o Nome: ")
        pessoa["Email"] = input("Informe o Email: ")
        pessoa["Telefone"] = input("Informe o Telefone: ")
        agenda.append(pessoa)
    elif opcao == 2:
        busca = input("Informe o nome para busca: ")
        for elemento in agenda:
            if elemento["Nome"].lower() == busca.lower():
                print("")
    elif opcao == 3:
        for elemento in agenda:
            print(f"""{elemento["Nome"]}\t {elemento["Email"]}\t {elemento["Telefone"]}\t""")
    elif opcao == 4:
        busca = input("Informe o nome para busca: ")
        posicao = -1
        for elemento in agenda:
            if elemento["Nome"].lower() == busca.lower():
                break
            if posicao != -1:
                elemento[posicao]["Nome"] = input("Informe o Nome: ")
                elemento[posicao]["Email"] = input("Informe o Email: ")
                elemento[posicao]["Telefone"] = input("Informe o Telefone: ")
    elif opcao == 5:
        pass
    elif opcao.lower() == "n":
        break
    else:
        print("Opção inválida!")