import tkinter as tk
from tkinter import filedialog
import pandas as pd

def carregar_dados():
    global df_original

    # Carregar os dados do arquivo Excel
    df_original = pd.read_excel(
        'C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\tabela_exemplo.xlsx',
        sheet_name='Planilha1'
    )

    aplicar_filtro()  # Chamar para exibir os dados ao carregar

def aplicar_filtro():
    global df_filtrado

    termo = entrada_filtro.get().lower()

    # Filtrar dados com base em cada célula da linha
    df_filtrado = df_original[df_original.apply(
        lambda row: row.astype(str).str.contains(termo, case=False).any(), axis=1)]

    exibir_pagina()  # Atualizar a tabela com os dados filtrados

def destacar_celula(event):
    widget = event.widget
    widget.configure(bg='yellow', font=('Arial', 14, 'bold'))

def restaurar_celula(event):
    widget = event.widget
    widget.configure(bg='white', font=('Arial', 10))

def exibir_pagina():
    # Limpar o frame antes de exibir os dados
    for widget in frame_tree.winfo_children():
        widget.destroy()

    # Exibir cabeçalhos das colunas
    for j, col in enumerate(df_filtrado.columns):
        header = tk.Label(frame_tree, text=col, font=('Arial', 12, 'bold'), borderwidth=1, relief='solid', bg='lightblue')
        header.grid(row=0, column=j, sticky='nsew')

    # Exibir dados da tabela
    for i, row in enumerate(df_filtrado.itertuples(), start=1):
        for j, value in enumerate(row[1:]):  # row[1:] para ignorar o índice do `itertuples`
            cell = tk.Label(frame_tree, text=value, font=('Arial', 10), borderwidth=1, relief='solid', padx=3, pady=3, background='white')
            cell.grid(row=i, column=j, sticky='nsew')

            # Adicionar os binds para destacar/restaurar a célula
            cell.bind('<Enter>', destacar_celula)
            cell.bind('<Leave>', restaurar_celula)

    # Ajustar as colunas e linhas para expandir conforme a janela
    for j in range(len(df_filtrado.columns)):
        frame_tree.grid_columnconfigure(j, weight=1)

    for i in range(len(df_filtrado) + 1):  # +1 para incluir os cabeçalhos
        frame_tree.grid_rowconfigure(i, weight=1)

def exportar_dados_filtrados():
    # Exportar os dados filtrados para um arquivo Excel
    arquivo = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel Files', '*.xlsx')])
    if arquivo:
        df_filtrado.to_excel(arquivo, index=False)

# Configuração da Janela Principal
janela = tk.Tk()
janela.title('Tabela Interativa com Dados de Excel')
janela.geometry('720x600')

# Título da janela
titulo = tk.Label(janela, text='Tabela de Informações', font=('Arial', 18, 'bold'))
titulo.pack(fill='x', padx=20)

# Frame do Filtro
frame_filtro = tk.Frame(janela, bg='#f8f9fa')
frame_filtro.pack(pady=10, fill='x')

# Entrada para o termo de filtro
entrada_filtro = tk.Entry(frame_filtro, font=('Arial', 12))
entrada_filtro.pack(side='left', padx=10, fill='x', expand=True)
entrada_filtro.bind('<KeyRelease>', lambda event: aplicar_filtro())

# Botão para exportar os dados
btn_exportar = tk.Button(frame_filtro, text='Exportar Dados Filtrados', command=exportar_dados_filtrados, bg='#f8f9fa', fg='black', font=('Arial', 12, 'bold'))
btn_exportar.pack(side='right', padx=10)

# Frame para exibir os dados
frame_tree = tk.Frame(janela)
frame_tree.pack(expand=True, fill='both')

# Carregar os dados inicialmente
carregar_dados()

# Iniciar o loop da janela
janela.mainloop()
