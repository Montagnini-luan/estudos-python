"""
Exercício Desempenho de Alunos

Desenvolva um programa que avalie o desempenho de três alunos de uma 
turma. O programa deve considerar o seguinte:

    1. Solicite ao usuário o nome de cada aluno e suas quatro notas.

    2. Calcule a média de cada aluno e armazene-as em uma lista chamada "medias".

    3. Exiba quantos alunos obtiveram média maior ou igual a 7,0.

    4. Mostre os nomes dos alunos que obtiveram média superior ou igual a 7,0.

    5. Informe qual aluno obteve a maior média e qual foi essa média.

    6. Calcule e apresente a média geral da turma. Baseando-se nessa 
    média, classifique o desempenho da turma como:
        "Excelente", se a média for maior ou igual a 9;
        "Boa", se a média for maior ou igual a 7 e menor que 9;
        "Regular", se a média for maior ou igual a 5 e menor que 7;
        "Precisa melhorar", se a média for menor que 5.

"""

alunos = {}

for i in range(2):
    nome = input("Digite o nome do aluno: ")
    
    notas = [float(input(f"Digite a nota {j+1} de {nome}: ")) for j in range(4)]

    alunos[nome] = notas

print(alunos)

medias = {}

for nome, notas in alunos.items():

    media = sum(notas) / 2
    medias[nome] = media

aprovados = 0

for media in medias.values():
    
    if media >= 7:
        
        aprovados += 1

print(f"{aprovados} alunos obtiveram média maior ou igual a 7.0")

alunos_aprovados = []

for nome, media in medias.items():

    if media >= 7:
        alunos_aprovados.append(nome)

print(f"Os alunos aprovados sao {alunos_aprovados}")

melhor_aluno = max(medias, key=medias.get)
print(f"O aluno com a maior média é {melhor_aluno} com a média {medias[melhor_aluno]:.2f}")

media_geral = sum(medias.values()) / len(medias)

print(f"A média geral da turma é: {media_geral:.2f}")

if media_geral >= 9:
    
    print("A turma foi classificada como Excelente!")
    
elif media_geral >= 7:
    
    print("A turma foi classificada como Boa!")
    
elif media_geral >= 5:
    
    print("A turma foi classificada como Regular!")
    

else:
    print("A turma Precisa Melhorar!")
