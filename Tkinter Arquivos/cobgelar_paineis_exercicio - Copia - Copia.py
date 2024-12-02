import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import asksaveasfilename
import pandas as pd


def atualizar_tabelas():
    tabela.delete(*tabela.get_children())
    
    tabela_congelada1.delete(*tabela_congelada1.get_children())
    tabela_congelada2.delete(*tabela_congelada2.get_children())

    for indice, linha in df.iterrows():
        valores_congelada1 = (linha[colunas_congeladas1[0]],)
        valores_congelada2 = (linha[colunas_congeladas2[0]],)

        valores_tabela = tuple(linha[coluna] for coluna in colunas_tabela)
        
        tabela_congelada1.insert("", tk.END, values=valores_congelada1)
        tabela_congelada2.insert("", tk.END, values=valores_congelada2)
        
        tabela.insert("", tk.END, values=valores_tabela)

    label_contagem.config(text=f"Registros exibidos: {len(df)}")


def aplicar_filtro(*args):
    global df

    df = df_original.copy()

    for coluna in colunas_tabela + colunas_congeladas1 + colunas_congeladas2:
        valor_filtro = filtros[coluna].get()

        if valor_filtro:
            df = df[df[coluna].astype(str).str.contains(valor_filtro, case=False, na=False, regex=False)]

    atualizar_tabelas()


def exportar_para_arquivo():
    tipo_arquivo = asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])

    if tipo_arquivo:
        if tipo_arquivo.endswith(".xlsx"):
            df.to_excel(tipo_arquivo, index=False)

        elif tipo_arquivo.endswith(".csv"):
            df.to_csv(tipo_arquivo, index=False, encoding="utf-8-sig")

        messagebox.showinfo("Exportação", f"Dados exportados com sucesso para {tipo_arquivo}")


def sincronizar_rolagem(*args):
    tabela.yview(*args)
    tabela_congelada1.yview(*args)
    tabela_congelada2.yview(*args)

global sincronizando
sincronizando = False


def sincronizar_selecao(event):
    global sincronizando

    if sincronizando:
        return

    sincronizando = True

    tabela_selecionada = event.widget
    
    selecionado = tabela_selecionada.selection()

    if selecionado:
        indice = tabela_selecionada.index(selecionado[0])

        if tabela_selecionada != tabela_congelada1:
            
            
            tabela_congelada1.selection_set(tabela_congelada1.get_children()[indice])  # Define a linha correspondente na primeira tabela congelada como selecionada.
            tabela_congelada1.see(tabela_congelada1.get_children()[indice])

        if tabela_selecionada != tabela_congelada2:
            tabela_congelada2.selection_set(tabela_congelada2.get_children()[indice])
            tabela_congelada2.see(tabela_congelada2.get_children()[indice])

        if tabela_selecionada != tabela:
            tabela.selection_set(tabela.get_children()[indice])
            tabela.see(tabela.get_children()[indice])

    sincronizando = False


def alternar_tela_cheia(janela):
    estado_tela_cheia = not janela.attributes('-fullscreen')
    janela.attributes('-fullscreen', estado_tela_cheia)


