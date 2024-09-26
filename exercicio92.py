"""

Exercício: Sistema de Gerenciamento de Estudantes

Descrição

Neste exercício, você irá criar uma aplicação simples para gerenciar informações 
sobre estudantes. O sistema deve ser capaz de adicionar novos estudantes, atualizar 
suas notas, visualizar informações de estudantes específicos e listar todos os estudantes.

Funcionalidades

    1. Adicionar um novo estudante.
    2. Atualizar a nota de um estudante existente.
    3. Visualizar informações de um estudante.
    4. Listar todos os estudantes.
    5. Sair do programa.

Detalhes da Implementação

    Utilize Programação Orientada a Objetos para estruturar seu código.
    Crie uma classe Estudante com atributos nome, idade e nota.
    Crie métodos getters e setters apropriados para cada atributo.
    Utilize um menu para interagir com o usuário e executar as diferentes funcionalidades.
"""

class Estudante:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
    
    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def set_idade(self, idade):
        self.idade = idade

    def get_idade(self):
        return self.idade
    
    def set_nota(self, nota):
        self.nota = nota
    
    def get_nota(self):
        return self.nota


def menu():

    estudantes = []

    while True:

        print("\n1. Adicionar Estudante")
        print("2. Atualizar Nota")
        print("3. Visualizar Estudante")
        print("4. Listar Estudantes")
        print("5. Sair")

        nav = input("Digite uma opcao: ")

        if nav == "1":
            nome = input("Digite o nome do estudante: ")
            idade = input("Digite a idade do estudante: ")
            nota = input("Digite a nota do estudante: ")

            novo_estudante = Estudante(nome, idade, nota)

            estudantes.append(novo_estudante)

        elif nav == "2":
            nome = input("Digite o nome do estudante para atualizar a nota: ")
            
            for estudante in estudantes:

                if estudante.get_nome() == nome:
                    nota = float(input("Digite a nova nota do estudante: "))

                    estudante.set_nota(nota)

                else:
                    print("Estudante nao esta na lista")

        elif nav == "3":
            nome = input("Digite o nome do estudante para vizaulizar: ")

            for estudante in estudantes:
                
                if estudante.get_nome() == nome:
                    print(f"O nome do estudante e {estudante.get_nome()}, Idade: {estudante.get_idade()} Nota: {estudante.get_nota()}")

                    break

                else:
                    print("Estudante nao encontrado")
                    
        elif nav == "4":

            for estudante in estudantes:
                    print(f"Nome: {estudante.get_nome()}, Idade: {estudante.get_idade()}, Nota: {estudante.get_nota()}")

        elif nav == "5":
            print("\nfechando...")
            break

        else:
            print("Opcao invalida")

if __name__ == "__main__":
    menu()
