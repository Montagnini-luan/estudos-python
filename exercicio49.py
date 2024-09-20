"""
Exercício: Operações com Conjuntos em Python

Objetivo: Familiarizar-se com as operações de conjuntos em Python e compreender 
como elas funcionam através de exemplos práticos.

Instruções:

    1. Criação de Conjuntos:
        Crie dois conjuntos: s1 contendo os números de 1 a 5 e s2 contendo os números de 4 a 8.

    2. União:
        Use a operação de união para combinar s1 e s2 e armazene o resultado 
        em uma variável chamada uniao.
        
        Imprima o resultado.
        Repita usando o método union().

    3. Intersecção:
        Determine os elementos comuns entre s1 e s2 e armazene o resultado 
        em uma variável chamada interseccao.
        
        Imprima o resultado.
        Repita usando o método intersection().

    4. Diferença:
        Determine os elementos que estão em s1 mas não em s2 e armazene o 
        resultado em uma variável chamada diferenca.
        
        Imprima o resultado.
        Repita usando o método difference().

    5. Diferença Simétrica:
        Determine os elementos que estão em s1 ou em s2, mas não 
        em ambos. Armazene o resultado em uma variável chamada diff_simetrica.
        
        Imprima o resultado.
        Repita usando o método symmetric_difference().

    6. Subset e Superset:
        Verifique se s1 é um subconjunto de s2 e imprima o resultado.
        Verifique se s2 é um superconjunto de s1 e imprima o resultado.

Dicas:

    Utilize operadores como |, &, -, ^ para realizar operações entre conjuntos.
    
    Métodos como union(), intersection(), difference(), symmetric_difference(), issubset(), issuperset() 
    também estão disponíveis para realizar essas operações.
"""


s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

uniao = s1 | s2
print(uniao)
uniao = s1.union(s2)
print(uniao)

interseccao = s1 & s2
print(interseccao)
interseccao = s1.intersection(s2)
print(interseccao)

diferenca = s1 - s2
print(diferenca)
diferenca = s1.difference(s2)
print(diferenca)

diferneca_simetrica = s1 ^ s2
print(diferneca_simetrica)
diferneca_simetrica = s1.symmetric_difference(s2)
print(diferneca_simetrica)

is_subset = s1.issubset(s2)
print(is_subset)

is_superset = s2.issuperset(s1)
print(is_superset)