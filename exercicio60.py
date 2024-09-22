"""
Exercício: Nome na Vertical em Escada com Variações

Desenvolva um programa com as seguintes especificações:

    1. Solicite ao usuário que digite seu nome.

    2. Pergunte ao usuário como ele deseja ver o nome exibido:
        a) Em formato de escada.
        b) Em formato de escada invertida.
        
    3. Baseado na escolha do usuário, exiba o nome conforme solicitado.

Por exemplo, se o usuário digitar o nome "ANA" e escolher a opção de 
escada, o programa deve exibir:

A
AN
ANA

Se escolher a opção de escada invertida, o programa deve exibir:

  A
 AN
ANA

"""

nome = input("Digite um nome: ")
modo = input(f"Digite o modo em que deseja exibir o {nome} (escada ou escada invertida): ")

if modo.lower() == "escada":

    for i in range(1, len(nome) + 1):
        for letra in nome:
            letra = nome[:i]
        print(letra)

elif modo.lower() == "escada invertida":
    espacos = len(nome)

    for i in range(1, len(nome)  + 1):
        for letra in nome:
            letra = " " * espacos + nome[:i]
        espacos -= 1

        print(letra)

else:
    print("valor invalido!")