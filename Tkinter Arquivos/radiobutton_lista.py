from tkinter import *

janela = Tk()

janela.geometry("500x300")

janela.title("Radiobutton")

variavel1OpcaoSeleionada = StringVar(janela, "0")

def imprimirItemSelecionado():
    label_resultado.config(text="Voce selecionou a letra " + variavel1OpcaoSeleionada.get())

lista_nomes = {"Letra A": "A",
          "Letra B": "B",
          "Letra C": "C",
          "Letra D": "D",
          "Letra E": "E",
          "Letra F": "F",
          "Letra G": "G",
          "Letra H": "H",
          "Letra I": "I"
}

for (texto_coluna_0, texto_coluna_1) in lista_nomes.items():
    Radiobutton(janela,
                text=texto_coluna_0,
                variable=variavel1OpcaoSeleionada,
                value=texto_coluna_1,
                font=30,
                command=imprimirItemSelecionado
    ).pack()

label_resultado = Label(janela, text="", font=30)
label_resultado.pack()




janela.mainloop()
