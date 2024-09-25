"""
Exercício: Unir Duas Listas com Opções de Personalização

O objetivo deste exercício é criar um programa Python que percorre 
duas listas fornecidas pelo usuário e gera uma terceira lista sem elementos repetidos. 

O programa deve ter as seguintes funcionalidades:

Requisitos:

    1. Tipo de Dado: O programa deve começar perguntando ao usuário qual o 
        tipo de dado que ele deseja usar nas 
        listas (números inteiros, números de ponto flutuante ou strings).

    2. Criação das Listas: O programa deve então permitir que o usuário 
        insira elementos para duas listas diferentes, de acordo com o tipo 
        de dado escolhido.

    3. Remoção de Duplicatas: O programa deve perguntar ao usuário se ele 
        deseja remover elementos duplicados dentro de cada lista individualmente 
        antes de unir as duas.

    4. União das Listas: O programa deve unir as duas listas em uma 
        terceira lista, removendo qualquer duplicata.

    5. Ordenação: A terceira lista deve ser apresentada em ordem crescente.

    6. Exibição: Finalmente, o programa deve exibir a terceira lista gerada.

"""

def tipo_criar_listada(dado):

    lista = []

    n = int(input("Quantos elementos você deseja adicionar à lista? "))

    for _ in range(n):

        if dado == "1":
            dado_ = int(input("Digite int: "))

        if dado == "2":
            dado_ = float(input("Digite float: "))
        
        if dado == "3":
            dado_ = str(input("Digite string: "))
        
        lista.append(dado_)

    return lista

def unir_lista(lista1, lista2, remover_duplicados):
    
    lista_unida = []

    if remover_duplicados == "s":

        lista1 = list(set(lista1))
        lista2 = list(set(lista2))

    lista_unida = lista1[:]

    if remover_duplicados == "s":

        for x in lista2:

            if x not in lista1:
                lista_unida.append(x)

    else:

        if x in lista2:
            lista_unida.append(x)

    return sorted(lista_unida)    


def main():

    print("Escolha o tipo de dado para as listas:")
    print("1 - Inteiros")
    print("2 - Ponto flutuante")
    print("3 - Strings")

    dado = input("escolha uma opcao: ")

    lista1 = tipo_criar_listada(dado)
    lista2 = tipo_criar_listada(dado)

    remover_duplicados = input("Deseja remover itens duplicados (s/n): ")

    lista_final = unir_lista(lista1, lista2, remover_duplicados)

    print("A lista unida e:", lista_final)

main()