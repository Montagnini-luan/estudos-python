from tkinter import *

janela = Tk()

janela.geometry("500x300")

janela.title("Radiobutton")

variavel1OpcaoSeleionada = StringVar(janela, "0")

def imprimirItemSelecionado():
    label_resultado.config(text="Voce selecionou a letra " + variavel1OpcaoSeleionada.get())

radio_button1 = Radiobutton(janela,
                           text="Letra A",
                           variable=variavel1OpcaoSeleionada,
                           font=30,
                           value="A",
                           command=imprimirItemSelecionado)
radio_button1.pack()

radio_button2 = Radiobutton(janela,
                           text="Letra B",
                           variable=variavel1OpcaoSeleionada,
                           font=30,
                           value="B",
                           command=imprimirItemSelecionado)
radio_button2.pack()

radio_button3 = Radiobutton(janela,
                           text="Letra C",
                           variable=variavel1OpcaoSeleionada,
                           font=30,
                           value="C",
                           command=imprimirItemSelecionado)
radio_button3.pack()


label_resultado = Label(janela, text="", font=30)
label_resultado.pack()




janela.mainloop()
