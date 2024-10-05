from tkinter import *
import tkinter
from PIL import ImageTk, Image

janela = Tk()

janela.geometry("460x260")

janela.title('Botao')

Label(janela, text = "Imagem",
      font= ("Verdana", 15)).pack()

imagem = ImageTk.PhotoImage(Image.open('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\SAIR.jpg'))

botao_img = Button(image = imagem, command = janela.destroy)

botao_img.pack()

imagem_fundo = ImageTk.PhotoImage(Image.open('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\plano_fundo.png'))

Label_fundo = Label(image=imagem_fundo)
Label_fundo.place(x=0, y=0)

rotulo1 = Label(janela, text = "Python", relief=FLAT, bg="green", fg="white")
rotulo2 = Label(janela, text = "Python", relief=FLAT, bg="black", fg="white", width=50)
rotulo3 = Label(janela, text = "Python", relief=FLAT, bg="yellow", fg="black", width=50)

rotulo1.pack()
rotulo2.pack()
rotulo3.pack()



janela.mainloop()
