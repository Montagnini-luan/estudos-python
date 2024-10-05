from tkinter import messagebox
from tkinter import *


janela = Tk()

janela.geometry("950x400")

janela.title("Entry")

usuario = Label(text = "Usuario: ", font = "Arial 40")
usuario.grid(row=1, column=0, sticky="W")

compo_usuario = Entry(font="Arial 40")
compo_usuario.grid(row=1, column=1, sticky="W")

senha = Label(text = "Senha: ", font = "Arial 40")
senha.grid(row=2, column=0, sticky="W")

compo_senha = Entry(font="Arial 40", show="*")
compo_senha.grid(row=2, column=1, sticky="W")

def logar():
    nome =  str(compo_usuario.get())
    senha =  str(compo_senha.get())

    if nome == "luan" and senha == "888":
        messagebox.showinfo("Messagem", "Bem vindo(a) ao sistema!")

    else:
        messagebox.showinfo("Messagem", "Usuario ou senha invalidos!")

botao = Button(text="ENTRAR", font="Arieal 40",
               command=logar)

botao.grid(row=3, column=0, columnspan=2, sticky="NSEW")

janela.mainloop()
