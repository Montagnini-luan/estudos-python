"""
Exercício: Urna Eletrônica com Matrizes

Imagine que estamos conduzindo uma eleição para escolher o representante 
estudantil de uma universidade. Existem três candidatos concorrendo e, para 
simplificar, cada aluno pode votar apenas uma vez.

Seu objetivo é criar um programa que simule uma urna eletrônica 
simples usando matrizes.

Especificações:

    - A matriz terá 2 colunas: a primeira para armazenar o nome do 
    candidato e a segunda para armazenar a quantidade de votos.
    
    - O usuário deve inserir o nome do candidato em quem deseja votar. 
    Se o voto for para um candidato não listado, ele será considerado nulo.
    
    - Depois que todos os votos forem inseridos, o programa deve imprimir 
    o nome de cada candidato, o número total de votos que receberam e o vencedor da eleição.

Dica: Para simplificar, considere que o número total de eleitores é fixo, digamos 10.
"""

urna = [
    ["Nadinho", 0],
    ["Bobson", 0],
    ["Luanzito", 0]
    ]

voto_matriz = []

for i in range(4):

    voto = input("Digite o nome do candidato em que deseja votar (Nadinho, Bobson, Luanzito): ")

    encontrado = False

    for candidato in urna:

        if candidato[0] == voto:
                    
                candidato[1] += 1
                    
                encontrado = True
                break

    if not encontrado:
        print("Voto nulo.")

print("\nResultado:")

votos_maximos = -1
vencedor = ""

for candidato in urna:
     
    print(f"{candidato[0]}: {candidato[1]}")
    
    if candidato[1] > votos_maximos:
         
        votos_maximos = candidato[1]

        vencedor = candidato[0]

print(f"O candidato vencedor {vencedor} com {votos_maximos} votos!")




