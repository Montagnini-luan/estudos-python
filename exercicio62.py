"""
Exercício: Análise e Ordenação de Números

Objetivo: Desenvolver um programa que obtenha do usuário cinco números, 
mostre-os em ordem decrescente e forneça algumas análises adicionais.

Instruções:

    1. Solicite ao usuário que digite cinco números.
    
    2. Mostre os cinco números em ordem decrescente.
    
    3. Informe ao usuário qual é o maior e o menor 
        número dentre os fornecidos.
        
    4. Calcule e exiba a média dos números fornecidos.
    
    5. Verifique e informe ao usuário se algum dos números 
        fornecidos é divisível por 3 ou 5.
        
    6. Pergunte ao usuário se ele deseja inserir um novo conjunto
        de números ou encerrar o programa.

Observações: O programa deve considerar que o usuário fornecerá apenas valores 
numéricos válidos para os números.
"""

numeros = []

while True:
    
    for _ in range(1, 6):
        num = float(input("Digite 5 numeros: "))
        numeros.append(num)

    ordem = sorted(numeros, reverse=True)

    print(f"Numeros em ordem decrescente: {ordem}")

    maior = max(numeros)
    print(f"O maior numero fornecido e: {maior}")
    menor = min(numeros)
    print(f"O menor numero fornecido e: {menor}")

    media = sum(numeros) / len(numeros)
    print(f"A media dos numeros fornecidos e: {media}")

    divisiveis_3 = []
    divisiveis_5 = []

    for i in numeros:

        if i % 3 == 0:
            divisiveis_3.append(i)

        elif i % 5 == 0:
            divisiveis_5.append(i)
    
    print(f"Os numeros {divisiveis_3} sao divisiveis por 3")

    print(f"Os numeros {divisiveis_5} sao divisiveis por 5")

    escolha = input("Voce deseja inserir mais numeros? (Sim / Nao) ")

    if escolha.lower() != "sim":
        print("\nObrigado por usar o programa!")
        break