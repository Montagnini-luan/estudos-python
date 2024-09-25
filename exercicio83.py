"""
Exercício: Formatador de Frases em Python

Objetivo:

Neste exercício, você será desafiado a criar uma aplicação Python 
que ajuda os usuários a formatar frases de diversas maneiras. A aplicação 
deve oferecer opções para converter toda a frase para maiúsculas ou minúsculas, 
capitalizar a primeira letra, transformá-la em um título, contar 
vogais e consoantes, e mais.

Requisitos:

    Crie uma classe chamada FormatadorDeFrase que será responsável por 
    todas as operações de formatação.

    1. A classe deve possuir os seguintes métodos:
    
        para_maiusculas(): converte toda a frase para maiúsculas.
        para_minusculas(): converte toda a frase para minúsculas.
        capitalizar(): capitaliza a primeira letra da frase.
        formato_titulo(): converte a primeira letra de cada palavra da frase para maiúscula.
        contar_vogais(): conta e retorna o número de vogais na frase.
        contar_consoantes(): conta e retorna o número de consoantes na frase.
        contar_letra_a(): conta e retorna o número de ocorrências da letra 'a' na frase.
        procurar_palavra(palavra): conta e retorna o número de ocorrências de uma palavra específica na frase.
        obter_frase(): retorna a frase atual.

    2. Implemente uma função menu que serve como interface do usuário. Essa 
    função deve mostrar um menu com as opções de formatação e realizar a 
    operação escolhida pelo usuário.

    3. O programa deve continuar rodando e mostrando o menu até que o usuário escolha sair.

Detalhes:

    O programa deve ser case-insensitive para contagem e pesquisa de palavras.
    Você pode assumir que o usuário entrará apenas com caracteres alfabéticos e espaços.

"""

class FormatadorDeFrase:

    def __init__(self, frase):
        self.frase = frase

    def para_maiusculas(self):

        self.frase = self.frase.upper()
        print(self.frase)

    def para_minusculas(self):

        self.frase = self.frase.lower()
        print(self.frase)

    def capitalizar(self):

        self.frase = self.frase.capitalize()
        print(self.frase)

    def formato_titulo(self):

        self.frase = self.frase.title()
        print(self.frase)

    def contar_vogais(self):
        contador = 0

        for letra in self.frase:

            if letra.lower() in "aeiou":
                contador += 1

        print(f"A frase tem {contador} vogais")

    def contar_consoantes(self):
        contador = 0

        for letra in self.frase:

            if letra.lower() not in "aeiou ":
                contador += 1
            
        print(f"A frase tem {contador} consoantes")

    def contar_letra_a(self):
        contador = 0

        for letra in self.frase:

            if letra.lower() in "a":
                contador += 1

        print(f"A letra 'a' aparecer {contador} vezes na frase!")

    def procurar_palavra(self):

        palavra = input("Digite a palavra que deseja procurar na frase: ")

        contador = 0

        if palavra.lower() in self.frase.lower():
            contador += 1

            print(f"A palavra {palavra} aparecer {contador} vezes na frase")

        else: 
            print(f"A palavra {palavra} nao esta na frase")

    def obter_frase(self):
        print(f"A frase atual e {self.frase}")

def menu():

    print("\nBem-vindo ao Formatador de Frase!")

    frase = input("Digite uma frase: ")

    minha_frase = FormatadorDeFrase(frase)

    while True:
        try:
            print("\nEscolha uma opção para formatar a sua frase:")
            print("1. Converter para maiúsculas")
            print("2. Converter para minúsculas")
            print("3. Capitalizar a primeira letra da frase")
            print("4. Converter para o formato título.")
            print("5. Contar Vogais")
            print("6. Contar Consoantes")
            print("7. Contar letra 'a'")
            print("8. Pesquisar palavra")
            print("9. Mostrar frase atual")
            print("10. Sair")

            opcao = int(input( ))

            if opcao == 1:
                minha_frase.para_maiusculas()

            elif opcao == 2:
                minha_frase.para_minusculas()
            
            elif opcao == 3:
                minha_frase.capitalizar()

            elif opcao == 4:
                minha_frase.formato_titulo()

            elif opcao == 5:
                minha_frase.contar_vogais()

            elif opcao == 6:
                minha_frase.contar_consoantes()

            elif opcao == 7:
                minha_frase.contar_letra_a()

            elif opcao == 8:
                minha_frase.procurar_palavra()

            elif opcao == 9:
                minha_frase.obter_frase()

            else:
                print("Obrigado por usar o programa!")           
                break

        except ValueError:
            print("Valor invalido digite uma opcao valida")

menu()