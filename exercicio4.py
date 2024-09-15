"""
Exercício:

Crie um algoritmo que leia n números inteiros digitados pelo usuário,
e só pare quando o usuário digite 0.

No final, imprima na tela a soma de todos os números digitados.

"""

numero = int(input("Digite um número ou 0 para sair: "))
soma = 0

while True:

    if numero != 0:
        soma += numero
        numero = int(input("Digite um número ou 0 para sair: "))
    else:
        print("você digitou o numero 0")
        break

print(f"A soma dos numros digitos é {soma}!")