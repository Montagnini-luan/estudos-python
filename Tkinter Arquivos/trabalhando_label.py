
from tkinter import *

janela = Tk()

janela.title("Interface Grafica")

instrucao = Label(text='Bem vindos ao curso de Tkinter')  #escrevendo o texto para o usuario
instrucao.pack()  #coloca o objeto dentro da janela

rotulo1 = Label(janela, text= "Flat", relief=FLAT, bg="orange", fg="black", font="Times 12")
rotulo1.pack()

rotulo2 = Label(janela, text= "raised", relief=RAISED)
rotulo2.pack()

rotulo3 = Label(janela, text= "Sunken", relief=SUNKEN)
rotulo3.pack()

rotulo4 = Label(janela, text= "Groove", relief=GROOVE, borderwidth=10, bg="red", fg="white")
rotulo4.pack()

rotulo5 = Label(janela, text= "RIDGE", relief=RIDGE)
rotulo5.pack()

janela.mainloop()
