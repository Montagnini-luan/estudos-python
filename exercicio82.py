"""
Exercício Simulando a Rotina de uma Pessoa

Objetivo:
Neste exercício, você irá implementar uma classe chamada Pessoa que 
simula algumas atividades do dia a dia de um indivíduo. A classe deve conter 
métodos que representem diferentes ações, como acordar, comer, dirigir e dormir. 

Além disso, a classe deve manter o controle dos estados do indivíduo para evitar 
ações incompatíveis (por exemplo, não se pode dirigir enquanto come).

Requisitos:

    1. A classe deve ter um construtor que aceite o nome da pessoa como 
    parâmetro e inicialize os estados "acordado", "comendo" e "dirigindo" como False.

    2. Implemente métodos para as seguintes ações:
        x acordar(): Faz a pessoa acordar, se já não estiver acordada.
        x comer(): Permite que a pessoa coma, desde que não esteja dirigindo ou dormindo.
        x parar_de_comer(): Faz a pessoa parar de comer, se estiver comendo.
        x dirigir(): Permite que a pessoa dirija, desde que não esteja comendo ou dormindo.
        x parar_de_dirigir(): Faz a pessoa parar de dirigir, se estiver dirigindo.
        x dormir(): Permite que a pessoa durma, desde que não esteja comendo ou dirigindo.

    3. Cada método deve imprimir mensagens adequadas para indicar o que a pessoa 
    está fazendo ou por que uma ação não pode ser realizada.

    4. Teste a classe criando um objeto e chamando vários métodos em sequência, simulando 
    um dia na vida da pessoa.
"""

class pessoa:

    def __init__(self, nome):
        
        self.nome = nome
        self.acordado = False
        self.comendo = False
        self.dirigindo = False
    
    def acordar(self):

        if self.acordado:
            print(f"{self.nome} já está acordado.")

        else:
            self.acordado = True

            print(f"{self.nome} acordou.")

    def comer(self):

        if self.comendo:
            print(f"{self.nome} já está comendo.")
        
        if self.dirigindo:
            print(f"{self.nome} nao pode comer enquanto dirige")
        
        if not self.acordado:
            print(f"{self.nome} nao pode comer enquanto dorme")

        else:
            self.comendo = True

            print(f"{self.nome} comecou a comer")
        
    def dirigir(self):

        if self.dirigindo:
            print(f"{self.nome} Ja esta dirigindo")
        
        if not self.acordado:
            print(f"{self.nome} nao pode dirigir enquanto dormindo")

        if self.comendo:
            print(f"{self.nome} nao pode dirigir enquanto comendo")
        
        else:
            self.dirigindo = True

            print(f"{self.nome} Esta dirigindo")
    
    def dormir(self):

        if self.dirigindo:
            print(f"{self.nome} nao pode dormir enquanto dirige")
        
        if self.comendo:
            print(f"{self.nome} nao pode dormir enquanto come")
        
        else:
            self.acordado = False
            print(f"{self.nome} dormiu")
    
    def parar_comer(self):
        
        if self.comendo:

            self.comendo = False
            print(f"{self.nome} parou de comer")
        else:
            print(f"{self.nome} Nao esta comendo")

    def parar_dirigir(self):
        
        if self.dirigindo:

            self.dirigindo = False
            print(f"{self.nome} parou de dirigir")
        else:
            print(f"{self.nome} Nao esta dirigindo")


nome = pessoa("Luan")

nome.acordar()

nome.comer()

nome.dirigir()

nome.parar_comer()

nome.dirigir()

nome.dormir()

nome.parar_comer()

nome.parar_dirigir()

nome.dormir()

nome.comer()