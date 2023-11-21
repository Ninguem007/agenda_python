somatorio = 0
quantidade_numeros = 10

for i in range(quantidade_numeros):
    numero = float(input(f"Digite o {i + 1}º número: "))
    
    somatorio += numero

media = somatorio / quantidade_numeros

print("\nResultados:")
print(f"Somatório: {somatorio}")
print(f"Média: {media:.2f}")
