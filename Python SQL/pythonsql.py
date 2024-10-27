import pyodbc
from tkinter import *
from tkinter import ttk

# Constantes
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
    'width': 8
}

def criar_conexao():
    return pyodbc.connect('Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto_Compras.db')

def janela_menu():
    menu = Toplevel()
    menu.title('Menu Principal')
    menu.configure(bg=BG_COLOR)
    
    # Adicione aqui os elementos do menu principal
    Label(menu, text="Bem-vindo ao Sistema", bg=TITLE_BG, fg=TITLE_FG, font=TITLE_FONT).pack(fill=X, pady=(0, 10))
    
    Button(menu, text="Cadastrar Produto", **BUTTON_STYLE, command=lambda: print("Abrir janela de cadastro")).pack(pady=5)
    Button(menu, text="Listar Produtos", **BUTTON_STYLE, command=lambda: print("Abrir lista de produtos")).pack(pady=5)
    Button(menu, text="Sair", **BUTTON_STYLE, command=menu.destroy).pack(pady=5)

    centralizar_janela(menu, 300, 200)

def verificar_login():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    
    cursor.execute('SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ?', 
                   (nome_usuario_entry.get(), senha_usuario_entry.get()))

    if cursor.fetchone():
        janela_principal.withdraw()  # Esconde a janela de login
        janela_menu()
    else:
        mostrar_erro("Nome de usuário ou senha inválidos!")

    cursor.close()
    conexao.close()

def mostrar_erro(mensagem):
    erro_label = Label(frame_login, text=mensagem, bg=BG_COLOR, fg='red', font=FONT)
    erro_label.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)
    janela_principal.after(3000, erro_label.destroy)  # Remove a mensagem após 3 segundos

def centralizar_janela(janela, largura, altura):
    pos_x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    pos_y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

# Configuração da janela principal
janela_principal = Tk()
janela_principal.title('Login do Sistema')
janela_principal.configure(bg=BG_COLOR)
centralizar_janela(janela_principal, 300, 200)

# Frame de login
frame_login = Frame(janela_principal, bg=BG_COLOR, relief='raised', borderwidth=1)
frame_login.place(relx=0.5, rely=0.5, anchor='center')

# Título
Label(frame_login, text='Sistema de Login', bg=TITLE_BG, fg=TITLE_FG, font=TITLE_FONT, padx=5, pady=2).grid(row=0, column=0, columnspan=2, sticky='ew', padx=1, pady=(1, 10))

# Campos de entrada
Label(frame_login, text='Usuário:', bg=BG_COLOR, font=FONT).grid(row=1, column=0, sticky='e', padx=(5, 2), pady=2)
Label(frame_login, text='Senha:', bg=BG_COLOR, font=FONT).grid(row=2, column=0, sticky='e', padx=(5, 2), pady=2)

nome_usuario_entry = Entry(frame_login, font=FONT, relief='sunken', borderwidth=1)
nome_usuario_entry.grid(row=1, column=1, sticky='w', padx=(0, 5), pady=2)

senha_usuario_entry = Entry(frame_login, show='*', font=FONT, relief='sunken', borderwidth=1)
senha_usuario_entry.grid(row=2, column=1, sticky='w', padx=(0, 5), pady=2)

# Botões
botoes_frame = Frame(frame_login, bg=BG_COLOR)
botoes_frame.grid(row=4, column=0, columnspan=2, pady=10)

Button(botoes_frame, text='Entrar', command=verificar_login, **BUTTON_STYLE).pack(side=LEFT, padx=2)
Button(botoes_frame, text='Sair', command=janela_principal.quit, **BUTTON_STYLE).pack(side=LEFT, padx=2)

janela_principal.mainloop()
