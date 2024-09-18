"""
Exercício: Utilidades e Funções com Listas

Objetivo: Compreender e aplicar funções úteis que interagem 
com listas em Python.

Instruções:

    Dada a lista valores = [23, 45, 67, 89, 12, 56, 78, 90, 34, 56], determine 
    e imprima o número de elementos na lista usando a função len().

    Ainda utilizando a lista valores, encontre e imprima o maior e o menor valor 
    presente na lista usando as funções max() e min().

    Calcule e imprima a soma de todos os elementos na lista valores 
    usando a função sum().

    Crie uma lista pesos com os seguintes valores: 58.5, 63.2, 71.3, 69.4, 68.2. 
    Calcule e imprima a média dos pesos usando as funções sum() e len().
"""

valores = [23, 45, 67, 89, 12, 56, 78, 90, 34, 56]

print("O número de elementos é ", len(valores))

print("o valor maior é ", max(valores), "\nO valor menor é ", min(valores))

print("A soma dos valores é ", sum(valores))

pesos = [58.5, 63.2, 71.3, 69.4, 68.2]

mediaPesos = sum(pesos) / len(pesos)

print(f"A média de peso é {mediaPesos}")