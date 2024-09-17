"""
Exercício: List Comprehensions

Objetivo: Familiarizar-se com a criação de listas usando a notação 
concisa de "List Comprehensions" em Python.

Instruções:

    1. Use uma list comprehension para criar uma lista dos dez primeiros 
    números elevados ao cubo e imprima o resultado.

    2. Use uma list comprehension para criar uma lista contendo todos os números 
    de 1 a 20 que são divisíveis por 3. Imprima o resultado.

    3. Dada a lista de palavras frutas = ["maçã", "banana", "manga", "uva", "abacaxi", "laranja"], 
    use uma list comprehension para criar uma lista com as frutas que possuem mais de 5 caracteres. 
    Imprima o resultado.

    4. Dada a lista notas = [89, 92, 56, 78, 45, 34, 90, 99, 65, 76, 80, 82], use 
    uma list comprehension para obter todas as notas acima de 75 e imprima o resultado.
"""

numeroscubo = [x**2 for x in range(11)]
print(numeroscubo)

divisaolista = [(x) for x in range(20) if x % 3 == 0]
print(divisaolista)

frutas = ["maçã", "banana", "manga", "uva", "abacaxi", "laranja"]

frutas5 = [fruta for fruta in frutas if len(fruta) > 5]
print(frutas5)

notas = [89, 92, 56, 78, 45, 34, 90, 99, 65, 76, 80, 82]

acimanotas = [nota for nota in notas if nota > 75 ]
print(acimanotas)
