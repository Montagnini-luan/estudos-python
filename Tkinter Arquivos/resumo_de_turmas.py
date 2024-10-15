import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
import pandas as pd

def carregar_dados():
    df = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\notas_estudantes.xlsx', sheet_name='Dados')
    df['Média'] = df[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].mean(axis=1)
    df['Situação'] = df.apply(lambda row: classificar_situacao(row['Média'], row['Faltas']), axis=1)
    return df

def classificar_situacao(media, faltas):
    if faltas > 10:
        return 'Reprovado por Faltas'
    elif media < 2:
        return 'Reprovado por Nota'
    elif 2 <= media < 7:
        return 'Recuperacao'
    else:
        return 'Aprovado'

def filtrar_alunos(*args):
    filtro = entrada_filtro.get().lower()

    alunos_filtrados_locais = alunos_filtrados[alunos_filtrados['Nome'].str.lower().str.contains(filtro) |
                                               alunos_filtrados['Situação'].str.lower().str.contains(filtro)]
    
    for item in tabela_detalhes.get_children():
        tabela_detalhes.delete(item)

    for _, aluno in alunos_filtrados_locais.iterrows():
        tabela_detalhes.insert('', 'end', values=(aluno['Nome'], f"{aluno['Média']:.2f}", aluno['Situação']))

def exportar_para_excel():
    alunos_filtrados_locais = alunos_filtrados[alunos_filtrados['Nome'].str.lower().str.contains(entrada_filtro.get().lower()) |
                                               alunos_filtrados['Situação'].str.lower().str.contains(entrada_filtro.get().lower())]
    
    if not alunos_filtrados_locais.empty:
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel files', '*.xlsx')])

        if caminho_arquivo:
            alunos_filtrados_locais.to_excel(caminho_arquivo, index=False)
            messagebox.showinfo('Exportacao bem sucedida', f'Os dados foram exportados para {caminho_arquivo} com sucesso')

def calcular_estatisticas(df):
    estatisticas = df.groupby('Turma').agg(
        media_da_turma=('Média', 'mean'),
        total_de_faltas=('Faltas', 'sum')
    ).reset_index()
    estatisticas = estatisticas.sort_values(by='Turma')
    return estatisticas

def exibir_detalhes(event):
    linha_id = tabela.identify_row(event.y)
    if linha_id:
        item = tabela.item(linha_id)
        valores = item['values']
        turma = valores[0]
        global alunos_filtrados
        alunos_filtrados = df[df['Turma'] == turma]
        atualizar_tabela_detalhes()
        titulo_turma.config(text=f'Turma: {turma}')

def atualizar_tabela_detalhes():
    for item in tabela_detalhes.get_children():
        tabela_detalhes.delete(item)
    for _, aluno in alunos_filtrados.iterrows():
        tabela_detalhes.insert('', 'end', values=(aluno['Nome'], f'{aluno["Média"]:.2f}', aluno['Situação']))

def exibir_tooltip_aluno(event):
    linha_id = tabela_detalhes.identify_row(event.y)

    if linha_id:
        item = tabela_detalhes.item(linha_id)
        nome_aluno = item['values'][0]
        aluno = df[df['Nome'] == nome_aluno].iloc[0]
        texto_aluno = (f'Nome: {aluno["Nome"]}\n'
                       f'Nota 1: {aluno["Nota 1"]}\n'
                       f'Nota 2: {aluno["Nota 2"]}\n'
                       f'Nota 3: {aluno["Nota 3"]}\n'
                       f'Nota 4: {aluno["Nota 4"]}\n'
                       f'Media:{aluno["Média"]}\n'
                       f'Faltas: {aluno["Faltas"]}\n'
                       f'Situacao: {aluno["Situação"]}')
        
        label_tooltip_aluno.config(text=texto_aluno)
        tooltip_aluno.wm_geometry(f'+{event.x_root + 10}+{event.y_root + 10}')
        tooltip_aluno.deiconify()

def ocultar_tooltip_aluno(event):
    tooltip_aluno.withdraw()

janela = tk.Tk()
janela.title('Resumo de Turmas')

df = carregar_dados()
estatisticas = calcular_estatisticas(df)

fonte_padrao = ('Arial', 12)
fonte_detalhes = ('Arial', 12, 'bold')

colunas = ('Turma', 'Media da Turma', 'Total de Faltas')
tabela = ttk.Treeview(janela, columns=colunas, show='headings', style='mystyle.Treeview')
tabela.pack(side='left', fill='both', expand=True)

style = ttk.Style()
style.configure('mystyle.Treeview', font=fonte_padrao, rowheight=30)
style.configure('mystyle.Treeview.Heading', font=fonte_detalhes)

for col in colunas:
    tabela.heading(col, text=col)

painel_lateral = tk.Frame(janela, bg='lightyellow', relief='solid', borderwidth=2, width=300)
painel_lateral.pack(side='right', fill='y')

titulo_turma = tk.Label(painel_lateral, text='Selecione uma turma', font=fonte_detalhes, bg='lightyellow')
titulo_turma.pack(padx=10, pady=10)

entrada_filtro = tk.Entry(painel_lateral, font=fonte_padrao)
entrada_filtro.pack(fill='x', padx=10, pady=5)
entrada_filtro.bind('<KeyRelease>', filtrar_alunos)

botao_exportar = tk.Button(painel_lateral, text='Exportar para excel', command=exportar_para_excel, font=fonte_padrao)
botao_exportar.pack(padx=10, pady=5)

tabela_detalhes = ttk.Treeview(painel_lateral, columns=('Nome', 'Media', 'Situacao'), show='headings', style='mystyle.Treeview')
tabela_detalhes.pack(fill='both', expand=True)

for col in ('Nome', 'Media', 'Situacao'):
    tabela_detalhes.heading(col, text=col)

tooltip_aluno = tk.Toplevel(janela)
tooltip_aluno.withdraw()
tooltip_aluno.overrideredirect(True)

label_tooltip_aluno = tk.Label(tooltip_aluno, text='', justify='left', background='lightblue', font=fonte_detalhes)
label_tooltip_aluno.pack(padx=10, pady=5)

tabela.bind('<Motion>', exibir_detalhes)
tabela_detalhes.bind('<Motion>', exibir_tooltip_aluno)
tabela_detalhes.bind('<Leave>', ocultar_tooltip_aluno)

for _, row in estatisticas.iterrows():
    tabela.insert('', 'end', values=(row['Turma'], f"{row['media_da_turma']:.2f}", row['total_de_faltas']))

janela.mainloop()
