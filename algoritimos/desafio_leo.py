def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero-1)

numero = int(input("Digite um número inteiro: "))
print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")
