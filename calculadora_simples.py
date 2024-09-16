
while True:

    print("\nCalculadora Simples")
    print("1 - Adição")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - sair")

    escolha = int(input("\nEscolha sua operação: "))

    if escolha == 5:
        print("\nAté mais!")
        break

    num1 = float(input("\nEscolha seu primeiro número: "))
    num2 = float(input("\nEscolha seu segundo número: "))

    if escolha == 1:

        print("\nO resultado da sua adição é ", num1 + num2)

    elif escolha == 2:

        print("\nO resultado da sua subtração é ", num1 - num2)

    elif escolha == 3:

        print("\nO resultado da sua multiplicação é ", num1 * num2)

    elif escolha == 4:

        if num2 != 0:

            print("\nO resultado da sua divisão é ", num1 / num2) 

        else:

            print("Erro: Divisão por zero.")
    else:
        
        print("opção invalida!")