"""
Exercício - Análise Comparativa e Estatística de Números

Objetivo: Desenvolver um programa que obtenha do usuário dez números e realize 
análises estatísticas e matemáticas com base nos valores inseridos.

Instruções:

    1. Solicite ao usuário que informe dez números.
    2. Determine e exiba qual é o maior número.
    3. Determine e exiba qual é o menor número.
    4. Calcule e exiba a média dos dez números.
    5. Informe quantos dos números são pares.
    6. Informe quantos dos números são positivos.
    7. Calcule e exiba a variação (diferença) entre o maior e o menor número.
    8. Mostre a soma dos números que são maiores que a média.
    9. Informe quantos dos números são negativos.
    
Observações: O programa deve considerar que o usuário fornecerá apenas 
valores numéricos válidos. Em todas as operações, os resultados devem ser 
exibidos com até duas casas decimais, quando aplicável.

"""


numeros = []

for i in range(4):
    num = float(input(f"\ninforme 10 numeros {i + 1}: "))
    numeros.append(num)

maior_numero = max(numeros)

print(maior_numero)

media = sum(numeros) / len(numeros)

print(media)
par = []
impar = []

for j in numeros:

    if j % 2 == 0:

        par.append(j)
    else:
        impar.append(j)

print(par)
print(impar)

menor_numero = min(numeros)

diferenca = maior_numero - menor_numero
soma_maiores = 0
negativos = []
for k in numeros:
    if k > media:
        soma_maiores += k
    elif k < 0:
        negativos.append(k)


print(soma_maiores)
print(negativos)


