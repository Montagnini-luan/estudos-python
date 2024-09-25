"""
Exercício: Sistema de Reservas para um Evento

Objetivo: Compreender a definição e utilização de métodos dentro de classes em Python.

Descrição:

Crie uma classe chamada Evento que represente um evento com um número limitado de 
lugares. A classe deve permitir:

    1. Reservar um lugar.
    2. Cancelar uma reserva.

A classe Evento deve ter os seguintes métodos:

    - reservar(): Este método deve diminuir o número de lugares disponíveis em um.
    - cancelar(): Este método deve aumentar o número de lugares disponíveis em um.
    - lugares_disponiveis(): Este método deve retornar o número de lugares disponíveis.

Restrições:

    1. O evento tem uma capacidade inicial definida (por exemplo, 10 lugares).
    
    2. Se tentar reservar um lugar e todos estiverem ocupados, o sistema deve 
    informar que não há lugares disponíveis.
    
    3. Se tentar cancelar uma reserva e todos os lugares estiverem disponíveis, 
    o sistema deve informar que não há reservas para cancelar.

"""

class Evento:

    def __init__(self, lugares=10):
        self.lugares = lugares
    
    def mostrar_disponivel(self):
        print(f"Tem {self.lugares} lugares disponiveis")

    def reservar(self):

        if self.lugares > 0:

            valor = int(input(f"Digite a quantidade de lugares que voce deseja resver (disponivel: {self.lugares}): "))

            if valor <= self.lugares:
                self.lugares -= valor
                print(f"\n{valor} lugares reservados com sucesso")

            else:
                print("Impossivel reservar esse numero de lugares")

        else:
            print("nehum lugar disponivel")

    def cancelar_reserva(self):

        if self.lugares < 10:

            valor = int(input(f"Digite a quantidade de lugares que voce deseja cancelar a reserva (disponivel: {10 - self.lugares}): "))

            if valor <= 10 - self.lugares:
                self.lugares += valor
                print(f"\n{valor} lugares cancelados com sucesso")

            else:
                print("Valor invalido")

        else:
            print("nehuma reserva feita")


evento = Evento()

while True:

    print("\nBem vindo ao evento")
    print("1- Mostrar lugares disponiveis")
    print("2- Reservar um local")
    print("3- Cancelar reserva")
    print("4- Sair")

    opcao = input("escolha uma opcao: ")

    if opcao == "1":
        evento.mostrar_disponivel()

    elif opcao == "2":
        evento.reservar()

    elif opcao == "3":
        evento.cancelar_reserva()

    elif opcao == "4":
        print("Obrigado por usar nosso aplicativo")
        break
    else:
        print("Opcao invalida")