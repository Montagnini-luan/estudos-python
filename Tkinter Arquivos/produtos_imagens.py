import tkinter as tk
from tkinter import ttk
from turtle import left
import pandas as pd
from PIL import Image, ImageTk
import os

def carregarDados():
    df = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\Vendedor.xlsx')
    df['Total'] = df['Total'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'v').replace('.', ',').replace('v', '.'))
    return df

def filtrar_dados(*args):
    filtro_vendedor = entrada_filtro_vendedor.get().lower()
    filtro_produto = entrada_filtro_produto.get().lower()
    filtro_total = entrada_filtro_total.get().lower()
    dados_filtrados = df[
        df['Vendedor'].str.lower().str.contains(filtro_vendedor) &
        df['Produto'].str.lower().str.contains(filtro_produto) &
        df['Total'].astype(str).str.lower().str.contains(filtro_total)
    ]
    atualizar_tabela(dados_filtrados)

def atualizar_tabela(dados):
    for item in tabela.get_children():
        tabela.delete(item)
    for index, linha in dados.iterrows():
        tabela.insert('', 'end', values=(linha['Vendedor'], linha['Produto'], linha['Total']))

def exibir_tooltip(evento):
    id_linha = tabela.identify_row(evento.y)

    if id_linha:
        item = tabela.item(id_linha)

        valores = item['values']
        vendedor, produto, total = valores

        caminho_imagem = os.path.join('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\produtos_imagens\\imagem', f'\\{produto}.jpg')

        if os.path.exists(caminho_imagem):
            imagem = Image.open(caminho_imagem)
            imagem = imagem.resize((200, 200), Image.Resampling.LANCZOS)
            imagem_tk = ImageTk.PhotoImage(imagem)

            label_imagem.config(image=imagem_tk)
            label_imagem.image = imagem_tk
        
        else:
            label_imagem.configure(image='', text='Imagem nao encontrada')

        texto_tooltip = f'Vendedor: {vendedor}\nProduto: {produto}\nTotal: {total}'
        label_tooltip.config(text=texto_tooltip)

        tooltip.wm_geometry(f'+{evento.x_root + 10}+{evento.y_root + 10}')
        tooltip.deiconify()

def ocultar_tooltip(evento):
    tooltip.withdraw()

janela = tk.Tk()
janela.title('Tabela de Vendas')

df = carregarDados()
fonte_padrao = ('Arial', 12)
font_tooltip = ('Arial', 14, 'bold')

filtros_frame = tk.Frame(janela)
filtros_frame.pack(fill='x')

tk.Label(filtros_frame, text='Filtrar por Vendedor', font=fonte_padrao).grid(row=0, column=0, padx=5, pady=5)
entrada_filtro_vendedor = tk.Entry(filtros_frame, font=fonte_padrao)
entrada_filtro_vendedor.grid(row=0, column=1, padx=5, pady=5)
entrada_filtro_vendedor.bind('<KeyRelease>', filtrar_dados)

tk.Label(filtros_frame, text='Filtrar por Produto', font=fonte_padrao).grid(row=0, column=2, padx=5, pady=5)
entrada_filtro_produto = tk.Entry(filtros_frame, font=fonte_padrao)
entrada_filtro_produto.grid(row=0, column=3, padx=5, pady=5)
entrada_filtro_produto.bind('<KeyRelease>', filtrar_dados)

tk.Label(filtros_frame, text='Filtrar por Total', font=fonte_padrao).grid(row=0, column=4, padx=5, pady=5)
entrada_filtro_total = tk.Entry(filtros_frame, font=fonte_padrao)
entrada_filtro_total.grid(row=0, column=5, padx=5, pady=5)
entrada_filtro_total.bind('<KeyRelease>', filtrar_dados)

colunas = ('Vendedor', 'Produto', 'Total')
tabela = ttk.Treeview(janela, columns=colunas, show='headings', style="mystyle.Treeview")
tabela.pack(fill='both', expand=True)

style = ttk.Style()
style.configure('mystyle.Treeview', font=fonte_padrao, rowheight=30)
style.configure('mystyle.Treeview.Heading', font=font_tooltip)

for col in colunas:
    tabela.heading(col, text=col)

tooltip = tk.Toplevel(janela)
tooltip.withdraw()
tooltip.overrideredirect(True)

tooltip_frame = tk.Frame(tooltip, bg='lightblue', relief='solid', borderwidth=2)
tooltip_frame.pack(fill='both', expand=True)

label_tooltip = tk.Label(tooltip_frame, text='', justify='left', background='lightblue', font=font_tooltip)
label_tooltip.pack(padx=10, pady=5)

label_imagem = tk.Label(tooltip_frame, background='lightblue')
label_imagem.pack(pady=5)

tabela.bind('<Motion>', exibir_tooltip)
tabela.bind('<Leave>', ocultar_tooltip)

atualizar_tabela(df)

janela.mainloop()
