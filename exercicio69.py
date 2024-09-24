"""
Exercicio 17
Exercício: Contagem em Intervalos

Desenvolva um programa que realize as seguintes funcionalidades:

    1. Leia uma quantidade indeterminada de números positivos.
    2. Conte quantos destes números estão nos seguintes intervalos:
        [0-25]
        [26-50]
        [51-75]
        [76-100]
    3. Exiba o total de números contabilizados em cada intervalo.
    4. A entrada de dados terminará quando for lido um número negativo.
    5. Bônus: Exiba a porcentagem de números em cada intervalo em relação ao total.
"""



lista_numeros = []

while True:
    num = int(input("Digite um numero positivo (digite um negativo para sair): "))

    if num >= 0:
            lista_numeros.append(num)
    else:
            break

intervalo1 = []
intervalo2 = []
intervalo3 = []
intervalo4 = []
print(lista_numeros)
for numero in lista_numeros:
        
    if 0 <= numero <= 25:
        intervalo1.append(numero)

    elif 26 <= numero <= 50:
        intervalo2.append(numero)

    elif 51 <= numero <= 75:
        intervalo3.append(numero)
        
    else:
        intervalo4.append(numero)

    porcentagem1 = (len(intervalo1) * 100) / len(lista_numeros)
    porcentagem2 = (len(intervalo2) * 100) / len(lista_numeros)
    porcentagem3 = (len(intervalo3) * 100) / len(lista_numeros)
    porcentagem4 = (len(intervalo4) * 100) / len(lista_numeros)

print(f"0 - 25 = {len(intervalo1)} ({porcentagem1}%)")
print(f"26 - 50 = {len(intervalo2)} ({porcentagem2}%)")
print(f"51 - 75 = {len(intervalo3)} ({porcentagem3}%)")
print(f"76 - 100 = {len(intervalo4)} ({porcentagem4}%)")