"""
Exercício: Contagem Regressiva para Lançamento de Foguete

Objetivo:

Desenvolver um programa em Python que realize uma contagem regressiva 
para o lançamento de um foguete.

Requisitos:

    1. O programa deve iniciar a contagem em 10 e terminar em 0.

    2. Cada número deve ser impresso na tela, um por vez.

    3. Entre cada número impresso, o programa deve fazer uma pausa de 1 segundo.

    4. Após chegar a 0, o programa deve imprimir a palavra "Fogo!" na tela.

Dicas:

    Utilize a função sleep do módulo time para fazer a pausa entre os números.
"""

import time

for i in range(10, -1, -1):

    print(i)

    time.sleep(1)

print("Fogo!!!")