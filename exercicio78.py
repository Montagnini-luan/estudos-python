"""
Exercício: Aprovação de Empréstimo Bancário com Validação de E-mail

O objetivo deste exercício é criar um programa Python para aprovar o empréstimo 
bancário para a compra de uma casa. Além disso, o programa deve validar o 
e-mail do requerente.

Requisitos:

    1. O programa deve começar pedindo ao usuário para fornecer um endereço de e-mail.
        Se o e-mail for inválido, o programa deve informar ao usuário e encerrar a execução.

    2. Se o e-mail for válido, o programa deve continuar e pedir as seguintes informações:
        Valor da casa a ser comprada.
        Salário do requerente.
        Quantidade de anos que o requerente planeja pagar pelo empréstimo.

    3. O valor da prestação mensal não pode exceder 30% do salário do requerente.
        Calcular o valor da prestação como sendo o valor da casa a comprar dividido 
        pelo número de meses a pagar.

    4. Com base nas informações fornecidas e nos cálculos realizados, o programa 
    deve decidir se o empréstimo será aprovado ou não.
        Se aprovado, informar o valor da prestação.
        Se não aprovado, informar que o empréstimo foi negado.
"""

import re

def validar_email(email):

    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    return bool(re.fullmatch(padrao, email))

email = input("Insira um email valido: ")


if not validar_email(email):
    print("email invalido!")
    exit()

else:

    valor = int(input("Digire o valor do imovel que deseja comprar: "))
    parcela = int(input("Digite em quntos anos voce deseja pagar: "))
    salario = int(input("Digire o seu salario mensal: "))

    valor_parcela = valor / (parcela * 12)

    if valor_parcela <= salario * 0.3:
        print("Seu emprestimo foi aprovado!")
        print(f"Sua parcela vai ser de {valor_parcela}")

    else:
        print("Emprestimo reprovado! valor da parcela mair do que 30% do seu salrio")
