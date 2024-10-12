import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw

class AplicacaoEfeitoRevelacao:
    def __init__(self, janela_principal, caminho_imagem_inferior, caminho_imagem_superior):
        self.janela_principal = janela_principal
        self.janela_principal.title('Efeito Revelação Dinâmica')
        
        try:
            self.imagem_inferior = Image.open(caminho_imagem_inferior)
            self.imagem_superior = Image.open(caminho_imagem_superior)
            self.imagem_superior = self.imagem_superior.resize(self.imagem_inferior.size, Image.Resampling.LANCZOS)
            
            self.tela = tk.Canvas(janela_principal, width=self.imagem_inferior.width, height=self.imagem_inferior.height)
            self.tela.pack()
            
            self.tk_imagem_inferior = ImageTk.PhotoImage(self.imagem_inferior)
            self.tk_imagem_superior = ImageTk.PhotoImage(self.imagem_superior)
            self.tela.create_image(0, 0, image=self.tk_imagem_inferior, anchor='nw')
            self.tela.bind('<Motion>', self.movimento_mouse)
            
            messagebox.showinfo('Inicialização Completa', 'Passe o mouse sobre a janela para ver o efeito')
        
        except Exception as erro:
            messagebox.showerror('Erro', f'Erro ao inicializar a aplicação: {erro}')

    def movimento_mouse(self, evento):
        x, y = evento.x, evento.y
        mascara = Image.new('L', self.imagem_inferior.size, 0)
        ImageDraw.Draw(mascara).ellipse((x - 50, y - 50, x + 50, y + 50), fill=255)
        
        imagem_com_mascara = Image.composite(self.imagem_superior, self.imagem_inferior, mascara)
        self.tk_imagem_com_mascara = ImageTk.PhotoImage(imagem_com_mascara)
        
        self.tela.create_image(0, 0, image=self.tk_imagem_com_mascara, anchor='nw')

if __name__ == '__main__':
    janela_principal = tk.Tk()
    aplicacao = AplicacaoEfeitoRevelacao(
        janela_principal,
        'C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\imagem-inferior.jpg',
        'C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\imagem-superior.jpg'
    )
    janela_principal.mainloop()
