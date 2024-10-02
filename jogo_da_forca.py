def mostrar_tabuleiro(n_erros):
    tabuleiro = [
        [' ', ' ', ' ', ' ', ' ', ' ', '_'],
        [' ', ' ', ' ', ' ', ' ', '|', ' '],
        [' ', ' ', ' ', ' ', ' ', '|', ' '],
        [' ', ' ', ' ', ' ', ' ', '|', ' '],
        [' ', ' ', ' ', ' ', ' ', '|', ' '],
        ['_', '_', '_', '_', '_', '|', ' ']
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
chutes = set()

while n_erros < 6 and '_' in palavra_oculta:
    mostrar_tabuleiro(n_erros)
    print("\nPalavra a adivinhar: " + " ".join(palavra_oculta))

    chute = input("Digite uma letra: ").lower()
    if len(chute) != 1 or not chute.isalpha():
        print("Entrada inválida. Por favor, digite uma única letra.")
        continue
    if chute in chutes:
        print("Você já adivinhou essa letra. Tente novamente.")
        continue
    
    chutes.add(chute)

    if chute in palavra:
        for indice, letra in enumerate(palavra):
            if letra == chute:
                palavra_oculta[indice] = chute
    else:
        n_erros += 1

mostrar_tabuleiro(n_erros)

if '_' in palavra_oculta:
    print("Você perdeu! A palavra era: " + palavra)
else:
    print("Você ganhou! A palavra era: " + palavra)
