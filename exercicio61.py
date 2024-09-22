"""
Exercício: Comparação de Preços e Desconto Adicional para Cinco Produtos

Objetivo: Desenvolver um programa que obtenha do usuário o preço de cinco
produtos e indique qual produto deve ser comprado com base no menor preço. 

Além disso, se o usuário optar por comprar o produto recomendado, o programa oferecerá um desconto.

Instruções:

    1. Solicite ao usuário que informe o preço de cinco produtos.
    2. Determine e exiba qual dos cinco produtos é o mais barato.
    3. Informe ao usuário a diferença de preço entre o produto mais barato e os outros quatro.
    4. Pergunte ao usuário se ele deseja comprar o produto mais barato agora.
        a. Se o usuário responder "sim", ofereça um desconto de 5% sobre o preço 
        do produto mais barato e informe o novo preço.
        
        b. Se o usuário responder "não", exiba uma mensagem: "Lembre-se de sempre 
        buscar o melhor negócio!"
    
    5. Caso o usuário escolha comprar o produto mais barato com o desconto, 
    peça um método de pagamento:
    
    a. Se o método de pagamento for "dinheiro", ofereça um desconto adicional de 2%.
        b. Se for "cartão", informe que o pagamento pode ser dividido em até 3 vezes sem juros.
    
    6.Exiba um resumo da compra, incluindo produto escolhido, preço original, desconto 
    aplicado e preço final.

Observações: O programa deve considerar que o usuário fornecerá apenas valores numéricos 
válidos para os preços. As respostas do usuário para perguntas como a intenção de compra 
podem ser "sim" ou "não", e o programa deve ser insensível a maiúsculas e minúsculas (ou 
seja, "Sim", "sim" e "SIM" são consideradas a mesma resposta).
"""

produto = []

for i in range(1, 6):
    precos = float(input("Digite o prco de 5 produtos: "))

    produto.append(precos)
print(produto)
mais_barato = min(produto)
print(f"\nO produto mais barato custa R$ {mais_barato:.2f}\n")

contador = 0
for i in produto:
    diferenca = i - mais_barato
    contador += 1
    if diferenca != 0:
        print(f"A diferenca do mais barato para o {contador} produto e de R${diferenca:.2f} ")

escolha = input("\nVoce deseja comprar o produto mais barato agora (Sim / Nao)? ")


if escolha.lower() == "sim":
    desconto = mais_barato * 0.05
    total_compra = mais_barato - desconto
    print(f"\nParabens voce acaba de ganhar um desconto de R${desconto:.2f}!")
    pagamento = input(f"\nNovo preco de {total_compra}, como voce gostaria de pagar (dinheiro / cartao): ")
    desconto_dinheiro = 0
    if pagamento.lower() == "dinheiro":
        desconto_dinheiro = total_compra * 0.02
        total_compra = mais_barato - desconto_dinheiro
        print(f"\nVoce ganhou mais R${desconto_dinheiro:.2f} de desconto por comprar em dinheiro!")
        print(f"\nTotal da compra R${total_compra}")
    elif pagamento.lower() == "cartao":
        print("Voce pode parcelar em ate 3x sem juros!")
        parcelamento = int(input("Digite em quantas vezes deja parcelar (1 - 3)"))
        total_compra = mais_barato - desconto
    else:
        print("opcao invalida")

    print(f"\nResumo da Compra:")
    print(f"Produto escolhido: Produto mais barato")
    print(f"Preço original: R$ {mais_barato:.2f}")
    print(f"Desconto aplicado: R$ {desconto + desconto_dinheiro:.2f}")
    print(f"Preço final: R$ {total_compra:.2f}")
    if pagamento.lower() == "cartao":
        print(f"Parcelado em: {parcelamento}x de R$ {total_compra / parcelamento:.2f}")

elif escolha.lower() == "nao":\
        print("\nLembre-se de sempre buscar o melhor negócio!")