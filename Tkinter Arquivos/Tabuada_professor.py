import tkinter as tk
from tkinter import messagebox

def gerar_tabuada():
    """Gera a tabuada do número inserido pelo usuário e exibe no widget de texto."""
    numero = entrada_numero.get().strip()

    if not numero:
        messagebox.showwarning('Aviso', 'Por favor, insira um número.')
        return

    try:
        numero = int(numero)
    except ValueError:
        messagebox.showwarning('Aviso', 'Por favor, insira um número válido.')
        return

    resultados = [f'{numero} x {i} = {numero * i}' for i in range(1, 11)]
    texto_resultado.delete('1.0', tk.END)
    texto_resultado.insert(tk.END, "\n".join(resultados))

# Configurações da Janela
janela = tk.Tk()
janela.title('Tabuada')
janela.configure(bg='white')

LARGURA_JANELA = 300
ALTURA_JANELA = 400

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicao_x = (largura_tela // 2) - (LARGURA_JANELA // 2)
posicao_y = (altura_tela // 2) - (ALTURA_JANELA // 2)

janela.geometry(f'{LARGURA_JANELA}x{ALTURA_JANELA}+{posicao_x}+{posicao_y}')

# Frame para Entrada de Dados
frame_entrada = tk.Frame(janela, bg='white')
frame_entrada.pack(pady=10)

label_numero = tk.Label(frame_entrada, text='Número:', bg='white', font=('Helvetica', 12))
label_numero.grid(row=0, column=0, pady=5, padx=5)

entrada_numero = tk.Entry(frame_entrada, width=20, font=('Helvetica', 12))
entrada_numero.grid(row=0, column=1, padx=5, pady=5)

# Botão para Gerar Tabuada
botao_gerar = tk.Button(janela, text='Gerar Tabuada', command=gerar_tabuada, font=('Helvetica', 12))
botao_gerar.pack(pady=10)

# Widget de Texto para Mostrar a Tabuada
texto_resultado = tk.Text(janela, width=25, height=10, font=('Helvetica', 12))
texto_resultado.pack(pady=10)

janela.mainloop()
