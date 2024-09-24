"""
Exercício: Impressão de Números

Desenvolva um programa que realize as seguintes funcionalidades:

    1. Imprima na tela os números de 1 a 20, um abaixo do outro.
    
    2. Após a finalização da primeira lista, o programa deve imprimir 
        os números de 1 a 20 um ao lado do outro, separados por espaços.
        
    3. Bônus: Permita que o usuário defina o intervalo de números a serem 
        impressos. Por exemplo, o usuário pode optar por imprimir os números de 5 a 30.
"""

numero1 = int(input("Escreva o primeiro numero: "))
numero2 = int(input("Escreva o segundo numero: "))

for i in range(numero1, numero2 + 1):
    print(i,)

print("\n")

for i in range(numero1, numero2 + 1):
    print(i, end=" ")