import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

def calcular_media_turma(grupo):
    notas = grupo[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].mean(axis=1)
    return notas.mean()

def calcular_situacao(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = "Aprovado"
    elif 2 <= media < 7:
        situacao = "Recuperacao"
    else:
        situacao = "Reprovado"
    return media, situacao

def exibir_informacoes_aluno(event):
    try:
        item_selecionado = arvore.selection()[0]
        info_aluno = arvore.item(item_selecionado, 'values')
        if info_aluno:
            nome_aluno = info_aluno[0]
            aluno_dados = df[df['Nome'] == nome_aluno]
            if not aluno_dados.empty:
                aluno_dados = aluno_dados.iloc[0]
                notas = [aluno_dados['Nota 1'], aluno_dados['Nota 2'], aluno_dados['Nota 3'], aluno_dados['Nota 4']]
                media, situacao = calcular_situacao(notas)
                entrada_nome.delete(0, tk.END)
                entrada_nome.insert(0, nome_aluno)
                entrada_nota1.delete(0, tk.END)
                entrada_nota1.insert(0, notas[0])
                entrada_nota2.delete(0, tk.END)
                entrada_nota2.insert(0, notas[1])
                entrada_nota3.delete(0, tk.END)
                entrada_nota3.insert(0, notas[2])
                entrada_nota4.delete(0, tk.END)
                entrada_nota4.insert(0, notas[3])
                entrada_media.delete(0, tk.END)
                entrada_media.insert(0, f"{media:.2f}")
                entrada_situacao.delete(0, tk.END)
                entrada_situacao.insert(0, situacao)
                if situacao == "Aprovado":
                    entrada_situacao.config(bg="green", fg="white")
                elif situacao == "Recuperacao":
                    entrada_situacao.config(bg="yellow", fg="black")
                else:
                    entrada_situacao.config(bg="red", fg="white")
            else:
                messagebox.showwarning("Aviso", "Aluno não encontrado no DataFrame.")
    except IndexError:
        messagebox.showwarning("Aviso", "Nenhum aluno selecionado.")

df = pd.read_excel(
    'C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\notas_estudantes (1).xlsx',
    sheet_name='Dados'
)

janela_principal = tk.Tk()
janela_principal.title("Notas dos Estudantes")

fonte_padrao = ('Arial', 14)
arvore = ttk.Treeview(janela_principal, style="mystyle.Treeview")
arvore.pack(side='left', fill='y')

style = ttk.Style()
style.configure("mystyle.Treeview", font=fonte_padrao, rowheight=30)
style.configure("mystyle.Treeview.Heading", font=('Arial', 16, 'bold'))

arvore.column("#0", width=300, minwidth=300)
arvore.heading("#0", text="Turma (Média da Turma)", anchor=tk.W)

turmas = df.groupby('Turma')

for turma, grupo in turmas:
    media_turma = calcular_media_turma(grupo)
    texto_turma = f"{turma} (Média: {media_turma:.2f})"
    turma_id = arvore.insert('', 'end', text=texto_turma, open=False)
    for _, aluno in grupo.iterrows():
        arvore.insert(turma_id, 'end', text=f"{aluno['Nome']}", values=(aluno['Nome'],))

frame_info = tk.Frame(janela_principal)
frame_info.pack(side='left', fill='both', expand=True, padx=10, pady=10)

tk.Label(frame_info, text="Nome:", font=fonte_padrao).grid(row=0, column=0, sticky=tk.W)
entrada_nome = tk.Entry(frame_info, width=30, font=fonte_padrao)
entrada_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_info, text="Nota 1:", font=fonte_padrao).grid(row=1, column=0, sticky=tk.W)
entrada_nota1 = tk.Entry(frame_info, width=10, font=fonte_padrao)
entrada_nota1.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_info, text="Nota 2:", font=fonte_padrao).grid(row=2, column=0, sticky=tk.W)
entrada_nota2 = tk.Entry(frame_info, width=10, font=fonte_padrao)
entrada_nota2.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_info, text="Nota 3:", font=fonte_padrao).grid(row=3, column=0, sticky=tk.W)
entrada_nota3 = tk.Entry(frame_info, width=10, font=fonte_padrao)
entrada_nota3.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_info, text="Nota 4:", font=fonte_padrao).grid(row=4, column=0, sticky=tk.W)
entrada_nota4 = tk.Entry(frame_info, width=10, font=fonte_padrao)
entrada_nota4.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame_info, text="Média:", font=fonte_padrao).grid(row=5, column=0, sticky=tk.W)
entrada_media = tk.Entry(frame_info, width=10, font=fonte_padrao)
entrada_media.grid(row=5, column=1, padx=5, pady=5)

tk.Label(frame_info, text="Situação:", font=fonte_padrao).grid(row=6, column=0, sticky=tk.W)
entrada_situacao = tk.Entry(frame_info, width=15, font=fonte_padrao)
entrada_situacao.grid(row=6, column=1, padx=5, pady=5)

arvore.bind("<<TreeviewSelect>>", exibir_informacoes_aluno)

janela_principal.mainloop()
