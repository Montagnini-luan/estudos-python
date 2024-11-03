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
            ("Pizza", self.abrir_janela_pizza),
            ("Linhas", self.abrir_janela_linhas),
            ("Área", self.abrir_janela_area),
            ("Funil", self.abrir_janela_funil)
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

            self.btn_gerar_2 = ttk.Button(self.janela_colunas, text="Grafico 2", style='Dashboard.TButton', command=self.criar_grafico_colunas_2)
            self.btn_gerar_2.pack(side=LEFT, padx=5, pady=5)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir a janela de colunas: {str(e)}")
            self.janela_colunas.destroy() 
        
    def criar_grafico_colunas(self):
        try:
            self.ax.clear()
            
            col_x = self.cb_eixo_x.get()
            col_y = self.cb_eixo_y.get()
            titulo_grafico = self.entry_titulo.get()
            nome_imagem = self.cb_imagem.get()
            
            df_agrupado = self.df.groupby(col_x).sum()[col_y]
            
            self.ax.bar(df_agrupado.index, df_agrupado.values)
            self.ax.set_xlabel(col_x)
            self.ax.set_ylabel(col_y)
            self.ax.set_title(f"Grafico de Colunas - {col_x} x {col_y}" if not titulo_grafico else titulo_grafico)
            self.ax.set_xticks(range(len(df_agrupado.index)))
            self.ax.set_xticklabels(df_agrupado.index, rotation=45, ha='right')
            
            for i, v in enumerate(df_agrupado.values):
                self.ax.annotate(f'{v:.2f}', xy=(i, v), ha='center', va='bottom')
            
            self.canvas.draw()
            
            # Salvando a imagem
            if nome_imagem:
                caminho_nome_imagem = f'{nome_imagem}.png'
                caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
                self.ax.figure.savefig(caminho_imagem, dpi=80)
            
            self.janela_colunas.destroy()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar o gráfico: {str(e)}")
        
    def criar_grafico_colunas_2(self):
        try:
            self.ax.clear()
            
            col_x = self.cb_eixo_x.get()
            col_y = self.cb_eixo_y.get()
            titulo_grafico = self.entry_titulo.get()
            nome_imagem = self.cb_imagem.get()
            
            df_agrupado = self.df.groupby(col_x).sum()[col_y]
            
            self.ax.bar(df_agrupado.index, df_agrupado.values)
            self.ax.set_xlabel(col_x)
            self.ax.set_ylabel(col_y)
            self.ax.set_title(f"Grafico de Colunas - {col_x} x {col_y}" if not titulo_grafico else titulo_grafico)
            self.ax.set_xticks(range(len(df_agrupado.index)))
            self.ax.set_xticklabels(df_agrupado.index, rotation=45, ha='right')
            self.ax.grid(True, axis='y')
            self.ax.figure.set_size_inches(10, 6)
            
            for i, v in enumerate(df_agrupado.values):
                self.ax.annotate(f'{v:.2f}', xy=(i, v), ha='center', va='bottom')
            
            self.canvas.draw()
            
            # Salvando a imagem
            if nome_imagem:
                caminho_nome_imagem = f'{nome_imagem}.png'
                caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
                self.ax.figure.savefig(caminho_imagem, dpi=80)
            
            self.janela_colunas.destroy()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar o gráfico: {str(e)}")
    
    def abrir_janela_pizza(self):
        try:
            self.janela_pizza = Toplevel(self.master)
            self.janela_pizza.title("Grafico de Pizza")
            self.janela_pizza.geometry("300x300")
            self.janela_pizza.grab_set()
            
            self.lb_eixo_x = ttk.Label(self.janela_pizza, text="Eixo X:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_eixo_x.pack(pady=5)
            
            self.cb_eixo_x = Combobox(self.janela_pizza, values=self.df.columns.tolist())
            self.cb_eixo_x.pack(pady=5)
            
            self.lb_eixo_y = ttk.Label(self.janela_pizza, text="Eixo Y:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_eixo_y.pack(pady=5)
            
            self.cb_eixo_y = Combobox(self.janela_pizza, values=self.df.columns.tolist())
            self.cb_eixo_y.pack(pady=5)
            
            self.lb_titulo = ttk.Label(self.janela_pizza, text="Titulo:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_titulo.pack(pady=5)
            
            self.entry_titulo = Entry(self.janela_pizza, width=20)
            self.entry_titulo.pack(pady=5)
            
            self.lb_imagem = ttk.Label(self.janela_pizza, text="Imagem:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_imagem.pack(pady=5)
            
            self.cb_imagem = Combobox(self.janela_pizza, 
                                    values=['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8'],
                                    style='Dashboard.TCombobox', font=('Segoe UI', 10))
            self.cb_imagem.pack(pady=5)
            
            self.btn_gerar_1 = ttk.Button(self.janela_pizza, text="Grafico 1", style='Dashboard.TButton', command=self.criar_grafico_pizza)
            self.btn_gerar_1.pack(side=LEFT, padx=5, pady=5)

            self.btn_gerar_2 = ttk.Button(self.janela_pizza, text="Grafico 2", style='Dashboard.TButton', command=self.criar_grafico_pizza_2)
            self.btn_gerar_2.pack(side=LEFT, padx=5, pady=5)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir a janela de pizza: {str(e)}")
            self.janela_pizza.destroy()
            
    def criar_grafico_pizza(self):
        try:
            self.ax.clear()
            
            col_x = self.cb_eixo_x.get()
            col_y = self.cb_eixo_y.get()
            titulo_grafico = self.entry_titulo.get()
            nome_imagem = self.cb_imagem.get()
            
            df_agrupado = self.df.groupby(col_x).sum()[col_y]
            
            total = df_agrupado.sum()
            pedacos = [(v / total) * 100 for v in df_agrupado.values]  # calculando o percentual    
            
            self.ax.pie(df_agrupado.values, labels=[f'{label} ({pedacos:.1f} %)' for label, pedacos in zip(df_agrupado.index, pedacos)], autopct='%1.0f%%')
            self.ax.set_title(f"Grafico de Pizza - {col_x} x {col_y}" if not titulo_grafico else titulo_grafico)
            
            for i, v in enumerate(df_agrupado.values):
                self.ax.annotate(f'{v:.2f}', xy=(i, v), ha='center', va='bottom')

            self.canvas.draw()
            
            # Salvando a imagem
            if nome_imagem:
                caminho_nome_imagem = f'{nome_imagem}.png'
                caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
                self.ax.figure.savefig(caminho_imagem, dpi=80)
            
            self.janela_pizza.destroy()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar o gráfico: {str(e)}")
            
    def criar_grafico_pizza_2(self):
        try:
            self.ax.clear()
            
            col_x = self.cb_eixo_x.get()
            col_y = self.cb_eixo_y.get()
            titulo_grafico = self.entry_titulo.get()
            nome_imagem = self.cb_imagem.get()
            
            df_agrupado = self.df.groupby(col_x).sum()[col_y]
            
            total = df_agrupado.sum()
            #pedacos = [(v / total) * 100 for v in df_agrupado.values]  # calculando o percentual    
            
            self.ax.pie(df_agrupado.values, labels=[f'{label} ({value:.0f})' for label, value in zip(df_agrupado.index, df_agrupado.values)])
            self.ax.set_title(f"Grafico de Pizza - {col_x} x {col_y}" if not titulo_grafico else titulo_grafico)
            
            for i, v in enumerate(df_agrupado.values):
                self.ax.annotate(f'{v:.2f}', xy=(i, v), ha='center', va='bottom')
                
            self.canvas.draw()
            
            # Salvando a imagem
            if nome_imagem:
                caminho_nome_imagem = f'{nome_imagem}.png'
                caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
                self.ax.figure.savefig(caminho_imagem, dpi=80)
            
            self.janela_pizza.destroy()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar o gráfico: {str(e)}")
        
    def abrir_janela_linhas(self):
        try:
            self.janela_linhas = Toplevel(self.master)
            self.janela_linhas.title("Grafico de Linhas")
            self.janela_linhas.geometry("300x300")
            self.janela_linhas.grab_set()
            
            self.lb_eixo_x = ttk.Label(self.janela_linhas, text="Eixo X:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_eixo_x.pack(pady=5)
            
            self.cb_eixo_x = Combobox(self.janela_linhas, values=self.df.columns.tolist())
            self.cb_eixo_x.pack(pady=5)
            
            self.lb_eixo_y = ttk.Label(self.janela_linhas, text="Eixo Y:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_eixo_y.pack(pady=5)
            
            self.cb_eixo_y = Combobox(self.janela_linhas, values=self.df.columns.tolist())
            self.cb_eixo_y.pack(pady=5)
            
            self.lb_titulo = ttk.Label(self.janela_linhas, text="Titulo:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_titulo.pack(pady=5)
            
            self.entry_titulo = Entry(self.janela_linhas, width=20)
            self.entry_titulo.pack(pady=5)
            
            self.lb_imagem = ttk.Label(self.janela_linhas, text="Imagem:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_imagem.pack(pady=5)
            
            self.cb_imagem = Combobox(self.janela_linhas, 
                                    values=['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8'],
                                    style='Dashboard.TCombobox', font=('Segoe UI', 10))
            self.cb_imagem.pack(pady=5)
            
            self.btn_gerar_1 = ttk.Button(self.janela_linhas, text="Grafico 1", style='Dashboard.TButton', command=self.criar_grafico_linhas)
            self.btn_gerar_1.pack(side=LEFT, padx=5, pady=5)

            self.btn_gerar_2 = ttk.Button(self.janela_linhas, text="Grafico 2", style='Dashboard.TButton', command=self.criar_grafico_linhas_2)
            self.btn_gerar_2.pack(side=LEFT, padx=5, pady=5)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir a janela de linhas: {str(e)}")
            self.janela_linhas.destroy()
            
    def criar_grafico_linhas(self):
        try:
            self.ax.clear()
            
            col_x = self.cb_eixo_x.get()
            col_y = self.cb_eixo_y.get()
            titulo_grafico = self.entry_titulo.get()
            nome_imagem = self.cb_imagem.get()
            
            df_agrupado = self.df.groupby(col_x).sum()[col_y]
            
            self.ax.plot(df_agrupado.index, df_agrupado.values, marker='o', linestyle='-', color='b')
            self.ax.set_xlabel(col_x)
            self.ax.set_ylabel(col_y)
            self.ax.set_title(f"Grafico de Linhas - {col_x} x {col_y}" if not titulo_grafico else titulo_grafico)
            
            for i, v in enumerate(df_agrupado.values):
                self.ax.annotate(f'{v:.0f}', xy=(df_agrupado.index[i], df_agrupado.values[i]), ha='center', va='bottom')

            self.canvas.draw()
            
            # Salvando a imagem
            if nome_imagem:
                caminho_nome_imagem = f'{nome_imagem}.png'
                caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
                self.ax.figure.savefig(caminho_imagem, dpi=80)
            
            self.janela_linhas.destroy()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar o gráfico: {str(e)}")
            
    def criar_grafico_linhas_2(self):
        try:
            self.ax.clear()
            
            col_x = self.cb_eixo_x.get()
            col_y = self.cb_eixo_y.get()
            titulo_grafico = self.entry_titulo.get()
            nome_imagem = self.cb_imagem.get()
            
            df_agrupado = self.df.groupby(col_x).sum()[col_y]
            
            self.ax.plot(df_agrupado.index, df_agrupado.values, '-o', color='mediumseagreen', linewidth=2, markersize=8)
            self.ax.set_xlabel(col_x)
            self.ax.set_ylabel(col_y)
            self.ax.set_title(f"Grafico de Linhas - {col_x} x {col_y}" if not titulo_grafico else titulo_grafico)
            
            for i, v in enumerate(df_agrupado.values):
                valor_formatado = f'{v:.0f}'.format(v)
                self.ax.annotate(valor_formatado, xy=(df_agrupado.index[i], df_agrupado.values[i]), ha='center', va='bottom', fontsize=10)
            
            self.ax.set_facecolor('white')
            self.ax.grid(color='lightgray', linestyle='--', linewidth=0.5)
            self.ax.set_xticks(range(len(df_agrupado.index)))
            self.ax.set_xticklabels(df_agrupado.index, rotation=45)
            
            self.canvas.draw()
            
            # Salvando a imagem
            if nome_imagem:
                caminho_nome_imagem = f'{nome_imagem}.png'
                caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
                self.ax.figure.savefig(caminho_imagem, dpi=80)
            
            self.janela_linhas.destroy()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar o gráfico: {str(e)}")
        
    def abrir_janela_area(self):
        try:
            self.janela_area = Toplevel(self.master)
            self.janela_area.title("Grafico de Area")
            self.janela_area.geometry("300x300")
            self.janela_area.grab_set()
            
            self.lb_eixo_x = ttk.Label(self.janela_area, text="Eixo X:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_eixo_x.pack(pady=5)
            
            self.cb_eixo_x = Combobox(self.janela_area, values=self.df.columns.tolist())
            self.cb_eixo_x.pack(pady=5)
            
            self.lb_eixo_y = ttk.Label(self.janela_area, text="Eixo Y:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_eixo_y.pack(pady=5)
            
            self.cb_eixo_y = Combobox(self.janela_area, values=self.df.columns.tolist())
            self.cb_eixo_y.pack(pady=5)
            
            self.lb_titulo = ttk.Label(self.janela_area, text="Titulo:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_titulo.pack(pady=5)
            
            self.entry_titulo = Entry(self.janela_area, width=20)
            self.entry_titulo.pack(pady=5)
            
            self.lb_imagem = ttk.Label(self.janela_area, text="Imagem:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_imagem.pack(pady=5)
            
            self.cb_imagem = Combobox(self.janela_area, 
                                    values=['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8'],
                                    style='Dashboard.TCombobox', font=('Segoe UI', 10))
            self.cb_imagem.pack(pady=5)
            
            self.btn_gerar_1 = ttk.Button(self.janela_area, text="Grafico 1", style='Dashboard.TButton', command=self.criar_grafico_area)
            self.btn_gerar_1.pack(side=LEFT, padx=5, pady=5)

            self.btn_gerar_2 = ttk.Button(self.janela_area, text="Grafico 2", style='Dashboard.TButton', command=self.criar_grafico_area_2)
            self.btn_gerar_2.pack(side=LEFT, padx=5, pady=5)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir a janela de area: {str(e)}")
            self.janela_area.destroy()
            
    def criar_grafico_area(self):
        try:
            self.ax.clear()
            
            col_x = self.cb_eixo_x.get()
            col_y = self.cb_eixo_y.get()
            titulo_grafico = self.entry_titulo.get()
            nome_imagem = self.cb_imagem.get()
            
            df_agrupado = self.df.groupby(col_x).sum()[col_y]
            
            self.ax.fill_between(df_agrupado.index, df_agrupado.values, color='lightblue', alpha=0.2)
            
            self.ax.plot(df_agrupado.index, df_agrupado.values, color='mediumseagreen')
            self.ax.set_xlabel(col_x)
            self.ax.set_ylabel(col_y)
            self.ax.set_title(f"Grafico de Area - {col_x} x {col_y}" if not titulo_grafico else titulo_grafico)
            
            for i, v in enumerate(df_agrupado.values):
                self.ax.annotate(f'{v:.0f}', xy=(df_agrupado.index[i], df_agrupado.values[i]), ha='center', va='bottom')

            self.ax.set_facecolor('white')
            self.ax.grid(color='lightgray', linestyle='--', linewidth=0.5)
            self.ax.set_xticks(range(len(df_agrupado.index)))
            self.ax.set_xticklabels(df_agrupado.index, rotation=45)
            
            self.canvas.draw()
            
            # Salvando a imagem
            if nome_imagem:
                caminho_nome_imagem = f'{nome_imagem}.png'
                caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
                self.ax.figure.savefig(caminho_imagem, dpi=80)
            
            self.janela_area.destroy()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar o gráfico: {str(e)}")
            
    def criar_grafico_area_2(self):
        try:
            self.ax.clear()
            
            col_x = self.cb_eixo_x.get()
            col_y = self.cb_eixo_y.get()
            titulo_grafico = self.entry_titulo.get()
            nome_imagem = self.cb_imagem.get()
            
            df_agrupado = self.df.groupby(col_x).sum()[col_y]
            
            self.ax.fill_between(df_agrupado.index, df_agrupado.values, color='lightblue', alpha=0.2)
            
            self.ax.plot(df_agrupado.index, df_agrupado.values, color='red', label=f'{col_y} (linha)')
            self.ax.set_xlabel(col_x)
            self.ax.set_ylabel('A soma de ' + col_y)
            self.ax.legend()
            self.ax.grid(True)
            self.ax.set_title(f"Grafico de Area - {col_x} x {col_y}" if not titulo_grafico else titulo_grafico)
            
            for i, v in enumerate(df_agrupado.values):
                self.ax.annotate(f'{v:.0f}', xy=(df_agrupado.index[i], df_agrupado.values[i]), ha='center', va='bottom')

            self.ax.set_facecolor('white')
            self.ax.grid(color='lightgray', linestyle='--', linewidth=0.5)
            self.ax.set_xticks(range(len(df_agrupado.index)))
            self.ax.set_xticklabels(df_agrupado.index, rotation=45)
            
            self.canvas.draw()
            
            # Salvando a imagem
            if nome_imagem:
                caminho_nome_imagem = f'{nome_imagem}.png'
                caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
                self.ax.figure.savefig(caminho_imagem, dpi=80)
            
            self.janela_area.destroy()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar o gráfico: {str(e)}")
        
    def abrir_janela_funil(self):
        try:
            self.janela_funil = Toplevel(self.master)
            self.janela_funil.title("Grafico de Funil")
            self.janela_funil.geometry("300x300")
            self.janela_funil.grab_set()
            
            self.lb_eixo_x = ttk.Label(self.janela_funil, text="Eixo X:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_eixo_x.pack(pady=5)
            
            self.cb_eixo_x = Combobox(self.janela_funil, values=self.df.columns.tolist())
            self.cb_eixo_x.pack(pady=5)
            
            self.lb_eixo_y = ttk.Label(self.janela_funil, text="Eixo Y:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_eixo_y.pack(pady=5)
            
            self.cb_eixo_y = Combobox(self.janela_funil, values=self.df.columns.tolist())
            self.cb_eixo_y.pack(pady=5)
            
            self.lb_titulo = ttk.Label(self.janela_funil, text="Titulo:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_titulo.pack(pady=5)
            
            self.entry_titulo = Entry(self.janela_funil, width=20)
            self.entry_titulo.pack(pady=5)
            
            self.lb_imagem = ttk.Label(self.janela_funil, text="Imagem:", style='Dashboard.TLabel', font=('Segoe UI', 10))
            self.lb_imagem.pack(pady=5)
            
            self.cb_imagem = Combobox(self.janela_funil, 
                                    values=['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8'],
                                    style='Dashboard.TCombobox', font=('Segoe UI', 10))
            self.cb_imagem.pack(pady=5)
            
            self.btn_gerar_1 = ttk.Button(self.janela_funil, text="Grafico 1", style='Dashboard.TButton', command=self.criar_grafico_funil)
            self.btn_gerar_1.pack(side=LEFT, padx=5, pady=5)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir a janela de funil: {str(e)}")
            self.janela_funil.destroy()
    
    def criar_grafico_funil(self):
        try:
            self.ax.clear()
            
            col_x = self.cb_eixo_x.get()
            col_y = self.cb_eixo_y.get()
            titulo_grafico = self.entry_titulo.get()
            nome_imagem = self.cb_imagem.get()
            
            df_agrupado = self.df.groupby(col_x).sum()[col_y]
            df_agrupado = df_agrupado.sort_values(ascending=True)
            
            perc_acumuladas = (df_agrupado.cumsum() / df_agrupado.sum()) * 100
            
            # Correção do cálculo das alturas usando iloc
            alturas = [perc_acumuladas.iloc[0]] + [
                perc_acumuladas.iloc[i] - perc_acumuladas.iloc[i-1] 
                for i in range(1, len(perc_acumuladas))
            ]

            # lista de cores hexadecimais para o funil
            cores = ['#FF9F55', '#F9D423', '#6FCF97', '#5485EC', '#9B51E0', '#FF6F61', '#FF4D4D', '#33CC33', '#3366FF']
            
            cores = plt.get_cmap('tab10', len(df_agrupado))(np.arange(len(df_agrupado)))

            # cria as barras do funil
            for i, (indice, valor) in enumerate(df_agrupado.items()):
                esquerda = (100 - alturas[i]) / 2
                self.ax.barh(i, alturas[i], left=esquerda, 
                         color=cores[i],
                         alpha=0.7,
                         edgecolor="white")
                label = f"{indice}: {int(valor):,d}"
                largura_barra = alturas[i]
                centraliza_barra = esquerda + largura_barra / 2
                self.ax.text(centraliza_barra, i, label, color='black', fontsize=10, ha='center', va='center')
                
            df_agrupado = df_agrupado.sort_index()
                
            fig, ax = plt.subplots()
            ax.set_axis_off()
            self.ax.axis('off')
            
            self.canvas.draw()
            
            # Salvando a imagem
            if nome_imagem:
                caminho_nome_imagem = f'{nome_imagem}.png'
                caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
                self.ax.figure.savefig(caminho_imagem, dpi=80)
            
            self.janela_funil.destroy()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar o gráfico: {str(e)}")
            
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
