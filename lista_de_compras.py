"""
Exercício: Lista de Compras

Crie um programa em Python que permita ao usuário adicionar 
itens a uma lista de compras. O programa deve exibir um menu com as seguintes opções:

    1. Adicionar item à lista
    2. Remover item da lista
    3. Exibir lista de compras
    4. Sair

O programa deve continuar executando até que o usuário escolha a opção 4 para sair.

"""

listaDeCompras = []

while True:

    print("\nMenu")
    print("1. Adicionar item à lista")
    print("2. Remover item da lista")
    print("3. Exibir lista de compras")
    print("4. Sair")
    
    opicao = int(input("\nDigite a uma opção: "))

    if opicao == 1:

        itemAdicao = input("Digite o item que voce quer adicionar: ")
        print(f"\nItem {itemAdicao} adicionado a lista!")
        listaDeCompras.append(itemAdicao)

    elif opicao == 2:

        if len(listaDeCompras) == 0:

            print("Lista de compras está vazia")
        
        else:
            itemRemover = input("Digite o item que voce quer remover: ")

            if itemRemover in listaDeCompras:
                listaDeCompras.remove(itemRemover)
                print(f"\nItem {itemRemover} removido da lista!")
            else:
                print("item não esta na lista")

    elif opicao == 3:
        print("Lista de compras")
        
        for item in listaDeCompras:
            print('- ', item)

    elif opicao == 4:
        break

    else:
        print("\nopção invalida")
