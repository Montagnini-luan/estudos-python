import tkinter as tk
from tkinter import messagebox

def calcular_aumento():
    """Calcula o aumento salarial e exibe o valor e percentual na interface."""
    try:
        salario_atual = float(salario_atual_entrada.get())
        novo_salario = float(novo_salario_entrada.get())

        if salario_atual > novo_salario:
            raise ValueError('O salário novo deve ser maior do que o salário atual.')
        
        valor_aumento = novo_salario - salario_atual
        percentual_aumento = (valor_aumento / salario_atual) * 100

        label_valor_aumento.config(text=f"Valor do Aumento: R$ {valor_aumento:.2f}")
        label_percentual_aumento.config(text=f"Percentual do Aumento: {percentual_aumento:.2f}%")

    except ValueError as ve:
        messagebox.showerror('Erro', f'Entrada inválida: {ve}')
    except Exception as e:
        messagebox.showerror('Erro', f'Erro inesperado: {e}')

# Configuração da Janela
janela = tk.Tk()
janela.title('Calculador de Aumento Salarial')
janela.configure(bg='white')

LARGURA_JANELA = 400
ALTURA_JANELA = 400

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicao_x = (largura_tela // 2) - (LARGURA_JANELA // 2)
posicao_y = (altura_tela // 2) - (ALTURA_JANELA // 2)

janela.geometry(f'{LARGURA_JANELA}x{ALTURA_JANELA}+{posicao_x}+{posicao_y}')

# Frame para Entradas
frame_entradas = tk.Frame(janela, bg='white')
frame_entradas.pack(pady=20)

label_inicio = tk.Label(frame_entradas, text="Salário Atual (R$):", bg='white', font=('Helvetica', 12))
label_inicio.grid(row=0, column=0, padx=5, pady=5)

salario_atual_entrada = tk.Entry(frame_entradas, width=10, font=('Helvetica', 12))
salario_atual_entrada.grid(row=0, column=1, padx=5, pady=5)

label_fim = tk.Label(frame_entradas, text="Novo Salário (R$):", bg='white', font=('Helvetica', 12))
label_fim.grid(row=1, column=0, padx=5, pady=5)

novo_salario_entrada = tk.Entry(frame_entradas, width=10, font=('Helvetica', 12))
novo_salario_entrada.grid(row=1, column=1, padx=5, pady=5)

# Botão para Calcular o Aumento
botao_calcular = tk.Button(janela, text='Calcular Aumento', command=calcular_aumento, font=('Helvetica', 12))
botao_calcular.pack(pady=20)

# Labels para Mostrar o Resultado
label_valor_aumento = tk.Label(janela, text='', bg='white', font=('Helvetica', 16))
label_valor_aumento.pack(pady=20)

label_percentual_aumento = tk.Label(janela, text='', bg='white', font=('Helvetica', 16))
label_percentual_aumento.pack(pady=20)

janela.mainloop()
