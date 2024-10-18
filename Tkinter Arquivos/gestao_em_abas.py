import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd

# Função para carregar dados do Excel
def carregar_dados():
    global df_original
    df_original = pd.read_excel(
        'C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\funcionarios.xlsx',
        sheet_name='Dados'
    )
    df_original['Salário'] = df_original['Salário'].apply(lambda x: f'{x:,.2f}').replace(',', 'v').replace('.', ',').replace('v', '.')
    
    departamentos = df_original['Departamento'].unique()
    
    # Criando uma aba para cada departamento
    for dept in departamentos:
        aba = ttk.Frame(caderno)
        caderno.add(aba, text=dept)
        abas[dept] = aba
    
    aplicar_filtro()

# Função para aplicar filtro
def aplicar_filtro():
    termo = entrada_filtro.get().lower()
    
    # Limpar widgets existentes
    for dept, aba in abas.items():
        for widget in aba.winfo_children():
            widget.destroy()
        
        df_filtrado = df_original[df_original.apply(lambda row: termo in row.to_string(index=False).lower(), axis=1)]
        df_dept = df_filtrado[df_filtrado['Departamento'] == dept]
        
        tree = ttk.Treeview(aba, columns=list(df_dept.columns), show='headings')
        tree.pack(expand=True, fill='both')
        
        for col in df_dept.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center')
        
        for index, row in df_dept.iterrows():
            tree.insert('', 'end', values=list(row))
        
        dados_filtrados[dept] = df_dept

# Função para exportar dados filtrados da aba ativa
def exportar_dados_filtrados_aba_ativa():
    aba_ativa = caderno.tab(caderno.select(), 'text')
    df_exportar = dados_filtrados.get(aba_ativa)
    
    if df_exportar is not None:
        arquivo = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel file', '*.xlsx')])
        if arquivo:
            df_exportar.to_excel(arquivo, index=False)

# Função para exportar dados de todas as abas
def exportar_todas_abas():
    arquivo = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel file', '*.xlsx')])
    
    if arquivo:
        with pd.ExcelWriter(arquivo) as writer:
            for dept in abas.keys():
                df_exportar = dados_filtrados.get(dept, pd.DataFrame())
                df_exportar.to_excel(writer, sheet_name=dept, index=False)

# Configuração da janela principal
janela = tk.Tk()
janela.title('Gestão de Funcionários')

# Título do projeto
titulo = tk.Label(janela, text='Projeto: Gestão de Funcionários', font=('Arial', 16, 'bold'))
titulo.pack(pady=10)

# Frame do filtro
frame_filtro = tk.Frame(janela)
frame_filtro.pack(pady=5)

label_filtro = tk.Label(frame_filtro, text='Filtrar:')
label_filtro.pack(side='left', padx=5)

entrada_filtro = tk.Entry(frame_filtro)
entrada_filtro.pack(side='left', padx=5, fill='x', expand=True)
entrada_filtro.bind('<KeyRelease>', lambda event: aplicar_filtro())

# Notebook para as abas
caderno = ttk.Notebook(janela)
caderno.pack(expand=True, fill='both')

abas = {}
dados_filtrados = {}

# Frame dos botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botao_exportar_aba = tk.Button(frame_botoes, text='Exportar Dados Filtrados da Aba Ativa', command=exportar_dados_filtrados_aba_ativa)
botao_exportar_aba.pack(side='left', padx=5)

botao_exportar_todas = tk.Button(frame_botoes, text='Exportar Todas as Abas', command=exportar_todas_abas)
botao_exportar_todas.pack(side='left', padx=5)

# Carregar os dados na inicialização
carregar_dados()

# Iniciar a aplicação
janela.mainloop()
