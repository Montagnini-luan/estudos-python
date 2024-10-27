"""
Interface gráfica para filtrar cidades por país e estado.
"""

import tkinter as tk
from tkinter import ttk
import pandas as pd

def carregar_dados_excel():
    """
    Carrega dados do arquivo Excel.

    Returns:
        DataFrame: Contém os dados de países, estados e cidades.
    """
    local_arquivo = (
        "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\"
        "estudos python\\Tkinter Arquivos\\Cidades.xlsx"
    )
    return pd.read_excel(local_arquivo, sheet_name='Dados')

def atualizar_combos(event=None):
    """
    Atualiza opções dos comboboxes.

    Args:
        event: Evento que disparou a função (opcional).
    """
    pais_selecionado = combo_pais.get()
    estado_selecionado = combo_estado.get()
    cidade_selecionada = combo_cidade.get()
    
    dados_filtrados = df
    
    if pais_selecionado:
        dados_filtrados = dados_filtrados[dados_filtrados['Pais'] == pais_selecionado]
        
        estados = sorted(dados_filtrados['Estado'].unique())
        combo_estado['values'] = estados
        
        if estado_selecionado:
            dados_filtrados = dados_filtrados[dados_filtrados['Estado'] == estado_selecionado]
        
        cidades = sorted(dados_filtrados['Cidade'].unique())
        combo_cidade['values'] = cidades
        
        if cidade_selecionada not in cidades:
            combo_cidade.set('')
    
    # Atualiza a Treeview com os dados filtrados
    tree.delete(*tree.get_children())
    for _, row in dados_filtrados.iterrows():
        tree.insert('', 'end', values=(row['Pais'], row['Estado'], row['Cidade']))
    

# Carrega dados
df = carregar_dados_excel()

# Configura janela principal
janela = tk.Tk()
janela.title('Filtro de Cidades')
janela.geometry('800x600')
janela.configure(bg='#E6E6FA')  # Cor de fundo lavanda claro

# Estilo geral
style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='#E6E6FA')
style.configure('TLabel', background='#E6E6FA', font=('Arial', 12))
style.configure('TCombobox', fieldbackground='#FFFFFF', background='#4B0082')
style.configure('Treeview', background='#FFFFFF', fieldbackground='#FFFFFF', foreground='#000000')
style.configure('Treeview.Heading', font=('Arial', 12, 'bold'), background='#4B0082', foreground='#FFFFFF')

# Frame para filtros
frame_filtros = ttk.Frame(janela, padding="10 10 10 10", style='TFrame')
frame_filtros.pack(pady=20, padx=20, fill='x')

# Labels e comboboxes
ttk.Label(frame_filtros, text='País:', style='TLabel').grid(row=0, column=0, padx=10, pady=5, sticky='e')
combo_pais = ttk.Combobox(frame_filtros, values=sorted(df['Pais'].unique()), font=('Arial', 12), state='readonly')
combo_pais.grid(row=0, column=1, padx=10, pady=5, sticky='ew')
combo_pais.bind('<<ComboboxSelected>>', atualizar_combos)

ttk.Label(frame_filtros, text='Estado:', style='TLabel').grid(row=1, column=0, padx=10, pady=5, sticky='e')
combo_estado = ttk.Combobox(frame_filtros, font=('Arial', 12), state='readonly')
combo_estado.grid(row=1, column=1, padx=10, pady=5, sticky='ew')
combo_estado.bind('<<ComboboxSelected>>', atualizar_combos)

ttk.Label(frame_filtros, text='Cidade:', style='TLabel').grid(row=2, column=0, padx=10, pady=5, sticky='e')
combo_cidade = ttk.Combobox(frame_filtros, font=('Arial', 12), state='readonly')
combo_cidade.grid(row=2, column=1, padx=10, pady=5, sticky='ew')
combo_cidade.bind('<<ComboboxSelected>>', atualizar_combos)

# Configura Treeview
tree_frame = ttk.Frame(janela, padding="10 10 10 10", style='TFrame')
tree_frame.pack(expand=True, fill='both', padx=20, pady=20)

tree = ttk.Treeview(
    tree_frame, columns=('Pais', 'Estado', 'Cidade'), show='headings', height=15
)
tree.heading('Pais', text='País')
tree.heading('Estado', text='Estado')
tree.heading('Cidade', text='Cidade')

# Barra de rolagem
scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
tree.pack(side='left', fill='both', expand=True)

# Preenche Treeview
for index, row in df.iterrows():
    tree.insert('', 'end', values=(row['Pais'], row['Estado'], row['Cidade']))

# Inicia loop principal
janela.mainloop()
