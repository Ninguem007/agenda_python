pessoa1 = {}

pessoa1['nome'] = input("Informe o nome: ")
pessoa1['email'] = input("Insira o email: ")
pessoa1['telefone'] = input('Digite seu telefone: ')

agenda = []
agenda.append(pessoa1)

for contato in agenda:
    print(contato['nome'])
    for contato in agenda:
     print(contato['email'])
    for contato in agenda:
     print(contato['telefone    '])