import tkinter as tk
from tkinter import messagebox


def texto_para_binario(texto):
    return ' '.join(format(ord(char), '08b') for char in texto)


def binario_para_texto(binario):
    try:
        texto = ''.join(chr(int(b, 2)) for b in binario.split(' '))
        return texto
    except ValueError:
        messagebox.showerror('Erro', 'Código inválido')
        return ''


def converter_para_binario():
    texto = entrada_texto.get('1.0', tk.END).strip()

    if not texto:
        messagebox.showwarning('Aviso', 'Por favor, insira algum texto para converter.')
        return

    resultado_binario = texto_para_binario(texto)
    saida_texto.delete('1.0', tk.END)
    saida_texto.insert(tk.END, resultado_binario)


def converter_para_texto():
    binario = entrada_texto.get('1.0', tk.END).strip()

    if not binario:
        messagebox.showwarning('Aviso', 'Por favor, insira algum código binário para converter.')
        return

    resultado_texto = binario_para_texto(binario)
    saida_texto.delete('1.0', tk.END)
    saida_texto.insert(tk.END, resultado_texto)


def mostrar_regras():
    regras_janela = tk.Toplevel(janela_principal)
    regras_janela.title("Regras da Conversão")
    regras_janela.configure(bg="white")

    largura_janela_regras = 600
    altura_janela_regras = 300
    largura_tela_regras = regras_janela.winfo_screenwidth()
    altura_tela_regras = regras_janela.winfo_screenheight()

    posicao_x_regras = (largura_tela_regras // 2) - (largura_janela_regras // 2)
    posicao_y_regras = (altura_tela_regras // 2) - (altura_janela_regras // 2)

    regras_janela.geometry(f"{largura_janela_regras}x{altura_janela_regras}+{posicao_x_regras}+{posicao_y_regras}")

    texto_regras = (
        "Conversão de Texto para Código Binário:\n"
        "1. Cada caractere é convertido para seu código ASCII.\n"
        "2. O código ASCII é então convertido para uma representação binária de 8 bits.\n"
        "3. Todos os bits são agrupados com espaços entre eles.\n\n"
        "Conversão de Código Binário para Texto:\n"
        "1. O código binário é dividido em grupos de 8 bits.\n"
        "2. Cada grupo de 8 bits é convertido para um número decimal (código ASCII).\n"
        "3. O código ASCII é convertido para o caractere correspondente."
    )

    label_regras = tk.Label(
        regras_janela, text=texto_regras, justify="left",
        bg="white", padx=10, pady=10, font=('Helvetica', 12)
    )
    label_regras.pack(fill="both", expand=True)


# Configuração da Janela Principal
janela_principal = tk.Tk()
janela_principal.title("Conversor de código binário")
janela_principal.configure(bg="white")

LARGURA_JANELA = 600
ALTURA_JANELA = 400
largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()
posicao_x = (largura_tela // 2) - (LARGURA_JANELA // 2)
posicao_y = (altura_tela // 2) - (ALTURA_JANELA // 2)
janela_principal.geometry(f"{LARGURA_JANELA}x{ALTURA_JANELA}+{posicao_x}+{posicao_y}")

frame_entrada = tk.Frame(janela_principal, bg="white")
frame_entrada.pack(pady=10)

label_entrada = tk.Label(frame_entrada, text="Texto ou Código Binário:", bg="white", font=('Helvetica', 12))
label_entrada.pack()

entrada_texto = tk.Text(frame_entrada, height=8, width=70, font=('Helvetica', 12))
entrada_texto.pack(pady=5)

frame_botoes = tk.Frame(janela_principal, bg="white")
frame_botoes.pack(pady=10)

botao_para_binario = tk.Button(frame_botoes, text="Converter para binário", command=converter_para_binario, font=('Helvetica', 12))
botao_para_binario.grid(row=0, column=0, padx=10)

botao_para_texto = tk.Button(frame_botoes, text="Converter para texto", command=converter_para_texto, font=('Helvetica', 12))
botao_para_texto.grid(row=0, column=1, padx=10)

botao_regras = tk.Button(frame_botoes, text="Regras", command=mostrar_regras, font=('Helvetica', 12))
botao_regras.grid(row=0, column=2, padx=10)

frame_saida = tk.Frame(janela_principal, bg="white")
frame_saida.pack(pady=10)

label_saida = tk.Label(frame_saida, text="Resultado:", bg="white", font=('Helvetica', 12))
label_saida.pack()

saida_texto = tk.Text(frame_saida, height=8, width=70, font=('Helvetica', 12))
saida_texto.pack(pady=5)

janela_principal.mainloop()
