import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import os
import random

def carregar_dados():
    global dados, max_colunas
    
    dados = pd.read_excel('Jogos.xlsx', sheet_name='Jogos')
    max_colunas = dados.notna().sum(axis=1).max()
    criar_cabecalhos(max_colunas)

    for i, linha in dados.iterrows():
        criar_linha_tabela(list(linha), i, max_colunas)

def criar_cabecalhos(max_colunas):
    cabecalhos = [f'Número {i+1}' for i in range(max_colunas)] + ['Acertos', '']

    for col, cabecalho in enumerate(cabecalhos):
        lbl = tk.Label(frame_rolavel, text=cabecalho, borderwidth=2, relief="solid", width=10)
        lbl.grid(row=0, column=col, sticky='nsew')

def criar_linha_tabela(valores, linha, max_colunas):
    indice_coluna = 0  # Índice da coluna 

    for val in valores:
        if pd.notna(val):
            lbl = tk.Label(frame_rolavel, text=str(int(val)), borderwidth=1, relief="solid", width=10)
            lbl.grid(row=linha+1, column=indice_coluna, sticky='nsew')
            tabela_labels[linha][indice_coluna] = lbl
            indice_coluna += 1

    for _ in range(indice_coluna, max_colunas):
        lbl = tk.Label(frame_rolavel, text="", borderwidth=1, relief="solid", width=10)
        lbl.grid(row=linha+1, column=indice_coluna, sticky='nsew')
        tabela_labels[linha][indice_coluna] = lbl
        indice_coluna += 1
        
    lbl_acertos = tk.Label(frame_rolavel, text="", borderwidth=1, relief="solid", width=15)
    lbl_acertos.grid(row=linha+1, column=indice_coluna, sticky='nsew')
    tabela_labels[linha][indice_coluna] = lbl_acertos
    btn_excluir = tk.Button(frame_rolavel, text="Excluir", command=lambda r=linha: excluir_jogo(r))
    btn_excluir.grid(row=linha+1, column=indice_coluna+1, sticky='nsew')
    tabela_labels[linha][indice_coluna+1] = btn_excluir

def excluir_jogo(linha):
    global dados
    
    dados = dados.drop(linha).reset_index(drop=True)
    dados.to_excel('Jogos.xlsx', sheet_name='Jogos', index=False)
    atualizar_tela()

def atualizar_tela():
    for widget in frame_rolavel.winfo_children():
        widget.destroy()
        
    carregar_dados()

def gerar_surpresinha():
    janela_surpresinha = tk.Toplevel(janela_principal)
    janela_surpresinha.title("Gerar Surpresinha")
    janela_surpresinha.configure(background='white')
    centralizar_janela(janela_surpresinha, 800, 400)
    frame_surpresinha = tk.Frame(janela_surpresinha, bg='white')
    frame_surpresinha.pack(pady=20)
    fonte = ("Arial", 20)
    janela_surpresinha.grid_columnconfigure(0, weight=1)
    janela_surpresinha.grid_columnconfigure(2, weight=1)
    janela_surpresinha.grid_rowconfigure(0, weight=1)
    janela_surpresinha.grid_rowconfigure(2, weight=1)
    tk.Label(frame_surpresinha, text="Escolha a quantidade de números:", font=fonte, bg='white', anchor='center').grid(row=0, column=1, pady=10, sticky='ew')
    entrada_quantidade = tk.Entry(frame_surpresinha, width=5, font=fonte, justify='center')
    entrada_quantidade.grid(row=1, column=1, pady=5, sticky='ew')

    def criar_surpresinha():
        num_numeros = int(entrada_quantidade.get())
        
        if 6 <= num_numeros <= 20:
            numeros_aleatorios = sorted(random.sample(range(1, 61), num_numeros))
            exibir_jogo_aleatorio(janela_surpresinha, numeros_aleatorios, num_numeros)
            
        else:
            tk.Label(frame_surpresinha, 
                     text="Por favor, insira um número entre 6 e 20.", 
                     font=fonte, bg='white', anchor='center').grid(row=2, column=1, pady=5, sticky='ew')

    botao_criar = tk.Button(frame_surpresinha, 
                            text="Criar", 
                            command=criar_surpresinha, 
                            font=fonte, bg='white')

    botao_criar.grid(row=3, column=1, pady=10, sticky='ew')

def exibir_jogo_aleatorio(janela_surpresinha, numeros_aleatorios, num_numeros):
    for widget in janela_surpresinha.winfo_children():
        widget.destroy()
        
    janela_surpresinha.configure(background='white')
    frame_resultado = tk.Frame(janela_surpresinha, bg='white')
    frame_resultado.pack(pady=20)
    fonte = ("Arial", 20)
    janela_surpresinha.grid_columnconfigure(0, weight=1)
    janela_surpresinha.grid_columnconfigure(2, weight=1)
    janela_surpresinha.grid_rowconfigure(0, weight=1)
    janela_surpresinha.grid_rowconfigure(2, weight=1)
    frame_resultado.grid(row=1, column=1)
    tk.Label(frame_resultado, 
             text=f"Jogo Aleatório ({num_numeros} números):", 
             font=fonte, bg='white', anchor='center').grid(row=0, column=1, pady=10, sticky='ew')

    tk.Label(frame_resultado, 
             text=" ".join(map(str, numeros_aleatorios)), 
             font=fonte, bg='white', anchor='center').grid(row=1, column=1, pady=5, sticky='ew')

    def salvar_jogo():
        adicionar_jogo(numeros_aleatorios)
        janela_surpresinha.destroy()
        
        atualizar_tela()

    botao_salvar = tk.Button(frame_resultado, 
                             text="Salvar Jogo", 
                             command=salvar_jogo, 
                             font=fonte, bg='white')
    botao_salvar.grid(row=2, column=1, pady=5, sticky='ew')

    botao_cancelar = tk.Button(frame_resultado, 
                               text="Cancelar", 
                               command=janela_surpresinha.destroy, 
                               font=fonte, bg='white')
    botao_cancelar.grid(row=3, column=1, pady=5, sticky='ew')