def criar_interface():
    janela = tk.Tk()
    janela.title('Projeto de Notas dos Estudantes')
    janela.geometry('900x600')
    janela.bind('<F11>', lambda event: alternar_tela_cheia(janela))
    janela.bind('<Escape>', lambda event: janela.quit())


    label_titulo = tk.Label(janela, text='Notas dos Estudantes', font=('Arial', 20, 'bold'), bg='lightblue', fg='white')
    label_titulo.pack(fill=tk.X)

    frame_filtro = tk.LabelFrame(janela, text="Filtros", padx=10, pady=5, bg="lightgray")

    canvas_filtros = tk.Canvas(frame_filtro, bg='lightgray', height=50)

    scrollbar_filtros = ttk.Scrollbar(frame_filtro, orient="horizontal", command=canvas_filtros.xview)
    frame_filtros_interior = tk.Frame(canvas_filtros, bg="lightgray")
    frame_filtros_interior.bind("<Configure>", lambda e: canvas_filtros.configure(scrollregion=canvas_filtros.bbox("all")))

    canvas_filtros.create_window((0, 0), window=frame_filtros_interior, anchor="nw")
    canvas_filtros.configure(xscrollcommand=scrollbar_filtros.set)
    canvas_filtros.pack(side=tk.TOP, fill=tk.X, expand=True)

    scrollbar_filtros.pack(side=tk.BOTTOM, fill=tk.X)
    frame_filtro.pack(fill=tk.X, pady=5)
    
    global filtros
    filtros = {}

    for coluna in df.columns:
        
        label_filtro = tk.Label(frame_filtros_interior, text=coluna, bg="lightgray")
        label_filtro.pack(side=tk.LEFT, padx=5)

        entrada_filtro = tk.Entry(frame_filtros_interior, width=10)
        entrada_filtro.pack(side=tk.LEFT, padx=5)
        entrada_filtro.bind("<KeyRelease>", aplicar_filtro)

        filtros[coluna] = entrada_filtro

    frame_contagem_exportar = tk.Frame(janela, bg="white")  
    frame_contagem_exportar.pack(fill=tk.X, pady=5)

    global label_contagem

    label_contagem = tk.Label(frame_contagem_exportar, text='', fg='blue', font=('Arial', 12))
    label_contagem.pack(side=tk.LEFT, pady=5)

    botao_exportar = tk.Button(frame_contagem_exportar, text='Exportar para Arquivo', bg='green', fg='white', font=('Arial', 12), command=exportar_para_arquivo)
    botao_exportar.pack(side=tk.RIGHT, pady=5, padx=5)

    botao_sair = tk.Button(frame_contagem_exportar, text='Sair', bg='red', fg='white', font=('Arial', 12), command=janela.destroy)
    botao_sair.pack(side=tk.RIGHT, pady=5, padx=5)

    frame_principal = tk.Frame(janela, bg='white')
    frame_principal.pack(fill=tk.BOTH, expand=True)

    frame_congelado1 = tk.Frame(frame_principal, bg='white')
    frame_congelado1.pack(side=tk.LEFT, fill=tk.Y)

    frame_congelado2 = tk.Frame(frame_principal, bg='white')
    frame_congelado2.pack(side=tk.LEFT, fill=tk.Y)

    frame_tabela = tk.Frame(frame_principal)
    frame_tabela.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    global colunas_congeladas1, colunas_congeladas2
    
    colunas_congeladas1 = [df.columns[0]]  # Armazena a primeira coluna do DataFrame.
    colunas_congeladas2 = [df.columns[1]]  # Armazena a segunda coluna do DataFrame.

    global tabela_congelada1, tabela_congelada2

    tabela_congelada1 = ttk.Treeview(frame_congelado1, columns=colunas_congeladas1, show='headings', height=15)
    tabela_congelada1.pack(side=tk.LEFT, fill=tk.Y)
    
    tabela_congelada2 = ttk.Treeview(frame_congelado2, columns=colunas_congeladas2, show='headings', height=15)
    tabela_congelada2.pack(side=tk.LEFT, fill=tk.Y)

    for coluna in colunas_congeladas1:
        tabela_congelada1.heading(coluna, text=coluna)
        tabela_congelada1.column(coluna, width=120, anchor='center')
    
    for coluna in colunas_congeladas2:
        tabela_congelada2.heading(coluna, text=coluna)
        tabela_congelada2.column(coluna, width=120, anchor='center')

    scrollbar_vertical = ttk.Scrollbar(frame_tabela, orient="vertical", command=sincronizar_rolagem) 
    scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)

    global colunas_tabela, tabela
    
    colunas_tabela = list(df.columns[2:])  # Exclui as duas primeiras colunas que são congeladas em outras tabelas.
    
    tabela = ttk.Treeview(frame_tabela, columns=colunas_tabela, show='headings', height=15)
    tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    for coluna in colunas_tabela:
        tabela.heading(coluna, text=coluna)  
        tabela.column(coluna, width=max(100, len(coluna) * 10), anchor='center')


    tabela.configure(yscrollcommand=scrollbar_vertical.set)  

    tabela_congelada1.configure(yscrollcommand=scrollbar_vertical.set)  
    tabela_congelada2.configure(yscrollcommand=scrollbar_vertical.set)

    scrollbar_horizontal = ttk.Scrollbar(janela, orient="horizontal", command=tabela.xview)
    scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)

    tabela.configure(xscrollcommand=scrollbar_horizontal.set)
    tabela.bind("<ButtonRelease-1>", sincronizar_selecao)
    tabela_congelada1.bind("<ButtonRelease-1>", sincronizar_selecao)
    tabela_congelada2.bind("<ButtonRelease-1>", sincronizar_selecao)

    atualizar_tabelas()

    janela.mainloop()


# Carregar o arquivo Excel e criar a interface
arquivo_excel = "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\notas_estudantes (3).xlsx"
df_original = pd.read_excel(arquivo_excel, sheet_name='Dados')
df = df_original.copy()
criar_interface()