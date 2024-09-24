"""
Calculadora de Duração

Desenvolva um programa que converta uma quantidade de minutos fornecida 
pelo usuário em horas, dias, semanas e anos.

Instruções:

    Solicite ao usuário a entrada de um valor inteiro em minutos, com um 
    limite de até 5 milhões de minutos.

    O programa deve converter esse valor em:
        - Minutos
        - Horas
        - Dias
        - Semanas
        - Anos

    Exibir a duração em cada uma das unidades de tempo. Por exemplo, se o usuário 
    inserir 1500 minutos, o programa deve exibir: "1500 minutos é igual a 25 horas 
    ou 1,04 dias ou 0,15 semanas ou 0,0028 anos."

    O programa deve ser capaz de lidar com valores que não são números inteiros, 
    informando ao usuário sobre entradas inválidas.

    
    Para simplificar, considere:
        1 dia = 24 horas
        1 semana = 7 dias
        1 ano = 365,25 dias (levando em conta anos bissextos)

"""


while True:

    try:

        minutos = int(input("Digite a quantidade de minutos (0 a 5.000.000): "))

        hora = minutos / 60
        dia = hora / 24
        semana = dia / 7
        ano = dia / 365.25

        print(f"{minutos} minutos é igual a {hora:.2f} horas ou {dia:.2f} dias ou {semana:.2f} semanas ou {ano:.5f} anos.")

        opcao = input("Desja pesquisar outro numero? (sim/nao): ")

        if opcao.lower() != "sim":
            print("Obrigado por usar nosso programa!")
            break

    except ValueError:
        print("Valor invalido!")
