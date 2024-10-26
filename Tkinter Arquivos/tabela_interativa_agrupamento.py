import tkinter as tk 
from tkinter import ttk
import pandas as pd

def formatar_salario(valor):
    formatted = f'{valor:,.2f}'
    return formatted.replace(',', 'x').replace('.', ',').replace('x', '.')


def carregar_dados():
    tree.delete(*tree.get_children())
    df_grouped = df.groupby('Cidade', as_index=False).sum()

    for _, row in df_grouped.iterrows():
        cidade = row['Cidade']

        salario_atual = formatar_salario(row['Salário'])

        cidade_id = tree.insert('', 'end', text=cidade, values=['','','', salario_atual], open=False, tags=('cidade',))
        registros_cidade = df[df['Cidade'] == cidade]

        for _, detalhe in registros_cidade.iterrows():
            valores = list(detalhe)
            valores[4] = formatar_salario(valores[4])
            valores[0] = ''

            tree.insert(cidade_id, 'end', values=valores)
            tree.tag_configure('cidade', background='lightgray')

            atualizar_visibilidade_colunas()

def atualizar_visibilidade_colunas():
    if colunas_ocultas:
        tree['displaycolumns'] = colunas[1:]

        btn_agrupar_colunas.config(text='-')

    else:
         tree['displaycolumns'] = ('Salário',)

         btn_agrupar_colunas.config(text='+')


colunas_ocultas = False


def toggle_colunas():
    global colunas_ocultas

    colunas_ocultas = not colunas_ocultas

    atualizar_visibilidade_colunas()



local_arquivo = "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\tabela_exemplo (2).xlsx"
df = pd.read_excel(local_arquivo)

df['Salário'] = df['Salário'].astype(float)

colunas = ['Cidade', 'Profissão', 'Nome', 'Idade', 'Salário']

janela= tk.Tk()
janela.title('Janela Interativa com Agrupamento de Colunas')
janela.configure(bg='white')

style = ttk.Style()
style.configure('Cidade.Treeview', background='lightgray', foreground='black')

titulo = tk.Label(janela, text='Projeto: Tabela Interativa com Filtros', font=('Arial', 16), bg='white')
titulo.grid(row=0, column=0, columnspan=3, pady=(10, 10))

container_filtros = tk.Frame(janela, bg='white')
container_filtros.grid(row=1, column=0, columnspan=3, pady=(10, 10))

filtros = {}

for idx, col in enumerate(colunas):
    label = tk.Label(container_filtros, text=col, font=('Arial', 12), bg='white')
    label.grid(row=0, column=idx, padx=(5, 5))

    filtro = tk.Entry(container_filtros, font=('Arial', 12))
    filtro.grid(row=1, column=idx, padx=(5, 5))
    filtros[col] = filtro

tree = ttk.Treeview(janela, columns=colunas, show='tree headings')
tree.heading('#0', text='Cidade')

for col in colunas:
    tree.heading(col, text=col)

tree.grid(row=3, column=0, columnspan=3, pady=10)

carregar_dados()

janela.mainloop()