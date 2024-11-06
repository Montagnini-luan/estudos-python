
class OlaMundo:
    def __init__(self):
        self.mensagem = "Olá Mundo!"

    def exibir_mensagem(self):
        print(self.mensagem)

def main():
    ola_mundo = OlaMundo()
    ola_mundo.exibir_mensagem()

if __name__ == "__main__":
    main()
