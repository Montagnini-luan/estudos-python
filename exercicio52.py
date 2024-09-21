"""
Exercício Análise de Números

Objetivo: Desenvolver um programa que solicita ao usuário a entrada de 
um número e, com base nesse número, realiza as seguintes operações:

    1. Mostrar o número informado.
    2. Informar se o número é par ou ímpar.
    3. Informar se o número é positivo, negativo ou zero.
    4. Se o número for positivo, calcular e mostrar sua raiz quadrada.

"""

numero = float(input("Digite um numero: "))

print(f"Seu numeor e: {numero}")

if numero % 2 == 0:
    print("Seu numero e par!")
else:
    print("Seu numero e impar!")

if numero > 0:
    print("Seu numero e positivo")
    quadrado = numero ** 0.5
    print(f"Raiz quadrada do seu numero e: {quadrado:.0f}")
elif numero < 0:
    print("Seu numero e negativo")
else:
    print("Seu numero e '0'")
