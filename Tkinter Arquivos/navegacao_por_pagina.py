import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd


def exportar_dados_filtrados():
    arquivo = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel Files', '*.xlsx')])
    if arquivo:
        df_filtrado.to_excel(arquivo, index=False)

def calcular_media_situacao(df):
    df['Media'] = df[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].mean(axis=1).round(2)

    def definir_situacao(linha):
        if linha['Faltas'] > 10:
            return 'Reprovado por Faltas'
        elif linha['Media'] >= 7:
            return 'Aprovado'
        elif linha['Media'] < 2:
            return 'Reprovado por Notas'
        else:
            return 'Recuperacao'
        
    df['Situacao'] = df.apply(definir_situacao, axis=1)
    return df


def carregar_dados():
    global df_original, num_paginas, pagina_atual

    df_original = pd.read_excel(
        'C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\notas_estudantes.xlsx',
        sheet_name='Dados'
    )

    df_original = calcular_media_situacao(df_original)

    aplicar_filtro()


def aplicar_filtro():
    global df_filtrado, num_paginas, pagina_atual

    termo = entrada_filtro.get().lower()
    df_filtrado = df_original[df_original.apply(lambda row: termo in row.to_string(index=False).lower(), axis=1)]

    num_paginas = (len(df_filtrado) // 5) + (1 if len(df_filtrado) % 5 != 0 else 0)

    pagina_atual = 1

    exibir_pagina()


def exibir_pagina():
    inicio_idx = (pagina_atual - 1) * 5
    fim_idx = inicio_idx + 5

    df_pagina = df_filtrado.iloc[inicio_idx:fim_idx]

    for widget in frame_tree.winfo_children():
        widget.destroy()

    tree = ttk.Treeview(frame_tree, columns=list(df_pagina.columns), show='headings', style='Custom.Treeview')
    tree.pack(expand=True, fill='both')

    largura_colunas = {
        'Nome': 150,
        'Turma': 100,
        'Nota 1': 60,
        'Nota 2': 60,
        'Nota 3': 60,
        'Nota 4': 60,
        'Media': 80,
        'Situacao': 140,
    }

    for col in df_pagina.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center', width=largura_colunas.get(col, 100))

    for indice, linha in df_pagina.iterrows():
        tree.insert('', 'end', value=list(linha))

    colorir_situacao(tree, list(df_filtrado.columns).index('Situacao'))

    label_status.configure(text=f'Pagina {pagina_atual} de {num_paginas}')
    style.map('Custom.Treeview.Heading', background=[('pressed', '#003366'), ('active', '#003366')], foreground=[('pressed', 'write'), ('active', 'white')])


def colorir_situacao(tree, col_index):
    for item in tree.get_children():
        situacao = tree.item(item, 'values')[col_index]

        if situacao == 'Aprovado':
            tree.item(item, tags=('aprovado',))

        elif situacao == 'Recuperacao':
            tree.item(item, tags=('recuperacao',))

        elif situacao == 'Reprovado por Notas':
            tree.item(item, tags=('reprovado_notas',))

        elif situacao == 'Reprovado por Faltas':
            tree.item(item, tags=('reprovado_faltas',))

        tree.tag_configure('aprovado', background='#d4edda', foreground='#155724')
        tree.tag_configure("recuperacao", background="#fff3cd", foreground="#856404")
        tree.tag_configure("reprovado_notas", background="#f8d7da", foreground="#721c24")
        tree.tag_configure("reprovado_faltas", background="#f5c6cb", foreground="#721c24")


def primeira_pagina():
    global pagina_atual

    pagina_atual = 1
    exibir_pagina()


def avancar_pagina():
    global pagina_atual
    if pagina_atual < num_paginas:
        pagina_atual += 1
        exibir_pagina()
    else:
        label_status.configure(text="Já está na última página", fg='red')

def voltar_pagina():
    global pagina_atual
    if pagina_atual > 1:
        pagina_atual -= 1
        exibir_pagina()
    else:
        label_status.configure(text="Já está na primeira página", fg='red')


def ultima_pagina():
    global pagina_atual

    pagina_atual = num_paginas
    exibir_pagina()


janela = tk.Tk()
janela.title('Gestao de Notas dos estudantes')
janela.geometry('1024x400')
style = ttk.Style()
style.configure('Custom.Treeview.Heading', font=('Arial', 12, 'bold'))
style.configure('Custom.Treeview', highlightthickness=0, bd=0, font=('Arial', 12, 'bold'))

titulo = tk.Label(janela, text='Projeto: Gestao de Notas dos Estudantes', font=('Arial', 18, 'bold'), bg='black', fg='white')
titulo.pack(fill='x')

frame_filtro = tk.Frame(janela, bg='#f8f9fa')
frame_filtro.pack(pady=10, fill='x')

label_filtro = tk.Label(frame_filtro, text='Filtrar:', bg='#f8f9fa', font=('Arial', 12))
label_filtro.pack(side='left', padx=10)

entrada_filtro = tk.Entry(frame_filtro, font=('Arial', 12))
entrada_filtro.pack(side='left', padx=10, fill='x', expand=True)
entrada_filtro.bind('<KeyRelease>', lambda event: aplicar_filtro())

frame_tree = tk.Frame(janela)
frame_tree.pack(expand=True, fill='both')

frame_botores = tk.Frame(janela, bg='#f8f9fa')
frame_botores.pack(fill='x', pady=10)

btn_primeira = tk.Button(frame_botores, text='<< Primeira', command=primeira_pagina, bg='#007bff', fg='white', font=('Arial', 12, 'bold'))
btn_primeira.pack(side='left', padx=5)

btn_voltar = tk.Button(frame_botores, text='< Voltar', command=voltar_pagina, bg='#007bff', fg='white', font=('Arial', 12, 'bold'))
btn_voltar.pack(side='left', padx=5)

btn_avancar = tk.Button(frame_botores, text='Avancar >', command=avancar_pagina, bg='#007bff', fg='white', font=('Arial', 12, 'bold'))
btn_avancar.pack(side='left', padx=5)

btn_ultima = tk.Button(frame_botores, text='Ultima >>', command=ultima_pagina, bg='#007bff', fg='white', font=('Arial', 12, 'bold'))
btn_ultima.pack(side='left', padx=5)

btn_exportar = tk.Button(frame_botores, text='Exportar Dados Filtrados', command=exportar_dados_filtrados, bg='#28a745', fg='white', font=('Arial', 12, 'bold'))
btn_exportar.pack(side='right', padx=10)

label_status = tk.Label(janela, text='', font=('Arial', 14), bg='#f8f9fa')
label_status.pack(pady=5)

carregar_dados()

janela.mainloop()
