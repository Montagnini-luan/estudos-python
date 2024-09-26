"""
Exercício Pet

Instruções do Exercício

    1. Crie uma classe chamada Pet.
    2. A classe deve ter os seguintes atributos privados: _nome, _idade e _peso.
        - Utilize métodos "getters" para cada um desses atributos.
        - Utilize métodos "setters" para cada um desses atributos. 
        
        Os "setters" devem conter as seguintes validações:
            - O nome deve ser uma string e não pode ser vazio.
            - A idade deve ser um número inteiro e deve ser maior ou igual a 0.
            - O peso deve ser um número flutuante e deve ser maior que 0.
    
    3. Adicione um método exibir_info() que mostre as informações do pet.
    
    
# Teste sua implementação
meu_pet = Pet()
meu_pet.set_nome("Buddy")
meu_pet.set_idade(5)
meu_pet.set_peso(9.5)
meu_pet.exibir_info()

Sua tarefa é completar a classe Pet seguindo as instruções. 
Certifique-se de utilizar "getters" e "setters" para controlar o acesso aos 
atributos da classe.
"""


class Pet:

    def __init__(self):

        self._nome = ""
        self._idade = 0
        self._peso = 0.0

    def set_nome(self, novo_nome):

        if isinstance(novo_nome, str) and novo_nome != "":

            self._nome = novo_nome
        
        else:

            print("Nome invalido")

    def set_idade(self, novo_idade):

        if isinstance(novo_idade, int) and novo_idade > 0:

            self._idade = novo_idade

        else:

            print("idade invalida")

    def set_peso(self, novo_peso):

        if isinstance(novo_peso, float) and novo_peso > 0:
            
            self._peso = novo_peso

        else:

            print("Peso invalido")

    def get_nome(self):

        return self._nome
    
    def get_idade(self):

        return self._idade
    
    def get_peso(self):

        return self._peso
    
    def exibir_info(self):

        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade} anos")
        print(f"Pesdo: {self._peso} kg")

"""
Exercício Pet


No mesmo exercício anterior, adicione um menu interativo com as seguintes informações:

    1. Definir o nome do pet
    2. Definir a idade do pet
    3. Definir o peso do pet
    4. Exibir informações do pet
    5. Sair

"""

def mostrar_menu():
    
    print("\n---- Menu de Gerenciamento de Pet ----")
    print("1. Definir o nome do pet")
    print("2. Definir a idade do pet")
    print("3. Definir o peso do pet")
    print("4. Exibir informações do pet")
    print("5. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    return escolha


def main():

    meu_pet = Pet()

    while True:

        escolha = mostrar_menu()

        if escolha == "1":
            nome = input("Escolha o nome: ")
            meu_pet.set_nome(nome)

        elif escolha == "2":

            try:
                idade = int(input("Digite a idade: "))
                meu_pet.set_idade(idade)

            except ValueError:
                print("A idade deve ser um numro inteiro")

        elif escolha == "3":

            try:
                peso = float(input("Digite o peso: "))
                meu_pet.set_peso(peso)

            except ValueError:
                print("O peso deve ser um numero")

        elif escolha == "4":
            meu_pet.exibir_info()

        elif escolha == "5":
            print("Obrigador por usar o programa!")
            break

        else:
            print("Deve ser informado um valor valido!")

if __name__ == "__main__":
    main()
