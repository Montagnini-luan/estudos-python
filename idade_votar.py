"""
Exercício:

Verifique a Elegibilidade para Votar

Neste exercício, você vai executar um programa que determina 
se uma pessoa está ou não elegível para votar com base em sua idade.

    Execute o programa.
    Insira sua idade quando solicitado.
    O programa irá informar se você é elegível para votar ou não.

Note que a idade mínima para votar é de 18 anos.
"""

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você tem idade para votar.")

else:
    print("Você não tem idade para votar.")