import tkinter as tk
from tkinter import ttk
import pandas as pd

def sincronizar_rolagem(*args):
    """Sincroniza a rolagem vertical entre as duas tabelas."""
    tabela.yview(*args)
    tabela_congelada.yview(*args)

def criar_interface():
    janela = tk.Tk()
    janela.title('Projeto de Notas de Estudantes')
    janela.geometry('800x600')

    label_titulo = tk.Label(janela, text='Notas dos Estudantes', font=('Arial', 16))
    label_titulo.pack(pady=10)

    frame_principal = tk.Frame(janela)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    # Frame da tabela congelada (primeira coluna)
    frame_congelado = tk.Frame(frame_principal)
    frame_congelado.pack(side=tk.LEFT, fill=tk.Y)

    # Frame da tabela rolável (demais colunas)
    frame_tabela = tk.Frame(frame_principal)
    frame_tabela.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Coluna congelada
    colunas_congeladas = [df.columns[0]]

    global tabela_congelada
    tabela_congelada = ttk.Treeview(frame_congelado, columns=colunas_congeladas, show='headings', height=20)
    tabela_congelada.pack(side=tk.LEFT, fill=tk.Y)

    for coluna in colunas_congeladas:
        tabela_congelada.heading(coluna, text=coluna)
        tabela_congelada.column(coluna, width=120, anchor='center')

    # Adicionar os dados na coluna congelada
    for indice, linha in df.iterrows():
        tabela_congelada.insert('', tk.END, values=(linha[coluna],))

    # Barra de rolagem vertical compartilhada
    scroll_vertical = ttk.Scrollbar(frame_tabela, orient='vertical', command=sincronizar_rolagem)
    scroll_vertical.pack(side=tk.RIGHT, fill=tk.Y)

    # Tabela com as colunas roláveis
    colunas_tabela = list(df.columns[1:])

    global tabela
    tabela = ttk.Treeview(frame_tabela, columns=colunas_tabela, show='headings', height=20)
    tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    for coluna in colunas_tabela:
        tabela.heading(coluna, text=coluna)
        tabela.column(coluna, width=100, anchor='center')  # Ajustar a largura da coluna

    # Adicionar os dados nas colunas roláveis
    for indice, linha in df.iterrows():
        valores = tuple(linha[coluna] for coluna in colunas_tabela)
        tabela.insert('', tk.END, values=valores)

    # Sincronizar a rolagem vertical entre as duas tabelas
    tabela.configure(yscrollcommand=scroll_vertical.set)
    tabela_congelada.configure(yscrollcommand=scroll_vertical.set)

    # Barra de rolagem horizontal para a tabela
    scrollbar_horizontal = ttk.Scrollbar(janela, orient='horizontal', command=tabela.xview)
    scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
    tabela.configure(xscrollcommand=scrollbar_horizontal.set)

    janela.mainloop()

# Carregar o arquivo Excel e criar a interface
arquivo_excel = "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\notas_estudantes (3).xlsx"
df = pd.read_excel(arquivo_excel, sheet_name='Dados')
criar_interface()
