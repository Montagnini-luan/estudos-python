"""
Exercício:

Calculadora de Descontos

Você é um cliente em uma loja que está tendo uma promoção especial. Dependendo 
do valor da sua compra, você pode receber um desconto!

    Execute o programa.
    
    Insira o valor da sua compra quando solicitado.
    
    O programa irá calcular e informar o valor do desconto aplicado e o valor final 
    com o desconto.

Os descontos são aplicados da seguinte forma:

    Compras acima de R$1000 recebem 20% de desconto.
    Compras de R$500 a R$1000 recebem 10% de desconto.
    Compras abaixo de R$500 não recebem desconto.
    
    
"""

valor_compra = float(input("Por favor, digite o valor da sua compra: $"))

if valor_compra > 1000:
    
    desconto = 0.20 * valor_compra
    
    print("Você recebeu 20% de desconto!")
    
elif valor_compra >= 500 and valor_compra <= 1000:
    
    desconto = 0.10 * valor_compra
    
    print("Você recebeu 10% de desconto!")
    
else:
    
    desconto = 0
    
    print("Você não recebeu desconto.")

valor_final = valor_compra - desconto

print(f"Valor do desconto: R${desconto:.2f}")
print(f"Valor final da compra: R${valor_final:.2f}")
