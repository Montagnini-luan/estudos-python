"""
Exercício Manipulador de Listas em Python

Objetivo:

Neste exercício, você criará uma aplicação Python que ajuda os usuários a 
manipular listas de números inteiros. A aplicação deve oferecer opções para 
adicionar elementos, remover elementos, encontrar o maior e o menor elemento, 
calcular a média dos elementos e mais.

Requisitos:

    1. Crie uma classe chamada ManipuladorDeLista que será responsável por todas as 
    operações de manipulação de lista.
    
        - adicionar_elemento(elemento): adiciona um elemento no final da lista.
        - remover_elemento(elemento): remove a primeira ocorrência do elemento na lista.
        - encontrar_maior(): encontra e retorna o maior elemento da lista.
        - encontrar_menor(): encontra e retorna o menor elemento da lista.
        - calcular_media(): calcula e retorna a média dos elementos na lista.
        - mostrar_lista(): retorna a lista atual.

    2. Implemente uma função menu() que serve como interface do usuário. Essa 
    função deve mostrar um menu com as opções de manipulação e realizar a operação 
    escolhida pelo usuário.

    3. O programa deve continuar rodando e mostrando o menu até que o usuário escolha sair.

"""

class MinupuladorDeListas:

    def __init__(self):
        self.lista = []
        

    def adiconar_elemento(self, elemento):
        self.lista.append(elemento)

    def remover_elemento(self, elemento):

        try:
            self.lista.remove(elemento)
            print(f"Numero {elemento} removido com sucesso")
        
        except ValueError:
            print("Numero nao esta na lista")

    def maior_elemento(self):
        print(f"O maior numero e: {max(self.lista)}")

    def menor_elemento(self):
        print(f"O menor numero e: {min(self.lista)}")

    def media_lista(self):
        media = sum(self.lista) / len(self.lista)
        print("A media dos numeors digitados e: ", media)

    def mostrar_lista(self):
        print(self.lista)

def menu():

    manipulacao = MinupuladorDeListas()

    while True:

        print("\nEscolha uma opção:")
        print("1. Adicionar elemento")
        print("2. Remover elemento")
        print("3. Encontrar maior elemento")
        print("4. Encontrar menor elemento")
        print("5. Calcular média")
        print("6. Mostrar lista")
        print("7. Sair")

        nav = input("\nDigite o número da sua escolha: ")
            
        if nav == "1":
            try:
                elemento = int(input("Digite o numro que voce deseja adicionar: "))

                manipulacao.adiconar_elemento(elemento)
                    
            except ValueError:
                print("Por favor, digite um numero valido!")

        elif nav == "2":
            elemento = int(input("Digite o numro que voce deseja remover: "))

            manipulacao.remover_elemento(elemento)

        elif nav == "3":
            manipulacao.maior_elemento()

        elif nav =="4":
            manipulacao.menor_elemento()

        elif nav =="5":
            manipulacao.media_lista()

        elif nav == "6":
            manipulacao.mostrar_lista()

        elif nav == "7":
            break

        else:
            print("Escolha invalida, tente novamente!")

if __name__ == "__main__":
    menu()