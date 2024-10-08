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
        messagebox.showwarning('Entrada invalida', 'Por favor, insira um numero valido para a qauntidade de digitos.')
        return

    incluir_maiusculas = var_maiusculas.get()
    incluir_minusculas = var_minusculas.get()
    incluir_numeros = var_numeros.get()
    incluir_especiais = var_especiais.get()

    if not (incluir_maiusculas or incluir_minusculas or incluir_numeros or incluir_especiais):
        messagebox.showwarning('Opcao invalida', 'Selecione pelo menos uma opcao')

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

    if len(caracteres) == 0:
        messagebox.showwarning('Opcao invalida', 'Selescione pelo menos uma opcao de caracteres.')
        return
    
    while len(senha) < comprimento:
        senha.append(random.choice(caracteres))
    random.shuffle(senha)

    senha = ''.join(senha[:comprimento])

    entrada_senha.delete(0, tk.END)
    entrada_senha.insert(0, senha)

janela = tk.Tk()

janela.title('Gerador de senhas')

janela.configure(bg="white")

largura_janela = 400
altura_janela = 400
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicao_x = (largura_tela // 2) - (largura_janela // 2)
posicao_y = (altura_tela // 2) - (altura_janela // 2)

janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

frame_opcoes = tk.LabelFrame(janela,
                             text='Opcoes de caracteres',
                             padx=10,
                             pady=10,
                             bg='white')

frame_opcoes.pack(pady=20, padx=20, fill='both', expand='yes')

var_maiusculas = tk.BooleanVar()
var_minusculas = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_especiais = tk.BooleanVar()

check_maiusculas = tk.Checkbutton(frame_opcoes,
                                      text='Incluir Letras Maiusculas',
                                      variable=var_maiusculas,
                                      bg='white')

check_maiusculas.grid(row=0, column=2, stick='W')

check_minusculas = tk.Checkbutton(frame_opcoes,
                                      text='Incluir Letras Minusculas',
                                      variable=var_minusculas,
                                      bg='white')

check_minusculas.grid(row=1, column=2, stick='W')

check_numeros = tk.Checkbutton(frame_opcoes,
                                      text='Incluir Numeros',
                                      variable=var_numeros,
                                      bg='white')

check_numeros.grid(row=2, column=2, stick='W')

check_especiais = tk.Checkbutton(frame_opcoes,
                                      text='Incluir Caracteres Especias',
                                      variable=var_especiais,
                                      bg='white')

check_especiais.grid(row=3, column=2, stick='W')

frame_comprimento = tk.Frame(janela, bg='white')

frame_comprimento.pack(pady=10)

label_comprimento = tk.Label(frame_comprimento,
                             text='Quantidade de Digitos:',
                             bg='white')

label_comprimento.pack(side='left', padx=5)

entrada_comprimento = tk.Entry(frame_comprimento, width=5)

entrada_comprimento.pack(side='left', padx=5)

botao_gerar = tk.Button(janela,
                        text='Gerar Senha',
                        command=gerar_senha)

botao_gerar.pack(pady=20)

frame_senha = tk.Frame(janela, bg='white')

frame_senha.pack(pady=10)

label_senha = tk.Label(frame_senha,
                       text='Senha Gerada',
                       bg='white')

label_senha.pack(side='left', padx=5)

entrada_senha = tk.Entry(frame_senha,
                         width=50,
                         font=('Helvetica', 14))

entrada_senha.pack(side='left', padx=5)

janela.mainloop()
