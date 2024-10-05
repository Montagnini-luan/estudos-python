from tkinter import *

janela = Tk()

janela.geometry("950x400")

janela.title("Checkbutton")

informacao = Label(janela, text="Selecione a opcao desejada",
                   fg="blue", font="Arial 20")

def azulClicado():
    print(varAzul.get())

def amareloClicado():
    print(varAmarelo.get())

def verdeClicado():
    print(varVerde.get())

varAzul = StringVar()
varAmarelo = StringVar()
varVerde = StringVar()

check_azul = Checkbutton(janela, text="azul",
                         variable= varAzul,
                         onvalue="Clicou na cor azul",
                         font="Arial 20",
                         offvalue="",
                         height=2,
                         width=10,
                         command=azulClicado)

check_amarelo = Checkbutton(janela, text="amarelo",
                         variable= varAmarelo,
                         onvalue="Clicou na cor amarelo",
                         font="Arial 20",
                         offvalue="",
                         height=2,
                         width=10,
                         command=amareloClicado)

check_verde = Checkbutton(janela, text="verde",
                         variable= varVerde,
                         onvalue="Clicou na cor verde",
                         font="Arial 20",
                         offvalue="",
                         height=2,
                         width=10,
                         command=verdeClicado)


informacao.pack()

check_azul.pack()
check_amarelo.pack()
check_verde.pack()

janela.mainloop()
