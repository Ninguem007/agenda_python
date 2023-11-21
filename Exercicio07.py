salario = float(input("Informe seu salário:R$ "))
cargo = int(input("Informe seu código: "))

nome_cargo=""
if cargo == 100:
    percentual = 20
    nome_cargo = "Assistente Administrativo"
elif cargo == 101:
    percentual = 15
    nome_cargo = "Engenheiro"
elif cargo == 102:
    percentual = 10
    nome_cargo = "Gerente"
else:
    percentual = 1
    nome_cargo = "Engenheiro"

reajuste = salario * (percentual/100)
novo_salario = salario + reajuste
print(f"Cargo: {nome_cargo}\nSalário: {salario:.2f}\nReajuste: {reajuste:.2f}\nNovo Salário: {novo_salario:.2f}")