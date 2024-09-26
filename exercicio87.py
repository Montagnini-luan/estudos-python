"""
Exercício: Termômetro Digital

Você vai criar uma classe Termometro que representará um termômetro 
digital simples.

Requisitos:

    1. O termômetro deve ter um atributo protegido _temperatura que 
        armazena a temperatura atual em graus Celsius.
    
    2. Implemente um método getter usando @property para a temperatura.
    
    3. Implemente um método setter para a temperatura que verifica se o 
        valor é uma temperatura razoável para a atmosfera terrestre (digamos, entre -100°C e 100°C).

Exemplo de Uso:

t = Termometro()
t.temperatura = 25
print(t.temperatura)  # Deve imprimir 25

t.temperatura = 200  # Deve imprimir "Temperatura fora do alcance"
print(t.temperatura)  # Deve imprimir 25, pois a temperatura anterior não foi alterada


Sua tarefa é implementar essa classe Termometro e garantir que ela funcione como especificado.
"""


class Termometro:
    def __init__(self):
        self._temperatura = 0
    
    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):

        if -100 <= valor <= 100:
            self._temperatura = valor

        else:
            print("Temperatura fora do alcance")
    

t = Termometro()

t.temperatura = 25
print(t.temperatura)

t.temperatura = 200
print(t.temperatura)