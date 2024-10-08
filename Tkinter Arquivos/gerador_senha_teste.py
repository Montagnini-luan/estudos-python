import tkinter as tk
from tkinter import messagebox
import http.client
import json
import string
import random
from PIL import Image, ImageTk

def gerar_senha():
    try:
        comprimento = int(entrada_comprimento.get())
    except ValueError:
        messagebox.showwarning('Entrada inválida', 'Por favor, insira um número válido para a quantidade de dígitos.')
        return
    
    incluir_maiusculas = var_maiusculas.get()
    incluir_minusculas = var_minusculas.get()
    incluir_numeros = var_numeros.get()
    incluir_especiais = var_especiais.get()
    
    if not (incluir_maiusculas or incluir_minusculas or incluir_numeros or incluir_especiais):
        messagebox.showwarning('Opção inválida', 'Selecione pelo menos uma opção')
        return
    
    caracteres = ''
    senha = []
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
        senha.append(random.choice(string.ascii_uppercase))
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
        senha.append(random.choice(string.ascii_lowercase))
    if incluir_numeros:
        caracteres += string.digits
        senha.append(random.choice(string.digits))
    if incluir_especiais:
        caracteres += string.punctuation
        senha.append(random.choice(string.punctuation))
    
    while len(senha) < comprimento:
        senha.append(random.choice(caracteres))
    
    random.shuffle(senha)
    senha = ''.join(senha[:comprimento])
    
    
    # Exibir a senha na interface
    lblSenha.config(text=f"Senha: {senha}")

def atualizar_imagem():
    if var_especiais.get():
        image_path = "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\R.jfif"
        image = Image.open(image_path)
        image = image.resize((100, 100), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label_imagem.config(image=photo)
        label_imagem.image = photo
    else:
        label_imagem.config(image='')


# Configuração da janela principal
janela = tk.Tk()
janela.title('Gerador de Senhas')
janela.configure(bg="white")

largura_janela = 400
altura_janela = 500
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = (largura_tela // 2) - (largura_janela // 2)
posicao_y = (altura_tela // 2) - (altura_janela // 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

# Configuração dos frames e widgets
frame_opcoes = tk.LabelFrame(janela, text='Opções de caracteres', padx=10, pady=10, bg='white')
frame_opcoes.pack(pady=20, padx=20, fill='both', expand='yes')

var_maiusculas = tk.BooleanVar()
var_minusculas = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_especiais = tk.BooleanVar()

check_maiusculas = tk.Checkbutton(frame_opcoes, text='Incluir Letras Maiúsculas', variable=var_maiusculas, bg='white')
check_maiusculas.grid(row=0, column=0, sticky='W')

check_minusculas = tk.Checkbutton(frame_opcoes, text='Incluir Letras Minúsculas', variable=var_minusculas, bg='white')
check_minusculas.grid(row=1, column=0, sticky='W')

check_numeros = tk.Checkbutton(frame_opcoes, text='Incluir Números', variable=var_numeros, bg='white')
check_numeros.grid(row=2, column=0, sticky='W')

check_especiais = tk.Checkbutton(frame_opcoes, text='Incluir Especial', variable=var_especiais, bg='white', command=atualizar_imagem)
check_especiais.grid(row=3, column=0, sticky='W')

frame_comprimento = tk.Frame(janela, bg='white')
frame_comprimento.pack(pady=10)

label_comprimento = tk.Label(frame_comprimento, text='Quantidade de Dígitos:', bg='white')
label_comprimento.pack(side='left', padx=5)

entrada_comprimento = tk.Entry(frame_comprimento, width=5)
entrada_comprimento.pack(side='left', padx=5)

botao_gerar = tk.Button(janela, text='Gerar Senha', command=gerar_senha)
botao_gerar.pack(pady=10)

lblSenha = tk.Label(janela, text="Senha: ", font="Arial 20", bg="white")
lblSenha.pack(pady=10)

label_imagem = tk.Label(janela, bg="white")
label_imagem.pack(pady=10)

janela.mainloop()



