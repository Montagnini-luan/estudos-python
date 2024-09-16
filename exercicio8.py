"""
Exercício: Tabela de Multiplicação

Objetivo: Escreva um programa que peça ao usuário um número inteiro positivo NN e 
exiba a tabela de multiplicação para esse número, de 1 a 10. Utilize um loop for para esta tarefa.

Etapas:

    - Solicite ao usuário um número inteiro positivo NN.
    - Utilize um loop for para iterar de 1 a 10.
    - Para cada iteração, multiplique o número NN pelo valor da iteração e imprima o resultado.
    
Exemplo de Saída:

Digite um número inteiro positivo para exibir a sua tabela de multiplicação: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
Fim da tabela de multiplicação.

"""

NN = int(input("Digite um número positivo e inteiro: "))

for i in range(1, 11):

    print(f"{NN} x {i} = {NN * i}")

print("Fim da tabela de multiplicação.")