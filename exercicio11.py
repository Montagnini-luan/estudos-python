"""
Exercício: Estrelas Descendentes

Objetivo: Use um loop for para criar um padrão descendente 
de estrelas (*). Comece com 5 estrelas na primeira linha e reduza 
uma estrela em cada linha subsequente até não restar nenhuma estrela.

Instruções:

    1. Use um loop for para iterar de 5 a 0 (dica: pense sobre 
    a função range() de maneira descendente).
    
    2. Em cada iteração do loop, imprima o número atual 
    de estrelas em uma única linha.

Após concluir o exercício, sua saída deve se parecer com:

*****
****
***
**
*
"""

for i in range(5, 0, -1):

    print("*" * i)