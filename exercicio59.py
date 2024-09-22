"""
Exercício: Análise de Caracteres e Formação de Palavras

Objetivo: Desenvolver um programa que obtenha do usuário uma letra ou uma palavra 
e realize análises sobre o tipo de caractere inserido, além de funções adicionais 
se uma palavra completa for fornecida.

Instruções:

    1. Solicite ao usuário que digite uma letra ou uma palavra.
    
    2. Se o usuário digitar apenas um caractere:
    
        a. Verifique se é uma vogal ou consoante.
        b. Se for uma vogal, exiba: "Você digitou uma vogal."
        c. Se for uma consoante, exiba: "Você digitou uma consoante."
        d. Se o caractere não for uma letra, exiba: "Caractere inválido."
    
    3. Se o usuário digitar mais de um caractere (uma palavra):
        
        a. Calcule e exiba o número de vogais na palavra.
        b. Calcule e exiba o número de consoantes na palavra.
        c. Exiba a palavra em ordem inversa.
        d. Informe se a palavra é um palíndromo (se lê da mesma forma de frente para trás 
        e de trás 
        para frente, como "arara").
    
    4. Peça ao usuário se deseja verificar outra letra ou palavra ou sair do programa.

Observações: O programa deve considerar letras maiúsculas e 
minúsculas (ou seja, "A" e "a" são ambas vogais).
"""


vogais = ['a', 'e', 'i', 'o', 'u']


while True:
    digitado = input("Digite uma palavra ou letra: ")
    frase = digitado.lower()

    if len(frase) == 1:
        if frase.isalpha():
            if frase in vogais:
                print("Você digitou uma vogal!")
            else:
                print("Você digitou uma consoante!")
        else:
            print("Caractere inválido. Digite apenas uma letra.")
    elif len(frase) > 1:

        num_vogais = 0
        num_consoantes = 0
        consoantes = []

        for frase in frase:
            if frase in vogais:
                num_vogais += 1
            if frase not in vogais:
                num_consoantes += 1
                consoantes.append(frase)
          
        print(f"A palavra tem {num_vogais} vogais")
        print(f"A palavra tem {num_consoantes} consoantes")
        print(f"As consoantes sao: {consoantes}")
        print(f"A palavra inversa e: {digitado.lower()[::-1]}")

        if frase == frase[::-1]:
            print(f"A palavra {digitado} é um palíndromo.")
        else:
            print(f"A palavra {digitado} não é um palíndromo.")

    continuar = input("Deseja verificar outra letra ou palavra? (sim/não) ")

    if continuar.lower() == "nao":
        print("Obrigado por usar o programa!")
        break

    


