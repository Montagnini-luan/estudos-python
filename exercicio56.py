"""
Exercício Análise de Números Inteiros e Reais

Objetivo: Desenvolver um programa que obtenha do usuário dois 
números inteiros e um número real, e em seguida realize e apresente 
uma série de cálculos e análises relacionadas a esses números.

Instruções:

    1. Solicite ao usuário dois números inteiros.
    2. Solicite ao usuário um número real.
    3. Calcule e exiba o produto do dobro do primeiro número com metade do segundo.
    4. Calcule e exiba a soma do triplo do primeiro número com o terceiro número.
    5. Calcule e exiba o terceiro número elevado ao cubo.
    6. Determine e informe se o primeiro número é par ou ímpar.
    7. Determine e informe se o terceiro número é positivo, negativo ou zero.
    8. Calcule e mostre a média aritmética entre os três números.
"""

num1 = int(input("digite o primeiro numero inteiro: "))
num2 = int(input("digite o segundo numero inteiro: "))
num3 = float(input("digite o numero real: "))

produto1 = (num1 * 2 ) * (num2 / 2)

print(f"produto do dobro do {num1} com metade do {num2} e: {produto1}")

produto2 = (num1 * 3) + num3

print(f"a soma do triplo do {num1} com o {num3} e: {produto2}")

produto3 = num3 ** 2

print(f"o {num3} elevado ao cubo e: {produto3}")

if num1 % 2 == 0:
    print("O primeiro numero e par")
else:
    print("O primeiro numero e impar")

produto4 = "positivo" if num3 > 0 else "negativo" if num3 < 0 else "Zero"

print(produto4)

produto5 = (num1 + num2 + num3) / 3

print("a média aritmética entre os três números e: ", produto5)