import tkinter as tk
from tkinter import messagebox


def adicionar_item():
    selecionado = lista_esquerda.curselection()

    if selecionado:
        item = lista_esquerda.get(selecionado)
        lista_direita.insert(tk.END, item)
        lista_esquerda.delete(selecionado)

    else:
        messagebox.showwarning('Selecao invalida', 'Selecione um item para adicionar')


def remover_item():
    selecionado = lista_direita.curselection()

    if selecionado:
        item = lista_direita.get(selecionado)
        lista_esquerda.insert(tk.END, item)
        lista_direita.delete(selecionado)

    else:
        messagebox.showwarning('Selecao invalida', 'Selecione um item para adicionar')


def mover_todos_para_direita():
    itens = lista_esquerda.get(0, tk.END)

    for item in itens:
        lista_direita.insert(tk.END, item)

    lista_esquerda.delete(0, tk.END)


def mover_todos_para_esquerda():
    itens = lista_direita.get(0, tk.END)

    for item in itens:
        lista_esquerda.insert(tk.END, item)

    lista_direita.delete(0, tk.END)


janela = tk.Tk()
janela.title('Passar Dados entre Listas')

fonte = ('Arial', 14)

lista_esquerda = tk.Listbox(janela, selectmode=tk.SINGLE, font=fonte)
lista_esquerda.pack(side=tk.LEFT, padx=10, pady=10)

lista_direita = tk.Listbox(janela, selectmode=tk.SINGLE, font=fonte)
lista_direita.pack(side=tk.RIGHT, padx=10, pady=10)

btn_adicionar = tk.Button(janela, text='Adicionar ->', command=adicionar_item, font=fonte)
btn_adicionar.pack(pady=5)

btn_remover = tk.Button(janela, text='<- Remover', command=remover_item, font=fonte)
btn_remover.pack(pady=5)

btn_mover_todos_direita = tk.Button(janela, text='Mover todos ->', command=mover_todos_para_direita, font=fonte)
btn_mover_todos_direita.pack(pady=5)

btn_mover_todos_esquerda = tk.Button(janela, text='<- Mover todos', command=mover_todos_para_esquerda, font=fonte)
btn_mover_todos_esquerda.pack(pady=5)

itens = [f'Item {i+1}' for i in range(15)]

for item in itens:
    lista_esquerda.insert(tk.END, item)

janela.mainloop()

