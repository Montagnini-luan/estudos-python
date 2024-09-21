"""
Exercício: Reserva de Assentos no Cinema usando Matrizes

Você foi contratado para criar um sistema simples de reserva de 
assentos para um pequeno cinema. O cinema tem 5 fileiras e 10 assentos 
em cada fileira, totalizando 50 assentos.

Cada assento pode estar disponível, reservado ou ocupado.

Especificações:

    Inicie com todos os assentos disponíveis.
    - O usuário pode escolher entre ver a disposição dos assentos, 
    reservar um assento ou sair.
    
    - A disposição dos assentos deve mostrar "D" para assentos 
    disponíveis, "R" para assentos reservados e "O" para assentos ocupados.
    
    - Para reservar um assento, o usuário deve inserir a fileira e o número do assento.
    
    - Uma vez que um assento é reservado, ele não pode ser selecionado por outro usuário.

Dica: Use uma matriz 5x10 para representar o cinema, onde cada elemento é uma 
string que indica o status do assento.
"""

cinema = []

##Gerar matriz de acentos disponiveis
for i in range(5):

    fileira = []

    for j in range(10):

        fileira.append("D")

    cinema.append(fileira)

##Menu de navegacao
while True:

    print("Menu:")
    print("1- Ver disposicao de assentos")
    print("2- Reservar um assento")
    print("3- Sair")

    menu_nav = int(input())

    if menu_nav == 1:

        for fileira in cinema:

            for assento in fileira:
                
                print(assento, end=" ")

            print()

    elif menu_nav == 2:

        fileira = int(input("Escolha a fileira(0-9): "))
        assento = int(input("Escolha a coluna(0-9): "))

        if cinema[fileira][assento] == "D":

            cinema[fileira][assento] = "R"
            print("Assento reservado com sucesso!")

        else:

            print("Assento ja reservado!")    

    elif menu_nav == 3:
        print("Obrigado por usar nosso sistema!")
        break
    
    else:
        print("opcao invalida!")