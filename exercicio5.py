"""
Exercício:

Crie um algoritmo que leia números inteiros positivos digitados pelo usuário
até que o usuário digite um número menor que 0. No final, imprima o maior número digitado.

"""
maior_numero = 0

numero_digitado = int(input("Digite uma lista de números positivos e inteiros, digite um numero menor do que 0 para sair: "))

while numero_digitado >= 0:

    if numero_digitado > maior_numero:

        maior_numero = numero_digitado
        
    numero_digitado = int(input("Digite uma lista de números positivos e inteiros, digite um numero menor do que 0 para sair: "))

print("O maior numro digitado foi:", maior_numero)