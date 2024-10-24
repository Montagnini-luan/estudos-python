import tkinter as tk
import pandas as pd

def carregar_dados_excel():
    global df, colunas_ocultas, indice_salario

    df = pd.read_excel("C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\tabela_exemplo (2).xlsx")
    colunas = list(df.columns)

    # Remove todas as células existentes antes de recriar
    for i in range(len(cabecalho)):
        cabecalho[i].grid_remove()
    for i in range(len(tabela)):
        for j in range(len(tabela[i])):
            tabela[i][j].grid_remove()

    coluna_atual = 0

    # Atualiza o cabeçalho da tabela com as colunas visíveis
    for j, coluna in enumerate(colunas):
        if j not in colunas_ocultas:
            cabecalho[coluna_atual].config(text=coluna)
            cabecalho[coluna_atual].grid(row=1, column=coluna_atual, sticky='NSEW')
            janela.grid_columnconfigure(coluna_atual, weight=1)
            if coluna == 'Salário':
                indice_salario = coluna_atual
            coluna_atual += 1

    # Preenche a tabela com os dados visíveis
    for i in range(len(df)):
        coluna_atual = 0
        for j in range(len(df.columns)):
            if j not in colunas_ocultas:
                tabela[i][coluna_atual].config(text=df.iloc[i, j])
                tabela[i][coluna_atual].grid(row=i + 2, column=coluna_atual, sticky='NSEW')
                coluna_atual += 1

    # Exibe o botão para expandir colunas ocultas na posição da coluna "Salário"
    btn_agrupar_colunas.grid(row=1, column=indice_salario, sticky='E')


def expandir_colunas():
    global colunas_ocultas

    # Exibe novamente as colunas ocultas
    colunas_ocultas = []  
    carregar_dados_excel()  # Atualiza a tabela para exibir todas as colunas

    btn_agrupar_colunas.config(text='-', command=agrupar_colunas)


def agrupar_colunas():
    global colunas_ocultas

    colunas_ocultas = list(range(1, len(df.columns) - 1))
    carregar_dados_excel()  # Atualiza a tabela para exibir todas as colunas

    btn_agrupar_colunas.config(text='+', command=expandir_colunas)


janela = tk.Tk()
janela.title('Tabela interativa com colunas')

# Carregar os dados do Excel
df = pd.read_excel("C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\tabela_exemplo (2).xlsx")

colunas = len(df.columns)
linhas = len(df)

# Índice da coluna "Salário"
indice_salario = colunas - 1

# Inicialmente ocultar todas as colunas, exceto a primeira e a última
colunas_ocultas = list(range(1, colunas - 1))

# Título da janela
titulo = tk.Label(janela, text='Tabela com Agrupamento de Colunas', font=('Arial', 16, 'bold'))
titulo.grid(row=0, column=0, columnspan=colunas, pady=10)

# Cabeçalho da tabela
cabecalho = []
for j in range(colunas):
    celula_cabecalho = tk.Label(janela, text='', bg='lightblue', fg='black', width=12, height=2, borderwidth=1, relief='solid', font=('Arial', 12, 'bold'))
    cabecalho.append(celula_cabecalho)

# Células da tabela
tabela = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        celula = tk.Label(janela, text='', bg='white', fg='black', width=12, height=3, borderwidth=1, relief='solid', font=('Arial', 10))
        linha.append(celula)
    tabela.append(linha)

# Botão para expandir as colunas ocultas
btn_agrupar_colunas = tk.Button(janela, text='+', command=expandir_colunas, font=('Arial', 12), width=3)

# Configuração de grid para ajustar a expansão das colunas
for j in range(colunas):
    janela.grid_columnconfigure(j, weight=1)

carregar_dados_excel()

janela.mainloop()
