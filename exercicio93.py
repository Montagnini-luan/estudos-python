"""
Exercício Agenda de Contatos - Programação Orientada a Objetos

Objetivo:

O objetivo deste exercício é criar uma aplicação de gerenciamento de 
agenda de contatos usando Programação Orientada a Objetos (POO) em Python.

Descrição:

Você deve criar uma classe chamada Contato que irá representar um contato 
individual na agenda. Cada contato deve ter três atributos: nome, telefone e email.

Além disso, você deve criar uma classe chamada Agenda que irá gerenciar os 
contatos. Esta classe deve conter métodos para adicionar, remover, listar e buscar contatos.

A aplicação deve também possuir um menu interativo para o usuário, permitindo 
que ele execute as seguintes ações:

    1. Adicionar um novo contato.
    2. Remover um contato existente.
    3. Listar todos os contatos na agenda.
    4. Buscar um contato pelo nome.
    5. Sair da aplicação.

Instruções:

    1. Comece definindo a classe Contato com os atributos e métodos necessários.
    2. Em seguida, defina a classe Agenda que contém uma lista de objetos da classe Contato.
    3. Implemente os métodos de Agenda para adicionar, remover, listar e buscar contatos.
    4. Crie uma função menu para gerenciar a interação com o usuário.
    5. No método main (ponto de entrada do programa), instancie um objeto da classe 
       Agenda e comece o loop do menu para o usuário.
"""


class Contato:

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
 

class Agenda:

    def __init__(self):
        self.contatos = []

    def acionar_contato(self, contato):
        self.contatos.append(contato)
    
    def listar_contato(self):
        return self.contatos
    
    def remover_contato(self, nome):

        for contato in self.contatos:

            if contato.nome == nome:
                
                self.contatos.remove(contato)

                return True

        return False

    def buscar_contato(self, nome):

        for contato in self.contatos:

            if contato.nome == nome:

                return contato
        return None

def menu():

    agenda = Agenda()

    while True:

        print("\n1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Listar Contatos")
        print("4. Buscar Contato")
        print("5. Sair")

        nav = input("Escolha uma opcao: ")

        if nav == "1":

            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")

            novo_contato = Contato(nome, telefone, email)

            agenda.acionar_contato(novo_contato)

            print(f"O contato {nome} foi adicionado com sucesso!")
            
        elif nav == "2":

            nome = input("Digite o nome do contato que deseja remover: ")

            if agenda.remover_contato(nome):

                print("Contato removido")

            else:

                print("Contato nao encontrado")

        elif nav == "3":

            for contato in agenda.listar_contato():

                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
            
        elif nav == "4":

            nome = input("Digite o nome do contato que deseja buscar: ")

            contato = agenda.buscar_contato(nome)

            if contato:
                    
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
                
            else:
                print("Contato não encontrado.")

        elif nav == "5":

            print("Saindo...")

            break

        else:
            print("opcao invalida!")

if __name__ == "__main__":
    menu()