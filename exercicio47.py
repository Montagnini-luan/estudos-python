"""
Exercício: Criação de Conjuntos em Python

Objetivo: Familiarizar-se com a criação de conjuntos em Python utilizando duas abordagens diferentes.

Instruções:

    1. Usando Chaves:
        Crie um conjunto chamado frutas_chaves que contenha as seguintes 
        frutas: "maçã", "banana" e "cereja".
        
        Imprima o conjunto.

    2. Usando a Função set():
        Crie uma lista chamada frutas_lista contendo as 
        frutas: "uva", "manga", "manga" e "uva".
        
        Converta frutas_lista em um conjunto chamado frutas_funcao.
        Imprima o conjunto.

    3. Comparação:
        Verifique se os conjuntos frutas_chaves e frutas_funcao possuem 
        alguma fruta em comum. Se sim, imprima a fruta em comum. Caso contrário, 
        imprima "Os conjuntos não têm frutas em comum".

Dicas:

    Lembre-se que conjuntos não permitem elementos duplicados. Portanto, ao 
    criar um conjunto com elementos repetidos, o conjunto resultante terá apenas 
    uma instância de cada elemento.
"""

frutas = {"maçã", "banana", "cereja"}

print(frutas)


lista_frutas = set(['uva', 'manga', 'manga', 'uva'])

print(lista_frutas)

if frutas == lista_frutas:
    print()
else:
    print('O conjunto não tem frutas em comum!')