"""
Exercício sobre Iterando Sobre Dicionários

Objetivo: Você tem um dicionário que representa o número de livros vendidos 
em uma livraria em diferentes meses. Sua tarefa é iterar sobre esse dicionário 
para realizar diferentes análises.

Dicionário fornecido:

Instruções:

    1. Iterando sobre as chaves (meses):
        - Imprima todos os meses em que a livraria registrou vendas.

    2. Iterando apenas sobre os valores (número de livros vendidos):
        - Calcule e imprima a venda total nos 5 meses.
        - Determine e imprima o mês com as vendas mais baixas.

    3. Iterando sobre chaves e valores simultaneamente (itens):
        - Para cada mês, imprima uma mensagem no seguinte 
        formato: "Em [mês], [número] livros foram vendidos".
        
"""
vendas = {
    "Janeiro": 120,
    "Fevereiro": 150,
    "Março": 80,
    "Abril": 190,
    "Maio": 210
}

print("Meses que registaram vendas:")
for meses in vendas:
    print(meses)


total = 0
venda_mais_baixas = float('inf')
mes_vendas_mais_baixas = ""
for venda in vendas.values():
    total += venda
    if venda < venda_mais_baixas:
        venda_mais_baixas = venda
for mes, venda in vendas.items():
    if venda == venda_mais_baixas:
        mes_vendas_mais_baixas = mes
        break
print(f"venda total é de: {total}")
print(f"O mes com vendas mais baixas foi: {mes_vendas_mais_baixas}")

for meses, venda in vendas.items():
    mes = meses
    numero_vendido = venda
    print(f"Em {mes}, {numero_vendido} livros foram vendidos")