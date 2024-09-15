##caixa eletronico

saldo = 1000.00

menu_nav = 0

while menu_nav != 4:
    print("\nCaixa Eletrônico\n1- Verificar Saldo\n2- Depositar Dinheiro\n3- Sacar Dinheiro\n4- Sair")

    menu_nav = int(input("Escolha uma opção (1-4):"))

    if menu_nav == 1:
        print(f"\nSeu saldo é de: R${saldo:.2f}\n")
    elif menu_nav == 2:
        valor_deposito = (int(input("\nDigite o valor de seu deposito: ")))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"valor de R${valor_deposito:.2f} depositado!\n")
        else:
            print("Valor de deposito invalido!\n")

    elif menu_nav == 3:
        valor_saque = (int(input("\nDigite o valor de seu saque: ")))
        if valor_saque > 0 and valor_saque <= saldo:
            saldo -= valor_saque
            print(f"valor de R${valor_saque:.2f} sacado!\n")
        else:
            print("Valor do saque invalido!\n")
    else:
        print("\nOpção inválida! Tente novamente.")

print("\nObrigado por usar nossos serviços!\n")