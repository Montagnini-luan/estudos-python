"""
Exercício: Slicing de Listas

Objetivo: Familiarizar-se com o conceito de "slicing" em listas, acessando 
subconjuntos de listas e utilizando passos para selecionar elementos específicos.

Instruções:

    1. Crie uma lista chamada cores com os seguintes 
    elementos: "vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom", "cinza".

    2. Acesse e imprima as cores "verde" e "azul" usando slicing.

    3. Imprima as duas primeiras cores da lista utilizando slicing.

    4. Imprima todas as cores a partir da cor "amarelo" usando slicing.

    5. Imprima todas as cores em posições ímpares na 
    lista (ou seja, "vermelho", "azul", "laranja", "marrom") usando slicing com passos.

    6. Inverta a ordem das cores na lista usando slicing e imprima o resultado.
"""

elementos = ["vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom", "cinza"]

print(elementos[1:3])

print(elementos[0:2])

print(elementos[3:])

print(elementos[::2])

print(elementos[::-1])