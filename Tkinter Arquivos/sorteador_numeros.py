import tkinter as tk
from tkinter import messagebox
import random
import time

def sortear_numero():
    """Sorteia um número entre os valores de início e fim inseridos pelo usuário."""
    try:
        inicio = int(entrada_texto.get())
        fim = int(entrada_fim.get())

        if inicio > fim:
            raise ValueError('O número inicial deve ser menor ou igual ao número final')
        
        botao_sortear.config(state=tk.DISABLED)
        entrada_texto.config(state=tk.DISABLED)
        entrada_fim.config(state=tk.DISABLED)

        for i in range(5, 0, -1):
            label_resultado.config(text=f"Sorteando em {i}...")
            janela.update()
            time.sleep(1)

        numero_sorteado = random.randint(inicio, fim)
        label_resultado.config(text=f'Número sorteado: {numero_sorteado}')
    
    except ValueError as ve:
        messagebox.showerror('Erro', f'Entrada inválida: {ve}')
    
    except Exception as e:
        messagebox.showerror('Erro', f'Erro inesperado: {e}')
    
    finally:
        botao_sortear.config(state=tk.NORMAL)
        entrada_texto.config(state=tk.NORMAL)
        entrada_fim.config(state=tk.NORMAL)

# Configuração da Janela
janela = tk.Tk()
janela.title('Sorteador de Número')
janela.configure(bg='white')

LARGURA_JANELA = 400
ALTURA_JANELA = 300

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicao_x = (largura_tela // 2) - (LARGURA_JANELA // 2)
posicao_y = (altura_tela // 2) - (ALTURA_JANELA // 2)

janela.geometry(f'{LARGURA_JANELA}x{ALTURA_JANELA}+{posicao_x}+{posicao_y}')

# Frame para Entradas
frame_entradas = tk.Frame(janela, bg='white')
frame_entradas.pack(pady=20)

label_inicio = tk.Label(frame_entradas, text="Número Inicial", bg='white', font=('Helvetica', 12))
label_inicio.grid(row=0, column=0, padx=5, pady=5)

entrada_texto = tk.Entry(frame_entradas, width=10, font=('Helvetica', 12))
entrada_texto.grid(row=0, column=1, padx=5, pady=5)

label_fim = tk.Label(frame_entradas, text="Número Final", bg='white', font=('Helvetica', 12))
label_fim.grid(row=1, column=0, padx=5, pady=5)

entrada_fim = tk.Entry(frame_entradas, width=10, font=('Helvetica', 12))
entrada_fim.grid(row=1, column=1, padx=5, pady=5)

# Botão para Sortear Número
botao_sortear = tk.Button(janela, text='Sortear Número', command=sortear_numero, font=('Helvetica', 12))
botao_sortear.pack(pady=20)

# Label para Mostrar o Resultado
label_resultado = tk.Label(janela, text='', bg='white', font=('Helvetica', 16))
label_resultado.pack(pady=20)

janela.mainloop()
