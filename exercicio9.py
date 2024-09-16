
N = int(input("Digite um número positico e inteiro: "))
soma = 0

for i in range(1, N + 1):

    quadrado = i**2

    print(f"Quadrado de {i}: {quadrado}")

    soma += quadrado

print(f"A soma dos quadrados dos números de 1 até {N} é: {soma}")