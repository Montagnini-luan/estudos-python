"""
Exercício: Soma dos Números Pares em uma Matriz 4x4

Enunciado:

Dada a seguinte matriz 4x4:
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16

    - Escreva um programa em Python que percorre cada elemento da matriz.
    - Some todos os números pares presentes na matriz.
    - Imprima o resultado da soma.

Dica: Use loops for aninhados para percorrer cada linha e coluna da matriz. 
Utilize o operador % para verificar se um número é par.

Ao resolver o exercício, os alunos devem ser capazes de navegar pelos elementos 
da matriz, aplicar condições lógicas e acumular valores baseados em critérios específicos.
"""

M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

soma_pares = 0

for linha in range(4):

    for coluna in range(4):
    
        if M[linha][coluna] % 2 == 0:

            soma_pares += M[linha][coluna]
            
print(soma_pares)

