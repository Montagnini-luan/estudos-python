import tkinter as tk
from tkinter import ttk, messagebox
from turtle import title
import pandas as pd

df = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\dados_cidades.xlsx', sheet_name='Cidades')

def exportar_para_excel():
    dados_exportar = [tabela.item(item)['values'] for item in tabela.get_children()]
    df_exportar = pd.DataFrame(dados_exportar, columns=['Cidade', 'População', 'PIB (em milhões)'])
    df_exportar.to_excel('dados_filtrados_cidades.xlsx', index=False)
    messagebox.showinfo('Concluido', 'Dados exportados para dados_filtrados_cidades.xlsx')

def aplicar_filtro(*args):
    filtros = {
        "Cidade": filtro_cidade.get().strip().lower(),
        "População": filtro_populacao.get().strip().lower(),
        "PIB (em milhões)": filtro_PIB.get().strip().lower()
    }

    df_filtrado = df[df['País'] == pais_selecionado]

    for coluna, filtro in filtros.items():
        if filtro:
            df_filtrado = df_filtrado[df_filtrado[coluna].astype(str).str.lower().str.contains(filtro)]

    atualizar_tabela(df_filtrado)

def atualizar_tabela(dados):
    for row in tabela.get_children():
        tabela.delete(row)

    for index, row in dados.iterrows():
        tabela.insert('', 'end', values=(row['Cidade'], row['População'], row['PIB (em milhões)']))

def exibir_informacao_pais(event):
    global pais_selecionado

    item_selecionado = arvore.selection()[0]
    info_pais = arvore.item(item_selecionado, 'values')

    if info_pais:
        pais_selecionado = info_pais[0]
        aplicar_filtro()

janela_principal = tk.Tk()
janela_principal.title('Treeview com exemplo e exportacao')

fonte_padrao = ('Arial', 12)

arvore = ttk.Treeview(janela_principal)
arvore.pack(side='left', fill='y')

style = ttk.Style()
style.configure('Treeview.Heading', font=('Arial', 14, 'bold'))

arvore.column('#0', width=250, minwidth=250)
arvore.heading('#0', text='Continete -> Pais', anchor=tk.W)

continentes = df.groupby('Continente')

for continente, grupo_continente in continentes:
    id_continente = arvore.insert('', 'end', text=continente, open=False)

    paises = grupo_continente.groupby('País')

    for pais, group_pais in paises:
        arvore.insert(id_continente, 'end', text=pais, values=(pais,))

frame_filtros = tk.Frame(janela_principal)
frame_filtros.pack(side='top', fill='x', pady=5, padx=10)

tk.Label(frame_filtros, text='Filtrar cidades:', font=fonte_padrao).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
filtro_cidade = tk.Entry(frame_filtros, font=fonte_padrao)
filtro_cidade.grid(row=0, column=1, padx=5, pady=5)
filtro_cidade.bind('<KeyRelease>', aplicar_filtro)

tk.Label(frame_filtros, text='Filtrar populacao:', font=fonte_padrao).grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
filtro_populacao = tk.Entry(frame_filtros, font=fonte_padrao)
filtro_populacao.grid(row=0, column=3, padx=5, pady=5)
filtro_populacao.bind('<KeyRelease>', aplicar_filtro)

tk.Label(frame_filtros, text='Filtrar PIB:', font=fonte_padrao).grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)
filtro_PIB = tk.Entry(frame_filtros, font=fonte_padrao)
filtro_PIB.grid(row=0, column=5, padx=5, pady=5)
filtro_PIB.bind('<KeyRelease>', aplicar_filtro)

frame_tabela = tk.Frame(janela_principal)
frame_tabela.pack(side='top', fill='both', expand=True, padx=10, pady=10)

colunas = ('Cidade', 'População', 'PIB (em milhões)')
tabela = ttk.Treeview(frame_tabela, columns=colunas, show='headings', height=20)
tabela.pack(fill='both', expand=True)

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=150)

btn_exportar = tk.Button(janela_principal, text='Exportar para excel', font=fonte_padrao, command=exportar_para_excel)
btn_exportar.pack(side='top', pady=10)

arvore.bind('<<TreeviewSelect>>', exibir_informacao_pais)

janela_principal.mainloop()
