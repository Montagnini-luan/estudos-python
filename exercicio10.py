"""
Exercício: Lista de Compras

Objetivo: Use um loop for para iterar sobre uma lista de itens de 
compras e imprimir cada item em um formato específico.

Instruções:

    1. Crie uma lista chamada itens_compra contendo alguns itens que 
    você compraria em uma loja, por exemplo: ["maçã", "banana", "cenoura", "leite"].
    
    2. Use um loop for para iterar sobre os itens da lista.
    3. Para cada item na lista, imprima o item no seguinte formato: "Eu preciso comprar [item]".

Após concluir o exercício, sua saída deve se parecer com:

Eu preciso comprar maçã
Eu preciso comprar banana
Eu preciso comprar cenoura
Eu preciso comprar leite

"""

lista = ["maçã", "banana", "cenoura", "leite"]

for item in lista:

    print(f"Eu preciso comprar {item}")