def adicionar_jogo(numeros_aleatorios):
    global dados, max_colunas

    nova_linha = pd.Series(numeros_aleatorios + [None]*(len(dados.columns) - len(numeros_aleatorios)), index=dados.columns)
    dados = pd.concat([dados, nova_linha.to_frame().T], ignore_index=True)
    dados.to_excel('Jogos.xlsx', sheet_name='Jogos', index=False)
    linha = dados.shape[0] - 1
    criar_linha_tabela(numeros_aleatorios + [None]*(max_colunas - len(numeros_aleatorios)), linha, max_colunas)

def conferir_numeros():
    numeros_entrada = [int(entrada.get()) for entrada in entradas]

    for linha, valores in enumerate(dados.values):
        valores_int = [int(float(val)) for val in valores if not pd.isna(val)]
        acertos = len(set(numeros_entrada).intersection(valores_int))
        lbl_acertos = tabela_labels[linha][max_colunas]
        lbl_acertos.config(text=f"Acertou {acertos}")
        
        for coluna in range(len(valores_int)):
            tabela_labels[linha][coluna].config(bg="white", fg="black")

        for coluna, val in enumerate(valores_int):
            if val in numeros_entrada:
                tabela_labels[linha][coluna].config(bg="blue", fg="white")

        if acertos >= 4:
            lbl_acertos.config(bg="green", fg="white")
            
        else:
            lbl_acertos.config(bg="white", fg="black")

def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

janela_principal = tk.Tk()
janela_principal.title("Conferidor de Jogos da Mega Sena")
janela_principal.geometry("1200x700")
janela_principal.resizable(False, False)
centralizar_janela(janela_principal, 1200, 550)
image_path = "mega-sena.jpg"

if os.path.exists(image_path):
    img = Image.open(image_path)
    img = img.resize((1200, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    label_imagem = tk.Label(janela_principal, image=photo)
    label_imagem.image = photo
    label_imagem.pack(pady=10)
    
else:
    print(f"Erro: o arquivo {image_path} não foi encontrado.")

titulo = tk.Label(janela_principal, 
                  text="Conferidor de Jogos da Mega Sena", 
                  font=("Arial", 16))

titulo.pack(pady=10)
frame_entradas = tk.Frame(janela_principal)
frame_entradas.pack(pady=10)

entradas = []
labels = []

for i in range(6):
    label = tk.Label(frame_entradas, text=f"Número {i+1}:")
    label.grid(row=0, column=i*2, padx=5)
    labels.append(label)
    entrada = tk.Entry(frame_entradas, width=5)
    entrada.grid(row=0, column=i*2+1, padx=5)
    entradas.append(entrada)

botao_conferir = tk.Button(frame_entradas, 
                           text="Conferir", 
                           command=conferir_numeros)

botao_conferir.grid(row=0, column=12, padx=5)

botao_surpresinha = tk.Button(frame_entradas, 
                              text="Surpresinha", 
                              command=gerar_surpresinha)

botao_surpresinha.grid(row=0, column=13, padx=5)
frame_tabela = tk.Frame(janela_principal)
frame_tabela.pack(pady=10, fill=tk.BOTH, expand=True)
canvas = tk.Canvas(frame_tabela)
scrollbar_x = tk.Scrollbar(frame_tabela, 
                           orient="horizontal", 
                           command=canvas.xview)
scrollbar_y = tk.Scrollbar(frame_tabela, 
                           orient="vertical", 
                           command=canvas.yview)
frame_rolavel = tk.Frame(canvas)
frame_rolavel.bind(
    "<Configure>",  # Evento de configuração/redimensionamento do frame rolável

    lambda e: canvas.configure(

        scrollregion=canvas.bbox("all")
        
    )
)

canvas.create_window((0, 0), 
                     window=frame_rolavel, 
                     anchor="nw")

canvas.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

canvas.grid(row=0, column=0, sticky="nsew")

scrollbar_x.grid(row=1, column=0, sticky="ew")

scrollbar_y.grid(row=0, column=1, sticky="ns")


frame_tabela.grid_rowconfigure(0, weight=1)

frame_tabela.grid_columnconfigure(0, weight=1)

tabela_labels = {}

for linha in range(100):  # Supondo um máximo de 100 linhas para os dados
    tabela_labels[linha] = {}


carregar_dados()

janela_principal.mainloop()