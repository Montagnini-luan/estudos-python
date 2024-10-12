import tkinter as tk

class ScrollerTexto:
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal
        self.janela_principal.title('Scroller de texto interativo')
        self.largura = 800
        self.altura = 100
        self.tela = tk.Canvas(janela_principal, width=self.largura, height=self.altura, bg='black')
        self.tela.pack()
        self.texto = 'Esse e um exemplo de scroller de texto utilizando Python e Tkinter...'
        self.texto_id =  self.tela.create_text(self.largura, 50, text=self.texto, font=('Helvetica', 50), fill='white', anchor='w')
        self.velocidade = -2
        self.animando = True
        self.tela.bind("<Enter>", self.parar_animacao)
        self.tela.bind("<Leave>", self.retomar_animcao)
        self.mover_texto()

    def mover_texto(self):
        if self.animando:
            self.tela.move(self.texto_id, self.velocidade, 0)
            pos_x = self.tela.bbox(self.texto_id)[2]

            if pos_x < 0:
                self.tela.coords(self.texto_id, self.largura, 50)

        self.janela_principal.after(50, self.mover_texto)

    def parar_animacao(self, event):
        self.animando = False

    def retomar_animcao(self, event):
        self.animando = True


if __name__ == '__main__':
    janela_principal = tk.Tk()
    aplicacao = ScrollerTexto(janela_principal)
    janela_principal.mainloop()
