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
            command=self.abrir_janela_dash_1
        )
        self.btn_dash1.grid(row=0, column=0, padx=5, pady=5)
        
        self.btn_dash2 = ttk.Button(
            self.frame_controles,
            text="Dashboard 2",
            style='Dashboard.TButton',
            command=self.abrir_janela_dash_2
        )
        self.btn_dash2.grid(row=0, column=1, padx=5, pady=5)
        
        self.btn_dash3 = ttk.Button(
            self.frame_controles,
            text="Dashboard 3",
            style='Dashboard.TButton',
            command=self.abrir_janela_dash_3
        )
        self.btn_dash3.grid(row=0, column=2, padx=5, pady=5)
        
        self.btn_editar = ttk.Button(
            self.frame_controles,
            text="Editar Dados",
            style='Dashboard.TButton',
            command=self.abrir_janela_editar_dados
        )
        self.btn_editar.grid(row=0, column=3, padx=5, pady=5)
        
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
            
    def abrir_janela_editar_dados(self):
        self.editar_dados = Toplevel(self.master)
        self.editar_dados.title("Editar Dados")
        self.editar_dados.grab_set()
        self.editar_dados.configure(bg=self.cor_bg)
        
        # Menu com estilo personalizado
        menu_editar_dados = Menu(
            self.editar_dados,
            tearoff=0,
            bg=self.cor_primaria,
            fg='white',
            activebackground=self.cor_destaque,
            activeforeground='white'
        )
        self.editar_dados.config(menu=menu_editar_dados)
        
        menu_salvar = Menu(
            menu_editar_dados,
            tearoff=0,
            bg=self.cor_primaria,
            fg='white',
            activebackground=self.cor_destaque,
            activeforeground='white'
        )
        menu_editar_dados.add_cascade(label="Formatar", menu=menu_salvar)
        
        menu_salvar.add_command(label="Renomear colunas", command=self.renomear_colunas)
        menu_salvar.add_command(label="Remover colunas", command=self.remover_colunas)
        menu_salvar.add_command(label="Remover linhas em Branco", command=self.remove_linhas_brancas)
        menu_salvar.add_command(label="Remover linhas Alternadas", command=self.remove_algumas_linhas)
        menu_salvar.add_command(label="Remover linhas Duplicadas", command=self.remover_linhas_duplicadas)
        
        # Frame principal
        frame_principal = ttk.Frame(self.editar_dados, style='Dashboard.TFrame')
        frame_principal.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Título
        titulo = ttk.Label(
            frame_principal,
            text=f"Editar Dados: {','.join(self.df.columns)}",
            style='Dashboard.TLabel',
            font=('Segoe UI', 12, 'bold')
        )
        titulo.pack(pady=10)
        
        # Treeview com estilo personalizado
        style = ttk.Style()
        style.configure(
            "Treeview",
            background=self.cor_bg,
            foreground=self.cor_texto,
            fieldbackground=self.cor_bg,
            font=('Segoe UI', 10)
        )
        style.configure(
            "Treeview.Heading",
            background=self.cor_primaria,
            foreground="white",
            font=('Segoe UI', 10, 'bold')
        )
        
        self.tree = ttk.Treeview(
            frame_principal,
            columns=list(self.df.columns),
            show='headings',
            style="Treeview"
        )
        
        # Scrollbars
        scrolly = ttk.Scrollbar(frame_principal, orient=VERTICAL, command=self.tree.yview)
        scrollx = ttk.Scrollbar(frame_principal, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        # Configurando cabeçalhos e dados
        for col in self.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        for i, row in self.df.iterrows():
            self.tree.insert('', 'end', values=list(row))
            
        # Layout dos componentes
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.tree.pack(fill=BOTH, expand=True)
        
    def renomear_colunas(self):
        janela_renomear_colunas = Toplevel(self.editar_dados)
        janela_renomear_colunas.title("Renomear Colunas")
        largura = 400
        altura = 250
        largura_tela = (self.editar_dados.winfo_screenwidth() - largura) // 2
        altura_tela = (self.editar_dados.winfo_screenheight() - altura) // 2
        janela_renomear_colunas.geometry(f"{largura}x{altura}+{largura_tela}+{altura_tela}")
        janela_renomear_colunas.grab_set()
        
        label_coluna = ttk.Label(
            janela_renomear_colunas,
            text="Selecione a coluna que deseja renomear:",
            style='Dashboard.TLabel',
            font=('Segoe UI', 12, 'bold')
        )
        label_coluna.pack(pady=10)
        
        entry_coluna = Entry(
            janela_renomear_colunas,
            width=20,
            font=('Segoe UI', 10),
        )
        entry_coluna.pack(pady=10)
        
        label_novo_nome = ttk.Label(
            janela_renomear_colunas,
            text="Digite o novo nome para a coluna:",
            style='Dashboard.TLabel',
            font=('Segoe UI', 12, 'bold')
        )
        label_novo_nome.pack(pady=10)
        
        entry_novo_nome = Entry(
            janela_renomear_colunas,
            width=20,
            font=('Segoe UI', 10),
        )
        entry_novo_nome.pack(pady=10)
        
        btn_renomear = ttk.Button(
            janela_renomear_colunas,
            text="Renomear",
            style='Dashboard.TButton',
            command=lambda: self.renomear_coluna_funcao(entry_coluna.get(), entry_novo_nome.get(), janela_renomear_colunas)
        )
        btn_renomear.pack(pady=10)
        
    def remover_colunas(self):
        janela_remover_colunas = Toplevel(self.editar_dados)
        janela_remover_colunas.title("Remover Colunas")
        largura = 400
        altura = 250
        largura_tela = (self.editar_dados.winfo_screenwidth() - largura) // 2
        altura_tela = (self.editar_dados.winfo_screenheight() - altura) // 2
        janela_remover_colunas.geometry(f"{largura}x{altura}+{largura_tela}+{altura_tela}")
        janela_remover_colunas.grab_set()
        
        label_coluna = ttk.Label(
            janela_remover_colunas,
            text="Selecione a coluna que deseja remover:",
            style='Dashboard.TLabel',
            font=('Segoe UI', 12, 'bold')
        )
        label_coluna.pack(pady=10)
        
        entry_coluna = Entry(
            janela_remover_colunas,
            width=20,
            font=('Segoe UI', 10),
        )
        entry_coluna.pack(pady=10)
        
        
        btn_remover = ttk.Button(
            janela_remover_colunas,
            text="Remover",
            style='Dashboard.TButton',
            command=lambda: self.remover_coluna_funcao(entry_coluna.get(), janela_remover_colunas)
        )
        btn_remover.pack(pady=10)
        
    
    def remover_coluna_funcao(self, coluna, janela):
        if coluna in self.df.columns:
            self.df.drop(columns=[coluna], inplace=True)
            janela.destroy()
            self.atualizar_treeview()
            messagebox.showinfo("Sucesso", "Coluna renomeada com sucesso!")
        else:
            messagebox.showerror("Erro", "Coluna não encontrada!")
        
    
    def renomear_coluna_funcao(self, coluna, novo_nome, janela):
        if coluna in self.df.columns:
            self.df.rename(columns={coluna: novo_nome}, inplace=True)
            janela.destroy()
            self.atualizar_treeview()
            messagebox.showinfo("Sucesso", "Coluna renomeada com sucesso!")
        else:
            messagebox.showerror("Erro", "Coluna não encontrada!")
            
    def remove_linhas_brancas(self):
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja remover as linhas em branco?")
        
        if resposta:
            self.df = self.df.dropna(axis=0)  # remover as linhas que tiverem pelo menos um valor nulo
            self.atualizar_treeview()
            messagebox.showinfo("Sucesso", "Linhas removidas com sucesso!")
            
        else:
            messagebox.showinfo("Cancelado", "Remoção de linhas cancelada!")
            
    def remove_algumas_linhas(self, linha_inicio=None, linha_fim=None):
        linha_inicio = int(simpledialog.askstring("Remover Linhas", "Digite o número da linha inicial:"))
        linha_fim = int(simpledialog.askstring("Remover Linhas", "Digite o número da linha final:"))
        
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja remover as linhas de " + str(linha_inicio) + " a " + str(linha_fim) + "?")
        
        if resposta:
            self.df = self.df.drop(range(linha_inicio - 1, linha_fim))
            self.atualizar_treeview()
            messagebox.showinfo("Sucesso", "Linhas removidas com sucesso!")
            
        else:
            messagebox.showinfo("Cancelado", "Remoção de linhas cancelada!")
            
    def remover_linhas_duplicadas(self):
        janela_remover_linhas_duplicadas = Toplevel(self.editar_dados)
        janela_remover_linhas_duplicadas.title("Remover Linhas Duplicadas")
        largura = 400
        altura = 250
        largura_tela = (self.editar_dados.winfo_screenwidth() - largura) // 2
        altura_tela = (self.editar_dados.winfo_screenheight() - altura) // 2
        janela_remover_linhas_duplicadas.geometry(f"{largura}x{altura}+{largura_tela}+{altura_tela}")
        janela_remover_linhas_duplicadas.grab_set()
        
        label_coluna = ttk.Label(
            janela_remover_linhas_duplicadas,
            text="Selecione a coluna que deseja remover:",
            style='Dashboard.TLabel',
            font=('Segoe UI', 12, 'bold')
        )
        label_coluna.pack(pady=10)
        
        entry_coluna = Entry(
            janela_remover_linhas_duplicadas,
            width=20,
            font=('Segoe UI', 10),
        )
        entry_coluna.pack(pady=10)
        
        btn_remover = ttk.Button(
            janela_remover_linhas_duplicadas,
            text="Remover",
            style='Dashboard.TButton',
            command=lambda: self.remover_linha_duplicada_funcao(entry_coluna.get(), janela_remover_linhas_duplicadas)
        )
        btn_remover.pack(pady=10)
        
    
    def remover_linha_duplicada_funcao(self, coluna, janela):
        if coluna in self.df.columns:
            self.df = self.df.drop_duplicates(subset=[coluna], keep='first')
            janela.destroy()
            self.atualizar_treeview()
            messagebox.showinfo("Sucesso", "Linhas duplicadas removidas com sucesso!")
        else:
            messagebox.showerror("Erro", "Coluna não encontrada!")
            
    def atualizar_treeview(self):
        self.tree.delete(*self.tree.get_children())
        
        self.tree['columns'] = list(self.df.columns)
        
        for col in self.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
            
        for i, row in self.df.iterrows():
            values = list(row)
            
            for j, value in enumerate(values):
                if isinstance(value, np.generic):
                    values[j] = np.asscalar(value)
                    
            self.tree.insert('', 'end', values=values)
            
    def abrir_janela_dash_1(self):
        self.dash_1 = Toplevel(self.master)
        self.dash_1.title("Dashboard 1")
        self.dash_1.grab_set()
        
        img1 = Image.open("image1.png")
        img1 = img1.resize((600, 500), Image.LANCZOS)
        self.img1 = ImageTk.PhotoImage(img1)
        
        img2 = Image.open("image2.png")
        img2 = img2.resize((400, 400), Image.LANCZOS)
        self.img2 = ImageTk.PhotoImage(img2)
        
        self.label_1 = Label(self.dash_1, image=self.img1, bd=2, relief=SOLID)
        self.label_1.image = self.img1
        self.label_1.grid(row=0, column=0, padx=5, pady=5)
        
        self.label_2 = Label(self.dash_1, image=self.img2, bd=2, relief=SOLID)
        self.label_2.image = self.img2
        self.label_2.grid(row=0, column=1, padx=5, pady=5)
        
        self.dash_1.mainloop()
        
    def abrir_janela_dash_2(self):
        self.dash_2 = Toplevel(self.master)
        self.dash_2.title("Dashboard 2")
        self.dash_2.grab_set()
        
        img1 = Image.open("image1.png").resize((400, 400), Image.LANCZOS)
        self.img1 = ImageTk.PhotoImage(img1)
        
        img2 = Image.open("image2.png").resize((400, 400), Image.LANCZOS)
        self.img2 = ImageTk.PhotoImage(img2)
        
        img3 = Image.open("image3.png").resize((400, 400), Image.LANCZOS)
        self.img3 = ImageTk.PhotoImage(img3)
        
        img4 = Image.open("image4.png").resize((400, 400), Image.LANCZOS)
        self.img4 = ImageTk.PhotoImage(img4)
        
        self.label_1 = Label(self.dash_2, image=self.img1, bd=2, relief=SOLID)
        self.label_1.image = self.img1 
        self.label_1.grid(row=0, column=0, padx=5, pady=5)
        
        self.label_2 = Label(self.dash_2, image=self.img2, bd=2, relief=SOLID)
        self.label_2.image = self.img2
        self.label_2.grid(row=0, column=1, padx=5, pady=5)
        
        self.label_3 = Label(self.dash_2, image=self.img3, bd=2, relief=SOLID)
        self.label_3.image = self.img3
        self.label_3.grid(row=1, column=0, padx=5, pady=5)
        
        self.label_4 = Label(self.dash_2, image=self.img4, bd=2, relief=SOLID)
        self.label_4.image = self.img4
        self.label_4.grid(row=1, column=1, padx=5, pady=5)
        
        self.dash_2.mainloop()
        
    def abrir_janela_dash_3(self):
        self.dash_3 = Toplevel(self.master)
        self.dash_3.title("Dashboard 3")
        self.dash_3.grab_set()
        
        img1 = Image.open("image1.png").resize((400, 400), Image.LANCZOS)
        self.img1 = ImageTk.PhotoImage(img1)
        
        img2 = Image.open("image2.png").resize((400, 400), Image.LANCZOS)
        self.img2 = ImageTk.PhotoImage(img2)
        
        img3 = Image.open("image3.png").resize((400, 400), Image.LANCZOS)
        self.img3 = ImageTk.PhotoImage(img3)
        
        img4 = Image.open("image4.png").resize((400, 400), Image.LANCZOS)
        self.img4 = ImageTk.PhotoImage(img4)
        
        img5 = Image.open("image5.png").resize((400, 400), Image.LANCZOS)
        self.img5 = ImageTk.PhotoImage(img5)
        
        img6 = Image.open("image6.png").resize((400, 400), Image.LANCZOS)
        self.img6 = ImageTk.PhotoImage(img6)
        
        self.label_1 = Label(self.dash_3, image=self.img1, bd=2, relief=SOLID)
        self.label_1.image = self.img1 
        self.label_1.grid(row=0, column=0, padx=5, pady=5)
        
        self.label_2 = Label(self.dash_3, image=self.img2, bd=2, relief=SOLID)
        self.label_2.image = self.img2
        self.label_2.grid(row=0, column=1, padx=5, pady=5)
        
        self.label_3 = Label(self.dash_3, image=self.img3, bd=2, relief=SOLID)
        self.label_3.image = self.img3
        self.label_3.grid(row=0, column=2, padx=5, pady=5)
        
        self.label_4 = Label(self.dash_3, image=self.img4, bd=2, relief=SOLID)
        self.label_4.image = self.img4
        self.label_4.grid(row=1, column=0, padx=5, pady=5)
        
        self.label_5 = Label(self.dash_3, image=self.img5, bd=2, relief=SOLID)
        self.label_5.image = self.img5
        self.label_5.grid(row=1, column=1, padx=5, pady=5)
        
        self.label_6 = Label(self.dash_3, image=self.img6, bd=2, relief=SOLID)
        self.label_6.image = self.img6
        self.label_6.grid(row=1, column=2, padx=5, pady=5)
        
        self.dash_3.mainloop()
    
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
