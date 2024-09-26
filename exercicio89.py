"""
Exercício: A Classe MusicoAtleta

Você está criando um software para uma competição muito especial
que envolve múltiplas disciplinas: música e esportes. 

Você foi instruído a criar classes que representem um Musico, um Atleta, e um 
MusicoAtleta que herda características de ambos.

    1. A classe Musico deve ter um método tocar_instrumento que 
        imprime "Tocando instrumento musical".

    2. A classe Atleta deve ter um método correr que imprime "Correndo na pista".

    3. A classe MusicoAtleta deve herdar de ambas as classes, Musico e Atleta.

    4. A classe MusicoAtleta deve também ter um método próprio chamado 
        exibir_habilidades, que imprime "Tocando instrumento e correndo".

Crie instâncias das classes e teste os métodos para garantir que a 
herança múltipla esteja funcionando como esperado.

A ideia aqui é praticar o conceito de herança múltipla, fazendo com que uma classe 
herde atributos e métodos de duas classes pai diferentes.
"""

class Musico:
    def tocar_instumento(self):
        print("Tocando instrumento musical")


class Atleta:
    def correr(self):
        print("Correndo na pista")


class MusicoAtleta(Musico, Atleta):

    def exibir_habilidades(self):
        print("Tocando instrumento e correndo")


musico_atleta = MusicoAtleta()

musico_atleta.tocar_instumento()

musico_atleta.correr()

musico_atleta.exibir_habilidades()