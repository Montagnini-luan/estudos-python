"""
Exercício: Métodos de Listas

Objetivo: Aprofundar a compreensão sobre os métodos específicos das listas em Python.

Instruções:

    1. Crie uma lista chamada números contendo os 
    valores: 23, 11, 89, 34, 11, 56, 78, 90, 23, 45.

    2. Ordene a lista em ordem crescente usando o 
    método sort() e imprima o resultado.

    3. Use o método reverse() para inverter a ordem dos elementos 
    da lista e imprima o resultado.

    4. Conte quantas vezes o número 11 aparece na lista usando o 
    método count() e imprima o resultado.

    5. Encontre o índice da primeira ocorrência do número 78 usando o 
    método index() e imprima o resultado.

    6. Tente encontrar o índice de um número que não está na 
    lista (por exemplo, 100) e capture a exceção usando um 
    bloco try-except para exibir uma mensagem amigável.
"""

valores = [23, 11, 89, 34, 11, 56, 78, 90, 23, 45]

valores.sort()
print(valores)

valores.reverse()
print(valores)

numero11 = valores.count(11)
print(numero11)

ocorrencia78 = valores.index(78)
print(ocorrencia78)

try:
    ocorrenciaerro = valores.index(100)

except:
    print("O número 100 não está na lista.")

