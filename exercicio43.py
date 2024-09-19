"""
Exercício: Compreensão de Dicionários (Dictionary Comprehension)

Objetivo: Familiarizar-se com a sintaxe básica da compreensão de dicionários em Python.


Instruções:

Dada a seguinte lista de números:

numeros = [1, 2, 3, 4, 5]

a) Use a compreensão de dicionário para criar um novo dicionário onde as 
chaves são os números da lista e os valores são os quadrados desses números.

Resultado esperado:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


Dica:

Para elevar um número ao quadrado, use o operador **. Por exemplo, 3**2 resulta em 9.


"""
 
numeros = [1, 2, 3, 4, 5]

quadrado = {}

for x in numeros:
    quadrado[x] = x **2
print(quadrado)



quadrado = {x: x**2 for x in numeros}
print(quadrado)