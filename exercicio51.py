"""
Exercício:

Dada a matriz matriz_pessoas, escreva um programa que imprima 
os nomes das pessoas com mais de 30 anos.

    matriz_pessoas = [
    [["Ana", 25], ["Bruno", 31], ["Carlos", 29], ["Alice", 34]],
    [["Amanda", 22], ["Beatriz", 45], ["Clara", 30], ["Arnaldo", 27]],
    [["Alfredo", 35], ["Bianca", 28], ["Cesar", 32], ["Ariel", 23]],
    [["Alberto", 40], ["Beto", 24], ["Camila", 21], ["Adriana", 37]]
]

"""

matriz_pessoas = [
    [["Ana", 25], ["Bruno", 31], ["Carlos", 29], ["Alice", 34]],
    [["Amanda", 22], ["Beatriz", 45], ["Clara", 30], ["Arnaldo", 27]],
    [["Alfredo", 35], ["Bianca", 28], ["Cesar", 32], ["Ariel", 23]],
    [["Alberto", 40], ["Beto", 24], ["Camila", 21], ["Adriana", 37]]
]

for i in range(4):
    for j in range(4):
        nome = matriz_pessoas[i][j][0]

        idade = matriz_pessoas[i][j][1]

        if idade > 30:
            print(nome)

        