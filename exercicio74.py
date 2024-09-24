"""
Exercício: Embaralhador de Palavra

Desenvolva um programa que cumpra as seguintes especificações:

Solicite ao usuário que digite uma palavra e imprima essa paralavra 
embaralhada e só pare quando o usuário digitar sair.
"""

import random

while True:

    palavra = input("Digite uma palavra (ou 'sair' para sair): ")

    if palavra.lower() == "sair":
        break

    separacao = list(palavra)

    print(separacao)

    random.shuffle(separacao)

    print(f"Palavra embaralhada: {"".join(separacao)}")