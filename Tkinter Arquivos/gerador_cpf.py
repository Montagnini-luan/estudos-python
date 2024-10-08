import tkinter as tk
from tkinter import messagebox
import random

def gerar_digito_verificador(nove_digitos):
    soma = 0

    for i, num in enumerate(nove_digitos):
        soma += int(num) * (10 - i)

    digito1 = soma % 11
    digito1 = 0 if digito1 < 2 else 11 - digito1

    soma = 0

    nove_digitos.append(str(digito1))

    for i, num in enumerate(nove_digitos):
        soma += int(num) * (11 - i)

    digito2 = soma % 11
    digito2 = 0 if digito2 < 2 else 11 - digito2

    return digito1, digito2

def gerar_cpf():
    nove_digitos = [str(random.randint(0, 9)) for _ in range(9)]
    digito1, digito2 = gerar_digito_verificador(nove_digitos)

    cpf = ''.join(nove_digitos[:9] + [str(digito1)] + [str(digito2)])

    entrada_cpf.delete(0, tk.END)
    entrada_cpf.insert(0, formatar_cpf(cpf))

def formatar_cpf(cpf):
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def mostrar_regras():
    """Mostra as regras do cálculo do CPF em uma nova janela."""
    regras_janela = tk.Toplevel(janela_principal)

    regras_janela.title("Regras do Cálculo do CPF")
    regras_janela.configure(bg="white")

    largura_janela_regras = 1200
    altura_janela_regras = 400

    largura_tela_regras = regras_janela.winfo_screenwidth()
    altura_tela_regras = regras_janela.winfo_screenheight()

    posicao_x_regras = (largura_tela_regras // 2) - (largura_janela_regras // 2)
    posicao_y_regras = (altura_tela_regras // 2) - (altura_janela_regras // 2)

    regras_janela.geometry(
        f"{largura_janela_regras}x{altura_janela_regras}+{posicao_x_regras}+{posicao_y_regras}"
    )

    texto_regras = (
        "O CPF (Cadastro de Pessoas Físicas) é composto por 11 dígitos.\n\n"
        "Os nove primeiros dígitos são a base do CPF. A partir deles, calculam-se os dois dígitos verificadores.\n\n"
        "Cálculo do primeiro dígito verificador:\n"
        "1. Multiplique os 9 primeiros dígitos pela sequência decrescente de 10 a 2.\n"
        "2. Some os resultados das multiplicações.\n"
        "3. Calcule o resto da divisão da soma por 11.\n"
        "4. Se o resto for menor que 2, o primeiro dígito verificador é 0. Caso contrário, subtraia o resto de 11 para obter o primeiro dígito verificador.\n\n"
        "Cálculo do segundo dígito verificador:\n"
        "1. Inclua o primeiro dígito verificador aos 9 primeiros dígitos, totalizando 10 dígitos.\n"
        "2. Multiplique os 10 dígitos pela sequência decrescente de 11 a 2.\n"
        "3. Some os resultados das multiplicações.\n"
        "4. Calcule o resto da divisão da soma por 11.\n"
        "5. Se o resto for menor que 2, o segundo dígito verificador é 0. Caso contrário, subtraia o resto de 11 para obter o segundo dígito verificador."
    )

    label_regras = tk.Label(regras_janela, text=texto_regras, justify="left", bg="white", padx=10, pady=10, font=('Helvetica', 12))

    label_regras.pack(fill="both", expand=True)

# Configuração da Janela Principal
janela_principal = tk.Tk()
janela_principal.title("Gerador de CPF")
janela_principal.configure(bg="white")

LARGURA_JANELA = 400
ALTURA_JANELA = 150
largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()
posicao_x = (largura_tela // 2) - (LARGURA_JANELA // 2)
posicao_y = (altura_tela // 2) - (ALTURA_JANELA // 2)
janela_principal.geometry(f"{LARGURA_JANELA}x{ALTURA_JANELA}+{posicao_x}+{posicao_y}")

janela_principal.grid_columnconfigure(0, weight=1)
janela_principal.grid_rowconfigure(0, weight=1)

frame_principal = tk.Frame(janela_principal, bg="white")
frame_principal.grid(row=0, column=0, sticky="nsew")

frame_botoes = tk.Frame(frame_principal, bg="white")
frame_botoes.pack(pady=20)

botao_gerar = tk.Button(frame_botoes, text="Gerar CPF", command=gerar_cpf, font=('Helvetica', 12))
botao_gerar.grid(row=0, column=0, padx=10)

botao_regras = tk.Button(frame_botoes, text="Regras", command=mostrar_regras, font=('Helvetica', 12))
botao_regras.grid(row=0, column=1, padx=10)

frame_cpf = tk.Frame(frame_principal, bg="white")
frame_cpf.pack(pady=20)

label_cpf = tk.Label(frame_cpf, text="CPF Gerado:", bg="white", font=('Helvetica', 12))
label_cpf.pack(side="left", padx=5)

entrada_cpf = tk.Entry(frame_cpf, width=20, font=('Helvetica', 14))
entrada_cpf.pack(side="left", padx=5)

janela_principal.mainloop()
