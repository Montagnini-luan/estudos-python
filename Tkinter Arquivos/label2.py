from tkinter import *

janela = Tk()

texto = """Curso de Tkinter
Aprendendo como criar
interface grafica com
python
"""

#formato = Label(janela,
#                font="Arial 40 bold",
#                text= texto).pack()

janela.title("Tela 3 x 3")

for linha in range(5):
    for coluna in range(3):
        tabela = Frame(
            master = janela,
            relief = RAISED,
            borderwidth = 1
        )
        tabela.grid(row=linha, column=coluna, padx=50, pady=50)
        label = Label(master=tabela, text=f"Linha{linha}\n Coluna {coluna}")
        label.pack()

janela.mainloop()