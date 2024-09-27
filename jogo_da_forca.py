"""
Jogo da Forca com Listas de Strings em Python
Objetivo:

O objetivo deste exercício é criar uma versão do jogo da forca que utilize
listas de strings para desenhar o boneco. Você deve usar uma lista para cada linha
do desenho e organizá-las em uma lista de listas. Ao invés de controlar quando imprimir 
cada parte do boneco, você deve atualizar as listas, substituindo o elemento a ser desenhado.

Requisitos:

    1. Crie uma função chamada mostrar_tabuleiro que aceite como argumento o número 
    de erros do jogador. Esta função deve desenhar o estado atual do tabuleiro com o boneco.

    2. Utilize uma variável numero_de_erros para manter o controle do número de erros do jogador.

    3. O jogador deve continuar adivinhando letras até que:
        O número máximo de 6 erros seja alcançado, ou;
        A palavra seja completamente adivinhada.

    4. Utilize uma lista de strings para representar a palavra a ser adivinhada, 
    substituindo letras não adivinhadas por sublinhados ("_").

    5. Quando o jogo terminar, mostre uma mensagem informando se o jogador 
    ganhou ou perdeu, além de revelar a palavra que deveria ser adivinhada.

Dicas:

    Comece criando o tabuleiro em uma lista de listas, preenchendo 
    as partes que nunca mudam.
    
    Atualize o tabuleiro a cada erro do jogador, chamando a função 
    mostrar_tabuleiro com o número atual de erros como argumento.
"""

def mostrar_tabuleiro(n_erros):
    tabuleiro = [
        [' ', ' ', ' ', ' ', ' ', ' ', '_'],  # Parte superior do poste
        [' ', ' ', ' ', ' ', ' ', '|', ' '],  # Poste vertical, parte 1
        [' ', ' ', ' ', ' ', ' ', '|', ' '],  # Poste vertical, parte 2 (onde a cabeça aparece)
        [' ', ' ', ' ', ' ', ' ', '|', ' '],  # Poste vertical, parte 3 (onde o corpo e os braços aparecem)
        [' ', ' ', ' ', ' ', ' ', '|', ' '],  # Poste vertical, parte 4 (onde as pernas aparecem)
        ['_', '_', '_', '_', '_', '|', ' ']   # Base e parte inferior do poste
    ]

    if n_erros >= 1:
        tabuleiro[2][5] = "0"

    if n_erros >= 2:
        tabuleiro[3][5] = "|"
    
    if n_erros >= 3:
        tabuleiro[3][4] = "/"

    if n_erros >= 4:
        tabuleiro[3][6] = "\\"
    
    if n_erros >= 5:
        tabuleiro[4][4] = "/"
    
    if n_erros >= 6:
        tabuleiro[4][6] = "\\"

    for linha in tabuleiro:
        print("".join(linha))

n_erros = 0

palavra = "python"
palavra_oculta = ['_'] * len(palavra)

while n_erros < 6 and '_' in palavra_oculta:

    mostrar_tabuleiro(n_erros)

    print("Palavra a adivinhar: " + " ".join(palavra_oculta))

    chute = input("Digite uma letra: ")

    if chute in palavra:

        for indice, letra in enumerate(palavra):
            
            if letra == chute:
                palavra_oculta[indice] = chute
    else:
        n_erros += 1
    
mostrar_tabuleiro(n_erros)

if '_' in palavra_oculta:
        print("Voce perdeu a palvra era:", palavra )
    
else:
    print("Você ganhou! A palavra era: " + palavra)