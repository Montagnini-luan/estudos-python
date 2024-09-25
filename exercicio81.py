"""
Exercício - Informações de Frutas em uma Mercearia

Em uma mercearia, várias frutas são vendidas, e você deseja criar um 
sistema simples para gerenciar as informações sobre essas frutas.

Objetivos:

    1. Definir uma classe chamada Fruta.
    2. Instanciar um ou mais objetos desta classe.
    3. Acessar e exibir os atributos dos objetos instanciados.

Instruções:

    1. Crie uma classe chamada Fruta com os seguintes atributos:
        - nome: o nome da fruta (ex: "Maçã", "Banana").
        - preco_por_kg: o preço da fruta por quilograma.
        - quantidade_em_estoque: a quantidade da fruta em estoque (em quilogramas).

    2. Instancie pelo menos duas frutas diferentes, fornecendo valores específicos para seus atributos.

    3. Acesse os atributos das frutas instanciadas e exiba suas informações de forma organizada, como:
    
        Nome da Fruta: [nome da fruta]
        Preço por Kg: [preço da fruta por quilograma]
        Quantidade em Estoque: [quantidade da fruta em estoque]

"""

class frutas:

    def __init__ (self, nome, peco_por_kg, quantidade_em_estoque):

        self.nome = nome
        self.peco_por_kg = peco_por_kg
        self.quantidade_em_estoque = quantidade_em_estoque

    def exibir_info(self):

        print("Nome da fruta:", self.nome)
        print("preco por KG:", self.peco_por_kg)
        print("Quantidade em estoque em:", self.quantidade_em_estoque)



fruta1 = frutas("maca", 9.99, 50)

fruta2 = frutas("banana", 4.99, 50)

fruta1.exibir_info()
print("-" * 30)
fruta2.exibir_info()

