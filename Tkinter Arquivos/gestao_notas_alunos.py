import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd


def carregar_dados():
    global df
    df = pd.read_excel(
        'C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\notas_estudantes.xlsx',
        sheet_name='Dados'
    )
    df['Média'] = df[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].mean(axis=1)
    df['Situação'] = df.apply(lambda row: classificar_situacao(row['Média'], row['Faltas']), axis=1)
    turmas = df['Turma'].unique()

    # Criando uma aba para cada turma
    for turma in turmas:
        aba = ttk.Frame(caderno)
        caderno.add(aba, text=turma)
        abas[turma] = aba
        aplicar_filtro()


def aplicar_filtro():
    termo = entrada_filtro.get().lower()

    # Limpar widgets existentes
    for turma, aba in abas.items():
        for widget in aba.winfo_children():
            widget.destroy()

        df_filtrado = df[df.apply(lambda row: termo in row.to_string(index=False).lower(), axis=1)]
        df_turma = df_filtrado[df_filtrado['Turma'] == turma]

        tree = ttk.Treeview(aba, columns=list(df_turma.columns), show='headings')
        tree.pack(expand=True, fill='both')

        for col in df_turma.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center')

        for index, row in df_turma.iterrows():
            situacao = row['Situação']
            if situacao == 'Aprovado':
                tags = 'aprovado'
            elif situacao == 'Recuperacao':
                tags = 'recuperacao'
            elif situacao == 'Reprovado por Faltas':
                tags = 'reprovado_faltas'
            else:
                tags = 'reprovado_nota'

            tree.insert('', 'end', values=list(row), tags=(tags))

        # Adicionando estilos condicionais
        tree.tag_configure('aprovado', background="#d4edda", foreground="#155724")
        tree.tag_configure('recuperacao', background="#fff3cd", foreground="#856404")
        tree.tag_configure('reprovado_faltas', background="#f5c6cb", foreground="#721c24")
        tree.tag_configure('reprovado_nota', background="#f8d7da", foreground="#721c24")

        dados_filtrados[turma] = df_turma


def classificar_situacao(media, faltas):
    if faltas > 10:
        return 'Reprovado por Faltas'
    elif media < 2:
        return 'Reprovado por Nota'
    elif 2 <= media < 7:
        return 'Recuperacao'
    else:
        return 'Aprovado'


def exportar_dados_filtrados_aba_ativa():
    aba_ativa = caderno.tab(caderno.select(), 'text')
    df_exportar = dados_filtrados.get(aba_ativa)

    if df_exportar is not None:
        arquivo = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel file', '*.xlsx')])
        if arquivo:
            df_exportar.to_excel(arquivo, index=False)


def exportar_todas_abas():
    arquivo = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel file', '*.xlsx')])

    if arquivo:
        with pd.ExcelWriter(arquivo) as writer:
            for turma in abas.keys():
                df_exportar = dados_filtrados.get(turma, pd.DataFrame())
                df_exportar.to_excel(writer, sheet_name=turma, index=False)


# Configuração da Janela Principal
janela = tk.Tk()
janela.title('Gestão de Notas Alunos')
janela.geometry("1024x400")

titulo = tk.Label(janela, text='Projeto: Gestão de Notas dos Estudantes', font=('Arial', 16, 'bold'), bg='black', fg='white')
titulo.pack(pady=10, fill='x')

# Frame do filtro
frame_filtro = tk.Frame(janela)
frame_filtro.pack(pady=5, fill='x')
label_filtro = tk.Label(frame_filtro, text='Filtrar:')
label_filtro.pack(side='left', padx=10)
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

botao_exportar_aba = tk.Button(frame_botoes, bg='green', fg='white', font=('Arial', 12, 'bold'), text='Exportar Dados Filtrados da Aba Ativa', command=exportar_dados_filtrados_aba_ativa)
botao_exportar_aba.pack(side='left', padx=5)

botao_exportar_todas = tk.Button(frame_botoes, bg='blue', fg='white', font=('Arial', 12, 'bold'), text='Exportar Todas as Abas', command=exportar_todas_abas)
botao_exportar_todas.pack(side='left', padx=5)

# Carregar os dados na inicialização
carregar_dados()

janela.mainloop()
