"""
Exercício: Iteração em Listas

Objetivo: Familiarizar-se com a iteração através de listas usando o 
loop for e a função enumerate() para acessar o índice e o valor dos elementos.

Instruções:

    Dada a lista nomes = ["Alice", "Bruno", "Clara", "Daniel", "Eduarda"], use um 
    loop for para imprimir cada nome na lista.

    Utilizando a mesma lista nomes, imprima o nome juntamente com a sua posição na 
    lista (índice). Para isso, utilize a função enumerate().

    Dada a lista notas = [85, 90, 78, 92, 88], use a função enumerate() para imprimir o 
    nome do aluno da lista nomes e a sua respectiva nota da lista notas.
    
Este exercício permite praticar a iteração em listas e combinar informações 
de múltiplas listas usando índices, tudo isso enquanto se familiarizam com a função útil enumerate().

"""

nomes = ["Alice", "Bruno", "Clara", "Daniel", "Eduarda"]

for nome in nomes:

    print(nome)

for indice, nome  in enumerate(nomes):
    print(f"Nome no índice {indice} é {nome}")


notas = [85, 90, 78, 92, 88]

for indice, nome in enumerate(nomes):
    
    print(f"{nome} obteve nota {notas[indice]}")