import tkinter as tk


def destacar_celula(event):
    for i in range(10):
        for j in range(5):
            tabela[i][j].configure(bg='white', fg='black', font=('Arial', 10))

    linha = event.widget.grid_info()['row']
    coluna = event.widget.grid_info()['column']

    tabela[linha][coluna].configure(bg='yellow', fg='black', font=('Arial', 14, 'bold'))

    for j in range(5):
        if j != coluna:
            tabela[linha][j].config(bg='lightgray')

    for i in range(10):
        if i != linha:
            tabela[i][coluna].config(bg='lightgray')


def restaurar_celula(event):
    linha = event.widget.grid_info()['row']
    coluna = event.widget.grid_info()['column']

    for i in range(10):
        for j in range(5):
            tabela[i][j].config(bg='white', fg='black', font=('Arial', 10))


janela = tk.Tk()
janela.title('Tabela interativa')

tabela = []

for i in range(10):
    linha = []

    for j in range(5):
        celula = tk.Label(janela, text=f'L{i+1} C{j+1}', bg='white', fg='black', width=12, height=3, borderwidth=1, relief='solid', font=('Arial', 10))
        celula.grid(row=i, column=j, sticky='NSEW')
        celula.bind('<Enter>', destacar_celula)
        celula.bind('<Leave>', restaurar_celula)

        linha.append(celula)

    tabela.append(linha)

for j in range(5):
    janela.grid_columnconfigure(j, weight=1)

for i in range(10):
    janela.grid_rowconfigure(i, weight=1)

janela.mainloop()
