from tkinter import *
from tkinter import messagebox

janela = Tk()

janela.title('Botao')

def exibirMensagemBox():
    messagebox.showinfo("Mensagem", "Ola mundo")

def exibirMensagem():
    print("Ola mundo!")

botao1 = Button(janela, 
                text = 'Enviar', 
                command=exibirMensagem, 
                bg="black", 
                fg="white",
                height=10, 
                width=50)

botao2 = Button(janela, 
                text = 'Enviar box', 
                command=exibirMensagemBox, 
                width=50,
                height=10)

botaoSair = Button(janela, 
                   text = 'Sair carai', 
                   command=janela.destroy, 
                   width=50,
                   height=10,
                   bg="red", 
                   fg="white")

botao1.pack(side="left")
botao2.pack(side="left")
botaoSair.pack(side="left")


janela.mainloop()
