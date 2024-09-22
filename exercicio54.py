"""
Exercício Análise de Desempenho do Aluno

Objetivo: Desenvolver um programa que avalie o desempenho de um aluno ao
longo dos bimestres. Para isso, o programa deve solicitar as quatro
notas bimestrais do aluno e, com base nelas, realizar as seguintes ações:

    1. Calcular e exibir a média das notas.
    2. Determinar e mostrar a maior e a menor nota entre as inseridas.
    3. Com base na média, informar ao usuário se o aluno está aprovado, 
    em recuperação ou reprovado. Considere os seguintes critérios:
        - Aprovado: média >= 7
        - Em recuperação: 5 <= média < 7
        - Reprovado: média < 5
        
    4. Calcular e mostrar a quantidade de notas que estão acima da média calculada.

"""
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
nota4 = float(input("Digite a quarta nota do aluno: "))

medias = (nota1 + nota2 + nota3 + nota4) / 4
print(f"\nA media de notas e {medias}")

maior_nota = max(nota1, nota2, nota3, nota4)
menor_nota = min(nota1, nota2, nota3, nota4)

print(f"A maior nota e: {maior_nota}")
print(f"A menor nota e: {menor_nota}")

aprovado = "aprovado" if medias >= 7 else "Em recuperação" if 5 <= medias < 7 else "reprovado"
print(aprovado)

contador = 0

for nota in (nota1, nota2, nota3, nota4):

    if nota > medias:

        contador += 1

    print(nota)
    
print(f"quantidade de notas acima da media {contador}")


