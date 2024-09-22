"""
Exercício Controle de Empréstimos em uma Biblioteca

Objetivo: Desenvolver um programa que auxilie Maria, uma bibliotecária, 
a controlar o número de livros emprestados por um usuário durante o mês. Para 
cada dia que o usuário exceder o limite estabelecido de livros pegos, uma multa 
será aplicada.

Instruções:

    1. O sistema de biblioteca possui um limite estabelecido de 5 
    livros que cada usuário pode pegar por vez.
    
    2. Para cada livro excedente, o usuário deve pagar uma multa de R$ 2,00.
    
    3. O programa deve começar solicitando ao usuário o número de 
    dias em que pegou livros no mês.
    
    4. Em seguida, para cada um desses dias, o programa deve pedir que 
    o usuário informe o número de livros pegos.
    
    5. O sistema deve calcular e exibir o excesso de livros e o valor 
    da multa para cada dia.
    
    6. Ao final, o programa deve mostrar o total de livros excedentes e 
    o total da multa acumulada no mês.
    
    7. Se, ao final do mês, o usuário não tiver excedido o limite em nenhum dia, 
    o programa deve mostrar uma mensagem de parabenização por seguir as regras.

Observação: O programa deve considerar que o usuário informará dados válidos, ou seja, 
valores inteiros não-negativos para o número de dias e o número de livros pegos em cada dia.
"""

limite_livros = 5
multa = 2.00

dias_livros = int(input("Digite o número de dias que você pegou livros no mês: "))

total_exedido = 0
total_multa = 0

for i in range(1, dias_livros + 1):
    livros_dia = int(input(f"Quantos livros você pegou no dia {i}: "))

    exedido = max(0, livros_dia - limite_livros)
    multa_livro = multa * exedido

    if exedido > 0:
        print(f"\nNo dia {i}, você excedeu em {exedido} livros e deve pagar R${multa_livro:.2f} de multa.")
    else:
        print(f"\nNo dia {i}, você não excedeu o limite de livros.")

    total_exedido += exedido
    total_multa += multa_livro

if total_exedido > 0:
    print(f"Você excedeu {total_exedido} livros, gerando uma multa total de R${total_multa:.2f}.")
else:
    print("Você não excedeu o limite de livros. Parabéns!")

