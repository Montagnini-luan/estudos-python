"""
Exercício: Determinando a Natureza de um Número

Objetivo: Desenvolva um programa que solicite ao usuário a 
entrada de um número. O programa deverá identificar se o número 
é inteiro ou decimal, informando ao usuário sua descoberta.

Instruções:

    1. Solicite ao usuário que insira um número. Este número pode 
    ser tanto um valor inteiro quanto um valor decimal.
    
    2. Utilize uma função de arredondamento para ajudar a determinar a natureza do número.
        - Se o número inserido for igual ao seu valor arredondado, classifique-o como inteiro.
        - Caso contrário, classifique-o como decimal.
    
    3. Exiba uma mensagem informando ao usuário se o número é inteiro ou decimal.
    
    4. No caso de uma entrada inválida (por exemplo, texto que não seja 
    convertido para um número), exiba uma mensagem de erro solicitando que 
    o usuário insira uma entrada válida.
    
    5. Após processar a entrada, pergunte ao usuário se ele deseja inserir e 
    verificar outro número. Se a resposta não for "sim", encerre o programa.
"""
while True:

    try:

        num = float(input("Insira um numero: "))

        determinacao = round(num)

        if num == determinacao:
            print("Seu numero e inteiro!")
            
        else:
            print("Seu numero e decimal")

        opcao = input("Deseja inserir um novo numero (sim/nao)?: ")

        if opcao.lower() != "sim":
            print("Obrigado por usar o programa")

            break

    except ValueError:
        print("Por favor, digite um número válido.")