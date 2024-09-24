"""
Exercício: Vetores Par, Ímpar e Outras Operações

Desenvolva um programa que realize as seguintes funcionalidades:

    1. Leia 20 números inteiros e armazene-os em um vetor.
    
    2. Separe os números pares e armazene-os em um vetor chamado PAR.
    
    3. Separe os números ímpares e armazene-os em um vetor chamado IMPAR.
    
    4. Imprima os três vetores.
    
    5. Bônus 1: Informe a soma total dos números pares e ímpares.
    
    6. Bônus 2: Mostre qual dos vetores, PAR ou IMPAR, tem a maior quantidade de elementos.
    
    7. Bônus 3: Solicite ao usuário que digite um número. Informe se este número está 
        presente em algum dos vetores e, se sim, em qual deles.
"""

vetor = []
vetor_par = []
vetor_impar = []


for i in range(5):

    num = int(input("Digite um numero: "))
    vetor.append(num)

    if num % 2 == 0:

        vetor_par.append(num)

    else:

        vetor_impar.append(num)


print(f"Sua lista de numeros: {vetor}")
print(f"Numeros pares: {vetor_par}")
print(f"Numeros impares: {vetor_impar}")
print(f"A soma dos pares e: {sum(vetor_par)}")
print(f"A soma dos impares e: {sum(vetor_impar)}")

if len(vetor_par) > len(vetor_impar):

    print("O maior vetor e o par")

elif len(vetor_par) < len(vetor_impar):

    print("O maior vetor e o impar")

else:

    print("Os dois vetores tem o mesmo tamnho")

opcao = int(input("Digite um numero para verifcar em qual vetor ele esta: "))

if opcao in vetor_par:
    print("O numro esta no vetor par")

elif opcao in vetor_impar:
    print("O numero esta no vetor impar")

else:
    print("O numero nao esta em nenhum vetor")