
"""
Exercício Herança Simples:

Crie uma classe Animal que tenha um método fazer_som(). 
Essa classe será a classe pai para outras duas classes: Cachorro e Gato. 

Ambas as classes filhas deverão ter seus próprios métodos fazer_som() que 
sobrescrevem o método da classe pai. Além disso, a classe Cachorro 
deve ter um método latir() e a classe Gato um método miar().

    1. A classe Animal deve ter um método fazer_som() que imprime "O animal faz um som".
    2. A classe Cachorro deve ter um método fazer_som() que imprime "O cachorro faz woof-woof".
    3. A classe Gato deve ter um método fazer_som() que imprime "O gato faz miau".
    4. A classe Cachorro deve ter um método adicional chamado latir() que imprime "Woof-woof".
    5. A classe Gato deve ter um método adicional chamado miar() que imprime "Miau".

Crie objetos das classes Cachorro e Gato e chame seus métodos para 
testar se tudo está funcionando como esperado.
"""


from regex import D


class Animal:
    def fazer_som(self):
        self.fazer_som = "O animal faz um som"

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro faz woof-woof")

    def latir(self):
        print("Woof-woof")

class Gato(Animal):
    def fazer_som(self):
        print("O gato faz miau")
    
    def miar(self):
        print("Miau")

cachorro = Cachorro()

gato = Gato()

cachorro.fazer_som()
cachorro.latir()

gato.fazer_som()
gato.miar()