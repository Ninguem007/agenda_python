salario = float(input("Informe seu salário:R$ "))
cargo = int(input("Informe seu código: "))

nome_cargo = ""
match cargo:
    case 100:
        percentual = 20
        nome_cargo = "Auxiliar Administrativo"
    case 101:
        percentual = 15
        nome_cargo = "Engenheiro"
    case 102:
        percentual = 10
        nome_cargo = "Gerente"
    case _:
        percentual = 0
        nome_cargo = "Cargo inválido!"

reajuste = salario * (percentual/100)
novo_salario = salario + reajuste
print(f"Cargo: {nome_cargo}\nSalário: {salario:.2f}\nReajuste: {reajuste:.2f}\nNovo Salário: {novo_salario:.2f}")