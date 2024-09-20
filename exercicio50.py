"""
Exercício: Aplicações Práticas de Conjuntos

Objetivo: Familiarizar-se com as aplicações práticas dos conjuntos, incluindo a 
remoção de duplicatas, teste de pertença e operações matemáticas de conjunto.

Instruções:

    1. Removendo Duplicatas:
        Dada a lista números = [10, 20, 30, 10, 40, 20], remova as duplicatas e imprima a lista 
        resultante.

    2. Testar a Pertença:
        Verifique se o número 25 está presente na lista única do passo anterior e imprima uma 
        mensagem apropriada.

    3. Operações de Conjunto:
        Dados os conjuntos conjunto_a = {1, 2, 3, 4} e conjunto_b = {3, 4, 5, 6}, realize 
        as seguintes operações:
            Encontre a união de ambos os conjuntos e imprima o resultado.
            Encontre a interseção de ambos os conjuntos e imprima o resultado.
            Encontre a diferença do conjunto_a em relação ao conjunto_b e imprima o resultado.
            Encontre a diferença simétrica entre os dois conjuntos e imprima o resultado.
            
            
Este exercício ajuda a praticar e solidificar sua compreensão das aplicações práticas dos conjuntos em Python.
"""

números = [10, 20, 30, 10, 40, 20]

remove_dupplicadas = set(números)
unicos = list(remove_dupplicadas)
print(unicos)

if 25 in unicos:
    print("O numero esta na lista")

else:
    print("O numero nao esta na lista")

conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

uniao_conjunto = conjunto_a | conjunto_b
print(uniao_conjunto)

insercao = conjunto_a & conjunto_b
print(insercao)

diferenca = conjunto_a - conjunto_b
print(diferenca)

diferenca_simetrica = conjunto_a ^ conjunto_b
print(diferenca_simetrica)