"""
Exercício: Estendendo a Classe Veiculo usando super()

Neste exercício, você trabalhará com uma classe Veiculo e uma 
subclasse Carro. O objetivo é usar a função super() para estender a 
funcionalidade da classe pai Veiculo na classe filha Carro.

    Passo 1: Defina a Classe Pai

        Crie uma classe chamada Veiculo que tenha um método 
        exibir_info() para exibir informações sobre o veículo.
        
    Passo 2: Defina a Classe Filha

        Agora crie uma classe Carro que herda de Veiculo. 
        Adicione um atributo adicional cor e use super() no método 
        exibir_info() para chamar o método da classe pai e adicionar 
        informações sobre a cor.
        
    Passo 3: Teste as Classes

        Finalmente, instancie objetos tanto para a classe Veiculo quanto 
        para a classe Carro, e chame o método exibir_info() em ambos.
"""

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def exibir_info(self):
        print(f"Veículo da marca {self.marca}, modelo {self.modelo}.")


class Carro(Veiculo):

    def __init__(self, marca, modelo, cor):
 
        super().__init__(marca, modelo)

        self.cor = cor
    

    def exibir_info(self):

        super().exibir_info()

        print(f"Cor do carro: {self.cor}.")

veiculo1 = Veiculo("Citroen", "C4 Pallas")

veiculo1.exibir_info()

carro1 = Carro("Citroen", "C4 Pallas", "Petro")

carro1.exibir_info()

