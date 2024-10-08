import tkinter as tk
from tkinter import messagebox

def tabuada():
    try:
        numero = int(campoDigitavelnumero.get())
    except ValueError:
        messagebox.showwarning('Entrada invalida', 'Por favor, insira um numero valido.')
        return
    
    tabela = ""

    for i in range(1, 11):
        resultado = i * numero
        tabela += f"{numero} x {i} = {resultado}\n"

    resultado_tabela.delete('1.0', tk.END)
    resultado_tabela.insert('1.0', tabela)

# Configuração da Janela
janela = tk.Tk()
janela.title('Gerador de Tabuada')
janela.configure(bg="white")

largura_janela = 500
altura_janela = 500
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicao_x = (largura_tela // 2) - (largura_janela // 2)
posicao_y = (altura_tela // 2) - (altura_janela // 2)

janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

# Widgets
numero = tk.Label(janela, text="Numero", font="Arial 20", bg="white")
numero.grid(row=1, column=1, pady=10)
campoDigitavelnumero = tk.Entry(janela, font="Arial 12")
campoDigitavelnumero.grid(row=1, column=2, pady=10)

botaoGerar = tk.Button(janela, text="Gerar Tabuada", font="Arial 20", command=tabuada)
botaoGerar.grid(row=1, column=3, padx=10, pady=10)

resultado = tk.Label(janela, text="Resultado", font="Arial 20", bg="white")
resultado.grid(row=2, column=1, columnspan=3)

resultado_tabela = tk.Text(janela, font="Arial 12", width=30, height=10)
resultado_tabela.grid(row=3, column=1, columnspan=3, pady=10)

# Inicialização da Janela
janela.mainloop()
