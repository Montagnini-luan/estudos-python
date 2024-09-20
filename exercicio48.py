"""
Exercício: Manipulando Conjuntos em Python

Objetivo: Familiarizar-se com as operações de adição e remoção de 
elementos em conjuntos usando os métodos disponíveis em Python.

Instruções:

    1. Início:
        Crie um conjunto chamado animais que contenha os seguintes 
        elementos: "gato", "cachorro", "pássaro".

    2. Usando add():
        Adicione "peixe" ao conjunto animais usando o método add().
        Imprima o conjunto atualizado.

    3. Usando remove():
        Remova "pássaro" do conjunto animais usando o método remove().
        Imprima o conjunto atualizado.
        Tente remover "lagarto" do conjunto usando remove(). Observe o que acontece.

    4. Usando discard():
        Descarte "lagarto" do conjunto usando discard(). Observe o que acontece.
        Imprima o conjunto atualizado.

    5. Usando pop():
        Use o método pop() para remover um elemento aleatório do conjunto 
        e imprima o elemento removido.
        
        Imprima o conjunto atualizado.

    6. Usando clear():
        Limpe o conjunto usando o método clear().
        Imprima o conjunto para confirmar que todos os elementos 
        foram removidos.

Dicas:

    Lembre-se de que o método pop() remove um elemento aleatório, já 
    que os conjuntos são desordenados. Portanto, o resultado exato pode 
    variar a cada vez que você executa o código.
    
Este exercício prático permitirá compreenderem as operações 
fundamentais de adição e remoção em conjuntos em Python.
"""

from regex import D


elementos = {"gato", "cachorro", "passaro"}

elementos.add("peixe")
print(elementos)

elementos.remove("passaro")
print(elementos)

try:
    elementos.remove("passaro")
except KeyError as e:
    print("Elemento nao existe")

elementos.discard("largarto")
print(elementos)

elementos.pop()
print(elementos)

elementos.clear()
print(elementos)