"""
Exercício: Embaralhador de Palavra Avançado

Desenvolva um programa que cumpra as seguintes especificações:

    1. Solicite ao usuário uma string (palavra ou frase).

    2. Pergunte ao usuário como ele deseja ver o resultado:
        a) Em caixa alta.
        b) Em caixa baixa.
        c) Mantendo a formatação original.

    3. Pergunte ao usuário se ele deseja embaralhar:
        a) Apenas as letras da string (mantendo espaços, números e 
            outros caracteres em suas posições originais).
        b) A string inteira (incluindo espaços, números e outros caracteres).

    4. Crie uma função chamada embaralhar_string que aceite a string do usuário, 
        a escolha de formatação e a opção de embaralhamento.

    5. A função deve retornar a string embaralhada conforme as opções escolhidas.

    Exiba o resultado para o usuário.
"""

import random

palavra = input("Digite uma palavra ou frase: ")

print("Como voce deseja ver o resultado?")
print("a) Em caixa alta.")
print("b) Em caixa baixa.")
print("c) Mantendo a formatação original.")

opcao = input()

if opcao.lower() == "a":
    palavra = palavra.upper()

elif opcao.lower() == "b":
    palavra = palavra.lower()

print("Como voce deseja embaralhar?")
print("a) Apenas as letras da string (mantendo espaços, números e outros caracteres em suas posições originais).")
print("b) A string inteira (incluindo espaços, números e outros caracteres).")

palavras = list(palavra)
opcao2 = input()

if opcao2.lower() == "a":

    letras = []

    for letra in palavras:

        if letra.isalpha():

            letras.append(letra)

    random.shuffle(letras)

    indice_letras = 0

    for i in range(len(palavras)):
            
        if palavras[i].isalpha():
                    
            palavras[i] = letras[indice_letras]
                    
            indice_letras += 1

    print(f"frase embaralhada e: {"".join(palavras)}")

else:

    random.shuffle(palavras)
    
    print(f"palavra embaralhada e: {"".join(palavras)}")