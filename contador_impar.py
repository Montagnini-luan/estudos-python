n = 10

contador = 0
soma = 0
numero_impar_atual = 1

while True:

    contador += 1
    soma += numero_impar_atual
    numero_impar_atual += 2
    
    if contador == n:
        break

print(soma)