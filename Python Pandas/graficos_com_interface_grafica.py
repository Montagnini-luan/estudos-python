# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
from PIL import ImageGrab
import os

# Classe principal
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        
        # Definindo cores do tema
        self.cor_bg = "#f0f2f5"  # Cinza claro para background
        self.cor_primaria = "#1a237e"  # Azul escuro
        self.cor_secundaria = "#283593"  # Azul médio
        self.cor_destaque = "#3949ab"  # Azul claro
        self.cor_texto = "#212121"  # Cinza escuro para texto
        self.cor_borda = "#e0e0e0"  # Cinza claro para bordas
        
        # Configurando a janela principal
        self.master.title("Dashboard Analytics")
        self.master.configure(bg=self.cor_bg)
        self.master.state('zoomed')  # Iniciar maximizado
        
        # Configurando o estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configurando estilos personalizados
        self.configure_styles()
        
        self.create_widgets()
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        
    def configure_styles(self):
        # Estilo para botões
        self.style.configure(
            'Dashboard.TButton',
            background=self.cor_primaria,
            foreground='white',
            padding=10,
            font=('Segoe UI', 10),
            borderwidth=0
        )
        self.style.map('Dashboard.TButton',
            background=[('active', self.cor_destaque)],
            foreground=[('active', 'white')]
        )
        
        # Estilo para frames
        self.style.configure(
            'Dashboard.TFrame',
            background=self.cor_bg,
            borderwidth=1,
            relief='solid'
        )
        
        # Estilo para labels
        self.style.configure(
            'Dashboard.TLabel',
            background=self.cor_bg,
            foreground=self.cor_texto,
            font=('Segoe UI', 10)
        )
        
    def create_widgets(self):
        # Menu superior moderno
        self.menu_bar = Menu(self.master, bg=self.cor_primaria, fg='white')
        self.master.config(menu=self.menu_bar)
        
        # Configuração do menu arquivo
        self.arquivo_menu = Menu(
            self.menu_bar,
            tearoff=0,
            bg=self.cor_primaria,
            fg='white',
            activebackground=self.cor_destaque,
            activeforeground='white'
        )
        self.menu_bar.add_cascade(label="Arquivo", menu=self.arquivo_menu)
        self.arquivo_menu.add_command(label="Abrir", command=self.abrir_arquivo)
        self.arquivo_menu.add_separator()
        self.arquivo_menu.add_command(label="Sair", command=self.master.destroy)
        
        # Frame superior para controles
        self.frame_controles = ttk.Frame(self.master, style='Dashboard.TFrame')
        self.frame_controles.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        # Botões de controle com ícones
        self.btn_dash1 = ttk.Button(
            self.frame_controles,
            text="Dashboard 1",
            style='Dashboard.TButton',
            command=self.criar_dashboard1
        )
        self.btn_dash1.grid(row=0, column=0, padx=5, pady=5)
        
        self.btn_dash2 = ttk.Button(
            self.frame_controles,
            text="Dashboard 2",
            style='Dashboard.TButton',
            command=self.criar_dashboard2
        )
        self.btn_dash2.grid(row=0, column=1, padx=5, pady=5)
        
        self.btn_editar = ttk.Button(
            self.frame_controles,
            text="Editar Dados",
            style='Dashboard.TButton',
            command=self.editar_dados
        )
        self.btn_editar.grid(row=0, column=2, padx=5, pady=5)
        
        # Frame lateral para botões de gráficos
        self.frame_botoes = ttk.Frame(self.master, style='Dashboard.TFrame')
        self.frame_botoes.grid(row=1, column=0, padx=10, pady=10, sticky="ns")
        
        # Label do menu de gráficos
        ttk.Label(
            self.frame_botoes,
            text="TIPOS DE GRÁFICOS",
            style='Dashboard.TLabel',
            font=('Segoe UI', 12, 'bold')
        ).grid(row=0, column=0, pady=10, padx=5)
        
        # Botões de gráficos
        graficos = [
            ("Colunas", self.abrir_janela_colunas),
            ("Pizza", self.criar_grafico_pizza),
            ("Linhas", self.criar_grafico_linhas),
            ("Área", self.criar_grafico_area),
            ("Funil", self.criar_grafico_funil)
        ]
        
        for i, (texto, comando) in enumerate(graficos, 1):
            ttk.Button(
                self.frame_botoes,
                text=texto,
                style='Dashboard.TButton',
                command=comando
            ).grid(row=i, column=0, pady=5, padx=5, sticky="ew")
            
        # Frame principal para exibição dos gráficos
        self.fig = plt.Figure(figsize=(6, 8), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        # Barra de status
        self.status_bar = ttk.Label(
            self.master,
            text="Pronto",
            style='Dashboard.TLabel',
            relief=SUNKEN,
            anchor=W
        )
        self.status_bar.grid(row=2, column=0, columnspan=2, sticky="ew")

    def abrir_arquivo(self):
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione um arquivo Excel",
            filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
        )
        
        if caminho_arquivo:
            try:
                self.df = pd.read_excel(caminho_arquivo)
                messagebox.showinfo("Sucesso", f"Arquivo {caminho_arquivo} carregado com sucesso")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {str(e)}")
        else:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado")
        
    def criar_dashboard1(self):
        # Implementar dashboard 1
        pass
        
    def criar_dashboard2(self):
        # Implementar dashboard 2
        pass
        
    def editar_dados(self):
        # Implementar edição de dados
        pass
    
    def abrir_janela_colunas(self):
        try:
            self.janela_colunas = Toplevel(self.master)
            self.janela_colunas.title("Grafico de Colunas")
            self.janela_colunas.geometry("300x300")
            self.janela_colunas.grab_set()
            
            self.lb_eixo_x = ttk.Label(self.janela_colunas, text="Eixo X:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_eixo_x.pack(pady=5)
            
            self.cb_eixo_x = Combobox(self.janela_colunas, values=self.df.columns.tolist())
            self.cb_eixo_x.pack(pady=5)
            
            self.lb_eixo_y = ttk.Label(self.janela_colunas, text="Eixo Y:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_eixo_y.pack(pady=5)
            
            self.cb_eixo_y = Combobox(self.janela_colunas, values=self.df.columns.tolist())
            self.cb_eixo_y.pack(pady=5)
            
            self.lb_titulo = ttk.Label(self.janela_colunas, text="Titulo:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_titulo.pack(pady=5)
            
            self.entry_titulo = Entry(self.janela_colunas, width=20)
            self.entry_titulo.pack(pady=5)
            
            self.lb_imagem = ttk.Label(self.janela_colunas, text="Imagem:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_imagem.pack(pady=5)
            
            self.cb_imagem = Combobox(self.janela_colunas, 
                                    values=['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8'],
                                    style='Dashboard.TCombobox', font=('Segoe UI', 10))
            self.cb_imagem.pack(pady=5)
            
            self.btn_gerar_1 = ttk.Button(self.janela_colunas, text="Grafico 1", style='Dashboard.TButton', command=self.criar_grafico_colunas)
            self.btn_gerar_1.pack(side=LEFT, padx=5, pady=5)

            self.btn_gerar_2 = ttk.Button(self.janela_colunas, text="Grafico 2", style='Dashboard.TButton', command=self.criar_grafico_colunas)
            self.btn_gerar_2.pack(side=LEFT, padx=5, pady=5)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir a janela de colunas: {str(e)}")
            self.janela_colunas.destroy()
            
        
    def criar_grafico_colunas(self):
        self.ax.clear()
        
        col_x = self.cb_eixo_x.get()
        col_y = self.cb_eixo_y.get()
        img = self.cb_imagem.get()
        
        df_agrupado = self.df.groupby(col_x).sum()[col_y]
        
        titulo_grafico = self.entry_titulo.get()
        
        self.ax.bar(df_agrupado.index, df_agrupado.values)
        self.ax.set_xlabel(col_x)
        self.ax.set_ylabel(col_y)
        self.ax.set_title(f"Grafico de Colunas - {col_x} x {col_y}" if not titulo_grafico else titulo_grafico)
        
        for i, v in enumerate(df_agrupado.values):
            self.ax.annotate(str(v), xy=(i, v), ha='center', va='bottom')
        
        self.canvas.draw()
        
    def criar_grafico_pizza(self):
        # Implementar gráfico de pizza
        pass
        
    def criar_grafico_linhas(self):
        # Implementar gráfico de linhas
        pass
        
    def criar_grafico_area(self):
        # Implementar gráfico de área
        pass
        
    def criar_grafico_funil(self):
        # Implementar gráfico de funil
        pass

# Função principal
def main():
    tela = Tk()
    tela.title("Dashboard Analytics")
    
    # Definir ícone
    # tela.iconbitmap('caminho_para_icone.ico')
    
    # Definir tamanho mínimo
    tela.minsize(800, 600)
    
    app = Application(master=tela)
    tela.mainloop()

if __name__ == "__main__":
    main()
