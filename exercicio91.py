"""
Exercício: Polimorfismo de "Sobrecarga" com a Classe Impressora

O objetivo deste exercício é criar uma classe Impressora que possa 
imprimir dados de tipos diferentes: texto, lista de textos e dicionário 
de textos. Para isso, implementaremos um método imprimir que se comporta 
de forma diferente, dependendo do tipo de dado passado como argumento.

    Passo 1: Implemente a Classe Impressora

        Crie uma classe Impressora com um método imprimir que 
        aceita um único argumento. Dentro do método, utilize if e isinstance 
        para verificar o tipo do argumento e decidir como imprimi-lo.
        
        
    Passo 2: Teste a Classe

        Após implementar a classe, crie uma instância da Impressora 
        e chame o método imprimir com diferentes tipos de argumentos.
"""

class Impressora:
    def imprimir(self, dado):

        if isinstance(dado, str):
            print(f"Imprimindo texto {dado}")

        elif isinstance(dado, list):
            print("Imprimindo lista de texto")

            for item in dado:
                print(f"- {item}")

        elif isinstance(dado, dict):
            print("Imprimindo dicionario")

            for chave, valor in dado.items():
                print(f" - {chave}: {valor}")

        else:
            print("valor invalido")

impressora = Impressora()

impressora.imprimir("Olá, mundo!")

impressora.imprimir(["Olá", "mundo", "!"])

impressora.imprimir({"saudacao": "Olá", "objeto": "mundo"})
