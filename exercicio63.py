"""
Exercício: Consulta de Dias da Semana

Objetivo: Desenvolver um programa que permita ao usuário identificar o nome 
do dia da semana a partir de um número ou vice-versa, e forneça opções de repetição de consultas.

Instruções:

    1. Ao iniciar, o programa deve exibir um menu com duas opções:
        1 - Digite o número (de 1 a 7) para saber o dia da semana correspondente.
        2 - Digite o nome do dia para descobrir o número correspondente.

    2. Baseado na escolha do usuário:
    
        - Se o usuário optar pela primeira opção e inserir um número, o programa deverá 
        
        - exibir o nome do dia da semana correspondente.
            Por exemplo, se o usuário inserir "1", o programa deve retornar "Domingo".
        
        - Se o usuário optar pela segunda opção e inserir o nome de um dia, o programa 
        deve retornar o número correspondente.
            Por exemplo, se o usuário inserir "segunda", o programa deve retornar "2".

    3. Caso o usuário insira um valor que não corresponda a um dia da semana válido (por exemplo, 
    número 8 ou "octaday"), o programa deve exibir uma mensagem de erro: "Valor inválido".

    4. Após cada consulta, pergunte ao usuário se ele deseja realizar outra consulta ou encerrar o programa

"""

dias_semana = {
    "domingo": 1,
    "segunda": 2,
    "terca": 3,
    "quarta": 4,
    "quinta": 5,
    "sexta": 6,
    "sabado": 7
}

while True:

    print("1- Digite o número (de 1 a 7) para saber o dia da semana correspondente.")
    print("2- Digite o nome do dia para descobrir o número correspondente.")
    opcao = int(input())

    if opcao == 1:
        num = int(input("Escolha um numero ente 1 a 7: "))

        if num > 0 and num < 8:
            for dia, numeros in dias_semana.items():
                if numeros == num:
                    print(dia)
        else:
            print("Numero invalido, digite um numero de 1 a 7")

    elif opcao == 2:
        dia_digitado = input("Digite o nome do dia para descobrir o número correspondente: ")
        for _ in range(1):
            encontrado = False
            for dia, numeros in dias_semana.items():
                if dia == dia_digitado.lower():
                    print(numeros)
                    encontrado = True

        if encontrado == False:
            print("Nome invalido, digite um numero da semana valido!")
    saida = input("Voce deseja continuar a pesquisa (sim / nao)? ")

    if saida.lower() != "sim":
        break