"""
Exercício: Dicionários e Funções

Objetivo: Praticar a interação entre dicionários e funções, aprendendo 
a passar dicionários como argumentos e a retornar dicionários a partir de funções.

Contexto:

Imagine que você está construindo um sistema para uma biblioteca. Este sistema deve ser capaz de:

    Registrar um novo livro, fornecendo título, autor e ano de publicação.
    Exibir detalhes de um livro registrado.

Instruções:

    1. Registro de Livro:

        a) Crie uma função chamada registrar_livro que aceite 
        três parâmetros: titulo, autor e ano.

        b) Esta função deve retornar um dicionário representando o livro. O dicionário deve 
        ter três chaves: 'titulo', 'autor' e 'ano', e os valores correspondentes devem ser 
        os fornecidos à função.

        Por exemplo:

        livro = registrar_livro("1984", "George Orwell", 1949)
        print(livro)
        # Output esperado: {'titulo': '1984', 'autor': 'George Orwell', 'ano': 1949}
        
    2. Exibição de Livro:

        a) Crie uma função chamada exibir_livro que aceite um 
        dicionário (representando um livro) como seu único argumento.

        b) A função deve imprimir os detalhes do livro em um formato 
        legível. Por exemplo:
        
        Título: 1984
        Autor: George Orwell
        Ano: 1949
        
        c) Teste sua função exibir_livro usando o dicionário que você criou 
        na etapa anterior (usando a função registrar_livro).

    Dicas:

        Lembre-se de usar o operador de atribuição = para criar pares 
        chave-valor no dicionário.
        
        Ao exibir os detalhes do livro, você pode usar um loop para iterar sobre 
        os pares chave-valor do dicionário ou acessar cada chave individualmente.


"""


def registrar_livro(titulo, autor, ano):

    return{
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    }

livro = registrar_livro("1984", "George Orwell", 1949)
print(livro)


def exibir_livro(livro_dicionario):
    print(f"Tituolo: {'titulo'}")
    print(f"autor: {'titulo'}")
    print(f"ano: {'titulo'}")


exibir_livro(livro)
