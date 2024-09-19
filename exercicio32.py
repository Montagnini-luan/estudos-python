"""
Exercício: Gerenciando Inventário de Produtos

Contexto: Você trabalha em um depósito e possui um inventário de produtos 
armazenados em tuplas. Cada tupla contém o nome do produto, a quantidade em 
estoque e o preço unitário. Sua tarefa é acessar e exibir certas informações desses produtos.

Objetivo: Acesse e exiba informações específicas dos produtos usando índices e fatiamento de tuplas.

Instruções:

    Definindo um Produto:
        Comece definindo uma tupla chamada produto com as seguintes 
        informações: "Laptop", 10 (quantidade em estoque), 1500.00 (preço em dólares).

    Acessando elementos usando índices:
        Exiba o nome do produto.
        Em seguida, exiba a quantidade em estoque.

    Fatiamento de tuplas:
        Mostre as informações excluindo o preço (ou seja, nome e quantidade 
        em estoque) usando fatiamento de tuplas.

Questões:

a) Qual é o nome do produto?

b) Quantos itens desse produto estão em estoque?

c) Sem mostrar o preço, quais são as informações disponíveis sobre o produto?

"""
produtos = ("Laptop", 10, 1500.00)

print("Nome do produto:", produtos[0])
print("Qtd estoque", produtos[1])
print("Produto e estoque:", produtos[:2])