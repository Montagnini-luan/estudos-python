"""
Exercício - Jogo da Velha com Matriz

Objetivo: Implementar o jogo da velha usando uma matriz 3x3 e permitir que dois jogadores joguem um contra o outro.

Instruções:

    Inicialize uma matriz 3x3 com espaços em branco para representar o tabuleiro do jogo da velha.
    Crie uma função para exibir o tabuleiro atualizado a cada jogada.
    Crie uma função para verificar se há um vencedor.
    Implemente um loop que alterna entre os jogadores (X e O) e permite que eles escolham uma posição no tabuleiro.
    Após cada jogada, verifique se há um vencedor ou se o tabuleiro está cheio.
    Se houver um vencedor ou o tabuleiro estiver cheio, termine o jogo e exiba o resultado.

Dicas:

    Lembre-se de verificar as linhas, colunas e diagonais ao procurar por um vencedor.
    Certifique-se de que os jogadores não possam escolher uma posição que já foi ocupada.
    Use funções para organizar seu código e torná-lo mais legível.

"""

tabuleiro = []

for i in range(3):

    linha = []

    for j in range(3):

        linha.append(" ")

    tabuleiro.append(linha)
        
def exibir_tabuleiro():

    for linha in tabuleiro:

        print("|".join(linha))

        print("-" * 5)

def vitoria(jogador):

    for i in range(3):

        todas_linhas = True
        todas_colunas = True

        for j in range(3):

            if tabuleiro[i][j] != jogador:
                todas_linhas = False

            if tabuleiro[j][i] != jogador:
                todas_colunas = False

        if todas_linhas or todas_colunas:
                return True
            
        if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
                return True
        
        if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
                return True

        return False

def jogada(jogador):

    while True:
        
        jogada = input(f"Jogador {jogador}, escolha a linha e coluna: ")

        try:

            linha, coluna = map(int, jogada.split())
            
            if tabuleiro[linha][coluna] == ' ':

                tabuleiro[linha][coluna] = jogador

                break

            else:

                print("Posição já ocupada. Tente novamente.")

        except:
            print("Entrada inválida. Tente novamente.")


jogador_atual = 'X'


for _ in range(9):
    
    exibir_tabuleiro()
    
    jogada(jogador_atual)
    
    if vitoria(jogador_atual):
        
        exibir_tabuleiro()
        
        print(f"Jogador {jogador_atual} venceu!")
        
        break
    
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'

else:
    
    exibir_tabuleiro()
    
    print("Empate!")
