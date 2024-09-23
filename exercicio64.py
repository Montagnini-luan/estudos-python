"""
Exercício: Decomposição de Números com Formatação Apropriada

Objetivo: Desenvolver um programa que obtenha do usuário um número inteiro 
menor que 10.000, decomponha esse número em milhares, centenas, dezenas e 
unidades, e apresente os resultados com uma formatação apropriada em 
relação ao plural e à pontuação.

Instruções:

    1. Solicitar um número ao usuário.
    
    2. Se o número estiver fora do intervalo permitido ou não for 
    um valor numérico, perguntar se o usuário deseja tentar novamente.
    
    3. Se o número for válido, decompor o número e exibir o resultado. 
    Após exibir o resultado, perguntar ao usuário se ele deseja decompor outro número.

Observações: Para este exercício, pode-se assumir que o usuário fornecerá valores numéricos 
válidos. A estrutura da mensagem será adaptada de acordo com o valor fornecido. Por exemplo:

    4321 = 4 milhares, 3 centenas, 2 dezenas e 1 unidade
    326 = 3 centenas, 2 dezenas e 6 unidades
    305 = 3 centenas e 5 unidades
    7 = 7 unidades
"""

def decomposicao_milhares(numero_dividido):

    numero_dividido[0] = numero_dividido[0] + " milhares,"
    numero_dividido[1] = numero_dividido[1] + " centenas,"
    numero_dividido[2] = numero_dividido[2] + " dezenas,"
    numero_dividido[3] = numero_dividido[3] + " e unidades"

    print(numero_dividido)

def decomposicao_centenas(numero_dividido):

    numero_dividido[0] = numero_dividido[0] + " centenas,"
    numero_dividido[1] = numero_dividido[1] + " dezenas,"
    numero_dividido[2] = numero_dividido[2] + " e unidades"

    print(numero_dividido)

def decomposicao_dezenas(numero_dividido):

    numero_dividido[0] = numero_dividido[0] + " dezenas,"
    numero_dividido[1] = numero_dividido[1] + " e unidades"

    print(numero_dividido)

def decomposicao_unidades(numero_dividido):

    numero_dividido[0] = numero_dividido[0] + " unidades"

    print(numero_dividido)


while True:

    num = input("Digite um numero: ")
    numero_dividido = list(num)

    if num.isalpha() == False:

        if len(numero_dividido) <= 4:

            if len(numero_dividido) == 4:
                decomposicao_milhares(numero_dividido)

            elif len(numero_dividido) == 3:
                decomposicao_centenas(numero_dividido)

            elif len(numero_dividido) == 2:
                decomposicao_dezenas(numero_dividido)
            
            elif len(numero_dividido) == 1:
                decomposicao_unidades(numero_dividido)
        else:
            opcao = input("Numero fora do intervalo permitido, deseja digitar novamente (sim / nao)? ")

            if opcao.lower() == "nao":
                print("Obrigado por usar o programa!")
                break
            
    else:
        opcao1 = input("Apenas numeros sao validos! deseja tentar novamente (sim / nao)? ")

        if opcao1.lower() == "nao":
            print("Obrigado por usar o programa!")
            break

    opcao2 = input("Deseja digitar mais um numero? ")

    if opcao2.lower() == "nao":
        print("Obrigado por usar o programa!")
        break