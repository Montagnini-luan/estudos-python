import pyodbc
from tkinter import *
from tkinter import ttk

# Constantes (as mesmas usadas em pythonsql.py)
BG_COLOR = '#C0C0C0'
FONT = ('MS Sans Serif', 8)
TITLE_FONT = ('MS Sans Serif', 12, 'bold')
TITLE_BG = '#000080'
TITLE_FG = 'white'
BUTTON_STYLE = {
    'bg': BG_COLOR,
    'fg': 'black',
    'font': FONT,
    'relief': 'raised',
    'borderwidth': 1,
    'width': 10
}

def centralizar_janela(janela, largura, altura):
    pos_x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    pos_y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

def cadastrar_produto():
    janela_cadastro_produto = Toplevel(janela)
    janela_cadastro_produto.title('Cadastro de Produtos')
    janela_cadastro_produto.configure(bg=BG_COLOR)
    centralizar_janela(janela_cadastro_produto, 300, 250)

    frame_cadastro = Frame(janela_cadastro_produto, bg=BG_COLOR, relief='raised', borderwidth=1)
    frame_cadastro.place(relx=0.5, rely=0.5, anchor='center')
    
    Label(frame_cadastro, text='Cadastro de Produto', bg=TITLE_BG, fg=TITLE_FG, font=TITLE_FONT, padx=5, pady=2).grid(row=0, column=0, columnspan=2, sticky='ew', padx=1, pady=(1, 10))

    Label(frame_cadastro, text='Nome:', bg=BG_COLOR, font=FONT).grid(row=1, column=0, sticky='e', padx=(5, 2), pady=2)
    nome_produto_cadastrar = Entry(frame_cadastro, font=FONT, relief='sunken', borderwidth=1)
    nome_produto_cadastrar.grid(row=1, column=1, sticky='w', padx=(0, 5), pady=2)
    
    Label(frame_cadastro, text='Descrição:', bg=BG_COLOR, font=FONT).grid(row=2, column=0, sticky='e', padx=(5, 2), pady=2)
    descricao_produto_cadastrar = Entry(frame_cadastro, font=FONT, relief='sunken', borderwidth=1)
    descricao_produto_cadastrar.grid(row=2, column=1, sticky='w', padx=(0, 5), pady=2)
    
    Label(frame_cadastro, text='Preço:', bg=BG_COLOR, font=FONT).grid(row=3, column=0, sticky='e', padx=(5, 2), pady=2)
    preco_produto_cadastrar = Entry(frame_cadastro, font=FONT, relief='sunken', borderwidth=1)
    preco_produto_cadastrar.grid(row=3, column=1, sticky='w', padx=(0, 5), pady=2)

    Button(frame_cadastro, text='Cadastrar', command=lambda: print("Produto cadastrado"), **BUTTON_STYLE).grid(row=4, column=0, columnspan=2, pady=10)

janela = Tk()
janela.title('Sistema de Produtos')
janela.configure(bg=BG_COLOR)
janela.attributes('-fullscreen', True)

menu_barra = Menu(janela)
janela.config(menu=menu_barra)

menu_arquivo = Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label='Arquivo', menu=menu_arquivo)

menu_arquivo.add_command(label='Cadastrar Produto', command=cadastrar_produto)
menu_arquivo.add_command(label='Sair', command=janela.destroy)

janela.mainloop()
