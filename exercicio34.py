"""
Exercício: Manipulando Sequências de Números

Contexto: Você está trabalhando com sequências de números em um software 
de análise. Para isso, você utiliza tuplas, uma vez que as sequências são fixas 
e não precisam de alterações. Contudo, existem algumas operações com as sequências 
que você precisa realizar para obter novos conjuntos de dados.

Objetivo: Utilize operações com tuplas para manipular e analisar sequências de números.

Instruções:

    1. Concatenação de Sequências:
        Você possui duas sequências: A = (1, 2) e B = (3, 4).
        Crie uma nova sequência C combinando as sequências A e B.

    2. Repetição de Sequências:
        Suponha que você queira repetir a sequência A três vezes para criar uma nova sequência D.
        Faça essa operação e registre o resultado em D.

    3. Análise de Elemento em Sequência:
        Utilizando a sequência E = (1, 2, 3, 4, 1, 2, 1, 2), verifique se o número 2 está presente.

Questões:

a) Qual é a sequência resultante C após a concatenação?

b) Qual é a sequência D após repetir a sequência A três vezes?

c) O número 2 está presente na sequência E?

O exercício busca ensinar as operações básicas que podem ser 
realizadas com tuplas. Ao final, você deve ser capaz de manipular 
e combinar diferentes tuplas para obter novos conjuntos de dados.
"""

A = (1, 2)
B = (3, 4)

C = A + B
print(C)

D = A * 3
print(D)

E = (1, 2, 3, 4, 1, 2, 1, 2)

print(2 in E)