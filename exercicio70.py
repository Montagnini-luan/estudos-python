"""
Exercício: Vetor Inverso e Operações

Desenvolva um programa que realize as seguintes funcionalidades:

    1. Leia um vetor de 10 números reais.
    
    2. Mostre-os na ordem inversa.
    
    3. Bônus 1: Calcule e exiba a média dos números inseridos.
    
    4. Bônus 2: Informe quantos números no vetor são maiores 
        que a média calculada.
    
    5. Bônus 3: Solicite ao usuário que escolha um dos números 
        do vetor e mostre sua posição original.
"""
lista_numeros = []

for _ in range(10):
    numero = int(input("Digite um numero: "))
    lista_numeros.append(numero)

print(f"a lista invertida e {lista_numeros[::-1]}")

soma = 0

for i in lista_numeros:
    soma += i 

media = soma / len(lista_numeros)

print(f"A media e {media}")

maior_media = []

for j in lista_numeros:

    if j > media:
        maior_media.append(j)

print(f"Esses numeros sao maiores que a media {maior_media}")

posicao = int(input("Digite um numro para saber a posicao dele na lista: "))

for k in lista_numeros:

    if posicao == k:
        print(f"O numero esta no posicao {k}")