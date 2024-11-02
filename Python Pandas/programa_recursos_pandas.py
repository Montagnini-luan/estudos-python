import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, simpledialog, ttk
import pandas as pd
import numpy as np  
from pandastable import Table
import os
import re


class ExcelEditor:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        
        # Definindo cores corporativas
        self.cor_primaria = "#2c3e50"  # Azul escuro
        self.cor_secundaria = "#ecf0f1"  # Cinza claro
        self.cor_destaque = "#3498db"  # Azul claro
        
        # Configurando o estilo da janela
        self.master.configure(bg=self.cor_secundaria)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configurando estilos personalizados
        self.style.configure("Treeview",
                           background=self.cor_secundaria,
                           foreground=self.cor_primaria,
                           rowheight=25,
                           fieldbackground=self.cor_secundaria)
        
        self.style.configure("Treeview.Heading",
                           background=self.cor_primaria,
                           foreground=self.cor_secundaria,
                           relief="flat")
        
        self.style.map("Treeview.Heading",
                      background=[('active', self.cor_destaque)])
        
        # Frame principal
        self.main_frame = Frame(self.master, bg=self.cor_secundaria)
        self.main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Label de resultado com estilo moderno
        self.resultado_frame = Frame(self.main_frame, bg=self.cor_secundaria)
        self.resultado_frame.pack(fill=X, pady=(0, 10))
        
        self.resultado_label = Label(
            self.resultado_frame,
            text="Total: ",
            font=("Segoe UI", 12),
            bg=self.cor_secundaria,
            fg=self.cor_primaria
        )
        self.resultado_label.pack(side=LEFT, padx=5)
        
        self.df = pd.DataFrame()
        self.tree = None
        self.table = None
        self.file_name = ''

        self.criar_widgets()
        self.tree.bind('<Double-1>', self.editar_itens)
    
    def criar_widgets(self) -> None:
        # Estilo moderno para o menu
        menu_bar = tk.Menu(self.master, bg=self.cor_primaria, fg=self.cor_secundaria)
        
        # Configurando estilos do menu
        menu_config = {'tearoff': 0,
                      'bg': self.cor_primaria,
                      'fg': self.cor_secundaria,
                      'activebackground': self.cor_destaque,
                      'activeforeground': 'white'}
        
        ''' Menu de Arquivo '''
        menu_de_arquivo = tk.Menu(menu_bar, **menu_config)
        menu_bar.add_cascade(label="Arquivo", menu=menu_de_arquivo)
        menu_de_arquivo.add_command(label="Abrir", command=self.carregar_excel)
        menu_de_arquivo.add_separator()
        menu_de_arquivo.add_command(label="Salvar Como", command=self.salvar_como)
        menu_de_arquivo.add_separator()
        menu_de_arquivo.add_command(label="Sair", command=self.master.destroy)
        
        ''' Menu de Editar '''
        menu_de_editar = tk.Menu(menu_bar, **menu_config)
        menu_bar.add_cascade(label="Editar", menu=menu_de_editar)
        menu_de_editar.add_command(label="Renomear Coluna", command=self.renomear_coluna)
        menu_de_editar.add_command(label="Remover Coluna", command=self.remover_colunas)
        menu_de_editar.add_command(label="Filtrar", command=self.filtrar)
        menu_de_editar.add_command(label="Pivot", command=self.master.destroy)
        menu_de_editar.add_command(label="Agrupar", command=self.agrupar)
        menu_de_editar.add_command(label="Remover Linhas em Branco", command=self.remover_linhas_em_branco)
        menu_de_editar.add_command(label="Remover Linhas Alternadas", command=self.remove_algumas_linhas)
        menu_de_editar.add_command(label="Remover Duplicatas", command=self.remover_duplicatas)
        
        ''' Menu de Merge '''
        menu_de_merge = tk.Menu(menu_bar, **menu_config)
        menu_bar.add_cascade(label="Merge", menu=menu_de_merge)
        menu_de_merge.add_command(label="Merge", command=self.master.destroy)
        menu_de_merge.add_command(label="Inner Join", command=self.inner_join)
        menu_de_merge.add_command(label="Join Full", command=self.inner_join_full)
        menu_de_merge.add_command(label="Left Join", command=self.inner_join_left)
        menu_de_merge.add_command(label="Merge Outer", command=self.merge_outer)
        
        ''' Menu de Relatórios '''
        menu_de_relatorios = tk.Menu(menu_bar, **menu_config)
        menu_bar.add_cascade(label="Relatórios", menu=menu_de_relatorios)
        menu_de_relatorios.add_command(label="Consolidar", command=self.consolidar_arquivos)
        menu_de_relatorios.add_command(label="Quebra", command=self.quebrar_arquivos)
        
        self.master.config(menu=menu_bar)
        
        # Frame para a Treeview com barra de rolagem
        self.tree_frame = Frame(self.main_frame, bg=self.cor_secundaria)
        self.tree_frame.pack(fill=BOTH, expand=True)
        
        # Criando a Treeview com estilo moderno
        self.tree = ttk.Treeview(self.tree_frame)
        
        # Adicionando barras de rolagem
        vsb = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self.tree_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        # Posicionando os elementos
        vsb.pack(side=RIGHT, fill=Y)
        hsb.pack(side=BOTTOM, fill=X)
        self.tree.pack(fill=BOTH, expand=True)
        
        # Adicionar tooltips aos menus
        self.criar_tooltips()
        
        # Adicionar barra de status
        self.status_bar = Label(self.master, 
                               text="Pronto", 
                               bd=1, 
                               relief=SUNKEN, 
                               anchor=W,
                               bg=self.cor_secundaria,
                               fg=self.cor_primaria)
        self.status_bar.pack(side=BOTTOM, fill=X)
        
        # Bind de eventos
        self.tree.bind('<Double-1>', self.editar_itens)
        self.tree.bind('<Delete>', lambda e: self.remover_linha())
        self.master.bind('<Control-s>', lambda e: self.salvar_como())
        self.master.bind('<Control-o>', lambda e: self.carregar_excel())
    
    def criar_tooltips(self) -> None:
        # Implementar tooltips para os menus
        pass
    
    def remover_linha(self) -> None:
        try:
            selected_item = self.tree.selection()[0]
            indice = self.tree.index(selected_item)
            self.df = self.df.drop(self.df.index[indice])
            self.tree.delete(selected_item)
            self.soma_colunas_valor()
            self.status_bar.config(text="Linha removida com sucesso")
        except IndexError:
            messagebox.showerror("Erro", "Selecione uma linha para remover")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao remover linha: {str(e)}")
    
    def soma_colunas_valor(self) -> None:
        resultados = []

        for coluna in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[coluna]):
                valores_numericos = self.df[coluna][0:]
                valores_numericos = pd.to_numeric(valores_numericos, errors='coerce') # converte para float
                valores_numericos = valores_numericos[~np.isnan(valores_numericos)] # remove os valores NaN
                
                soma = valores_numericos.sum()
                
                resultado = f'A soma da coluna {coluna} é {soma}'
                resultados.append(resultado)
                
        self.resultado_label.config(text="\n".join(resultados))
                

    def carregar_excel(self) -> None:
        tipo_de_arquivo = (('Excel files', '*.xlsx;*.xls'), ('All files', '*.*'))
        self.nome_do_arquivo = filedialog.askopenfilename(title="Selecione o Arquivo", filetypes=tipo_de_arquivo)
        
        try:
            self.df = pd.read_excel(self.nome_do_arquivo)
            self.atualiza_treeview()
        except Exception as e:
            messagebox.showerror("Erro ao carregar o arquivo", f"Erro ao carregar o arquivo: {e}")
            
        self.soma_colunas_valor()
            
    def atualiza_treeview(self) -> None:
        self.tree.delete(*self.tree.get_children())
        
        # Configura as colunas
        self.tree['columns'] = list(self.df.columns)
        self.tree['show'] = 'headings'  # Remove a coluna de índice vazia
        
        # Configura os cabeçalhos e ajusta as larguras
        for column in self.df.columns:
            self.tree.heading(column, text=column)
            # Ajusta a largura baseado no conteúdo
            max_width = max(
                len(str(self.df[column].max())),
                len(column)
            ) * 10
            self.tree.column(column, width=max_width)
        
        # Insere os dados de forma mais eficiente
        data = self.df.values.tolist()
        for row in data:
            # Converte valores numpy para Python nativos
            formatted_row = [val.item() if hasattr(val, 'item') else val for val in row]
            self.tree.insert('', 'end', values=formatted_row)
            
    def renomear_coluna(self) -> None:
        janela_renomear = tk.Toplevel(self.master)
        janela_renomear.title("Renomear Coluna")
        janela_renomear.configure(bg=self.cor_secundaria)
        
        largura_janela = 400
        altura_janela = 400
        
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()
        
        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)
        
        janela_renomear.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        
        # Estilo moderno para a janela de renomear
        frame_renomear = Frame(janela_renomear, bg=self.cor_secundaria, padx=20, pady=20)
        frame_renomear.pack(fill=BOTH, expand=True)
        
        Label(frame_renomear,
              text="Renomear Coluna",
              font=("Segoe UI", 14, "bold"),
              bg=self.cor_secundaria,
              fg=self.cor_primaria).pack(pady=(0, 20))
        
        label_coluna = Label(frame_renomear, text="Digite o nome da coluna que deseja renomear:", font=("Arial", 12))
        label_coluna.pack(pady=10)
        entry_coluna = Entry(frame_renomear, font=("Arial", 12))
        entry_coluna.pack(pady=10)
        
        label_novo_nome = Label(frame_renomear, text="Digite o novo nome da coluna:", font=("Arial", 12))
        label_novo_nome.pack(pady=10)
        entry_novo_nome = Entry(frame_renomear, font=("Arial", 12))
        entry_novo_nome.pack(pady=10)
        
        botao_renomear = Button(frame_renomear, text="Renomear", font=("Arial", 12), 
                                command=lambda: self.renomear_coluna_confirmar(entry_coluna.get(), entry_novo_nome.get(), frame_renomear))
        
        botao_renomear.pack(pady=10)
        
        janela_renomear.mainloop()
        
    def remove_algumas_linhas(self) -> None:
        janela_remover_linhas = tk.Toplevel(self.master)
        janela_remover_linhas.title("Remover Linhas")
        janela_remover_linhas.configure(bg=self.cor_secundaria)
        
        largura_janela = 400
        altura_janela = 400
        
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()
        
        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)
        
        janela_remover_linhas.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        
        # Estilo moderno para a janela de renomear
        frame_remover_linhas = Frame(janela_remover_linhas, bg=self.cor_secundaria, padx=20, pady=20)
        frame_remover_linhas.pack(fill=BOTH, expand=True)
        
        Label(frame_remover_linhas,
              text="Renomear Coluna",
              font=("Segoe UI", 14, "bold"),
              bg=self.cor_secundaria,
              fg=self.cor_primaria).pack(pady=(0, 20))
        
        label_linha_inicio = Label(frame_remover_linhas, text="Digite o número da linha inicial:", font=("Arial", 12))
        label_linha_inicio.pack(pady=10)
        entry_linha_inicio = Entry(frame_remover_linhas, font=("Arial", 12))
        entry_linha_inicio.pack(pady=10)
        
        label_linha_fim = Label(frame_remover_linhas, text="Digite o número da linha final:", font=("Arial", 12))
        label_linha_fim.pack(pady=10)
        entry_linha_fim = Entry(frame_remover_linhas, font=("Arial", 12))
        entry_linha_fim.pack(pady=10)
        
        botao_remover = Button(frame_remover_linhas, text="Remover", font=("Arial", 12), 
                                command=lambda: self.funcao_remove_algumas_linhas(entry_linha_inicio.get(), entry_linha_fim.get(), janela_remover_linhas))
        
        botao_remover.pack(pady=10)
        
        janela_remover_linhas.mainloop()
        
    def funcao_remove_algumas_linhas(self, linha_inicio, linha_fim, janela_remover_linhas) -> None:
        if linha_inicio and linha_fim:
            self.df = self.df.drop(self.df.index[int(linha_inicio)-1:int(linha_fim)])
            self.atualiza_treeview()
            self.soma_colunas_valor()
            janela_remover_linhas.destroy()
        else:
            messagebox.showerror("Erro", "Número de linha inválido")  
        
    def renomear_coluna_confirmar(self, coluna, novo_nome, janela_renomear) -> None:
        if novo_nome:
            self.df = self.df.rename(columns={coluna: novo_nome})
            self.atualiza_treeview()
            self.soma_colunas_valor()
            janela_renomear.destroy()
        else:
            messagebox.showerror("Erro", "Nome da coluna não pode ser vazio")
            
    def remover_linhas_em_branco(self) -> None:
        resposta = messagebox.askyesno("Remover Linhas em Branco", "Tem certeza que deseja remover as linhas em branco?")
        
        if resposta == 1:
            self.df = self.df.dropna(axis=0)
            self.atualiza_treeview()
            self.soma_colunas_valor()
            
    def remover_duplicatas(self) -> None:
        janela_remover_duplicatas = tk.Toplevel(self.master)
        janela_remover_duplicatas.title("Remover Duplicatas")
        janela_remover_duplicatas.configure(bg=self.cor_secundaria)
        
        largura_janela = 500
        altura_janela = 400
        
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()
        
        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)
        
        janela_remover_duplicatas.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        
        # Estilo moderno para a janela de renomear
        frame_remover_duplicatas = Frame(janela_remover_duplicatas, bg=self.cor_secundaria, padx=20, pady=20)
        frame_remover_duplicatas.pack(fill=BOTH, expand=True)
        
        Label(frame_remover_duplicatas,
              text="Renomear Coluna",
              font=("Segoe UI", 14, "bold"),
              bg=self.cor_secundaria,
              fg=self.cor_primaria).pack(pady=(0, 20))
        
        label_coluna = Label(frame_remover_duplicatas, text="Digite o nome da coluna que deseja remover as duplicatas:", font=("Arial", 12))
        label_coluna.pack(pady=10)
        entry_coluna = Entry(frame_remover_duplicatas, font=("Arial", 12))
        entry_coluna.pack(pady=10)
        
        botao_remover = Button(frame_remover_duplicatas, text="Remover", font=("Arial", 12), 
                                command=lambda: self.funcao_remove_duplicatas(entry_coluna.get(), janela_remover_duplicatas))
        
        botao_remover.pack(pady=10)
        
        janela_remover_duplicatas.mainloop()
        
    def funcao_remove_duplicatas(self, coluna, janela_remover_duplicatas) -> None:
        if coluna:
            self.df = self.df.drop_duplicates(subset=[coluna], keep='first')  # keep='first' mantém a primeira ocorrência e remove as duplicatas
            self.atualiza_treeview()
            self.soma_colunas_valor()
            janela_remover_duplicatas.destroy()
        else:
            messagebox.showerror("Erro", "Nome da coluna não pode ser vazio")
            
    def remover_colunas(self) -> None:
        remover_colunas = tk.Toplevel(self.master)
        remover_colunas.title("Remover Colunas")
        remover_colunas.configure(bg=self.cor_secundaria)
        
        largura_janela = 500
        altura_janela = 400
        
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()
        
        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)
        
        remover_colunas.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        
        # Estilo moderno para a janela de renomear
        frame_remover_colunas = Frame(remover_colunas, bg=self.cor_secundaria, padx=20, pady=20)
        frame_remover_colunas.pack(fill=BOTH, expand=True)
        
        Label(frame_remover_colunas,
              text="Renomear Coluna",
              font=("Segoe UI", 14, "bold"),
              bg=self.cor_secundaria,
              fg=self.cor_primaria).pack(pady=(0, 20))
        
        label_coluna = Label(frame_remover_colunas, text="Digite o nome da coluna que deseja remover:", font=("Arial", 12))
        label_coluna.pack(pady=10)
        entry_coluna = Entry(frame_remover_colunas, font=("Arial", 12))
        entry_coluna.pack(pady=10)
        
        botao_remover = Button(frame_remover_colunas, text="Remover", font=("Arial", 12), 
                                command=lambda: self.funcao_remove_colunas(entry_coluna.get(), remover_colunas))
        
        botao_remover.pack(pady=10)
        
        remover_colunas.mainloop()
        
    def funcao_remove_colunas(self, coluna, remover_colunas) -> None:
        if coluna:
            self.df = self.df.drop(columns=[coluna])
            self.atualiza_treeview()
            self.soma_colunas_valor()
            remover_colunas.destroy()
        else:
            messagebox.showerror("Erro", "Nome da coluna não pode ser vazio")
            
    def filtrar(self) -> None:
        filtrar = tk.Toplevel(self.master)
        filtrar.title("Filtrar")
        filtrar.configure(bg=self.cor_secundaria)
        
        largura_janela = 500
        altura_janela = 400
        
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()
        
        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)
        
        filtrar.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        
        # Estilo moderno para a janela de renomear
        frame_filtrar = Frame(filtrar, bg=self.cor_secundaria, padx=20, pady=20)
        frame_filtrar.pack(fill=BOTH, expand=True)
        
        Label(frame_filtrar,
              text="Filtrar",
              font=("Segoe UI", 14, "bold"),
              bg=self.cor_secundaria,
              fg=self.cor_primaria).pack(pady=(0, 20))
        
        label_coluna = Label(frame_filtrar, text="Digite o nome da coluna que deseja filtrar:", font=("Arial", 12))
        label_coluna.pack(pady=10)
        entry_coluna = Entry(frame_filtrar, font=("Arial", 12))
        entry_coluna.pack(pady=10)
        
        label_valor = Label(frame_filtrar, text="Digite o valor que deseja filtrar:", font=("Arial", 12))
        label_valor.pack(pady=10)
        entry_valor = Entry(frame_filtrar, font=("Arial", 12))
        entry_valor.pack(pady=10)
        
        botao_filtrar = Button(frame_filtrar, text="Filtrar", font=("Arial", 12), 
                                command=lambda: self.funcao_filtrar(entry_coluna.get(), entry_valor.get(), filtrar))
        
        botao_filtrar.pack(pady=10)
        
        filtrar.mainloop()
        
    def funcao_filtrar(self, coluna, valor, filtrar) -> None:
        if coluna and valor:
            self.df = self.df[self.df[coluna] == valor]
            self.atualiza_treeview()
            filtrar.destroy()
        else:
            messagebox.showerror("Erro", "Nome da coluna ou valor não pode ser vazio")
            
    def agrupar(self) -> None:
        agrupar = tk.Toplevel(self.master)
        agrupar.title("Agrupar")
        agrupar.configure(bg=self.cor_secundaria)
        
        largura_janela = 500
        altura_janela = 400
        
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()
        
        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)
        
        agrupar.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        
        # Estilo moderno para a janela de renomear
        frame_agrupar = Frame(agrupar, bg=self.cor_secundaria, padx=20, pady=20)
        frame_agrupar.pack(fill=BOTH, expand=True)
        
        Label(frame_agrupar,
              text="Filtrar",
              font=("Segoe UI", 14, "bold"),
              bg=self.cor_secundaria,
              fg=self.cor_primaria).pack(pady=(0, 20))
        
        label_coluna = Label(frame_agrupar, text="Digite o nome da coluna que deseja agrupar:", font=("Arial", 12))
        label_coluna.pack(pady=10)
        entry_coluna = Entry(frame_agrupar, font=("Arial", 12))
        entry_coluna.pack(pady=10)
        
        botao_agrupar = Button(frame_agrupar, text="Agrupar", font=("Arial", 12), 
                                command=lambda: self.funcao_agrupar(entry_coluna.get(), agrupar))
        
        botao_agrupar.pack(pady=10)
        
        agrupar.mainloop()
        
    def funcao_agrupar(self, coluna, agrupar) -> None:
        self.tree.delete(*self.tree.get_children())
        
        if coluna:
            groupy_dados = self.df.groupby(coluna).sum()
            
            for i, linha in groupy_dados.iterrows():
                values = list(linha)
                
                for j, value in enumerate(values):
                    
                    if isinstance(value, np.generic):
                        values[j] = np.asscalar(value)
                        
                self.tree.insert('', tk.END, values = [i] + values)
                
            agrupar.destroy()
        else:
            messagebox.showerror("Erro", "Nome da coluna não pode ser vazio")
            
    def inner_join(self) -> None:
        tipo_de_arquivo = (('Excel files', '*.xlsx;*.xls'), ('All files', '*.*'))
        nome_do_arquivo1 = filedialog.askopenfilename(title="Selecione o primeiro Arquivo", filetypes=tipo_de_arquivo)
        nome_do_arquivo2 = filedialog.askopenfilename(title="Selecione o segundo Arquivo", filetypes=tipo_de_arquivo)
        
        arquivo1 = pd.read_excel(nome_do_arquivo1)
        arquivo2 = pd.read_excel(nome_do_arquivo2)
        
        coluna_join = simpledialog.askstring("Coluna de Join", "Digite o nome da coluna que deseja usar para o join:")
        
        self.df = pd.merge(arquivo1, arquivo2, on=coluna_join, how='inner')  # inner join
        self.atualiza_treeview()
        self.soma_colunas_valor()
        
    def inner_join_full(self) -> None:
        tipo_de_arquivo = (('Excel files', '*.xlsx;*.xls'), ('All files', '*.*'))
        nome_do_arquivo1 = filedialog.askopenfilename(title="Selecione o primeiro Arquivo", filetypes=tipo_de_arquivo)
        nome_do_arquivo2 = filedialog.askopenfilename(title="Selecione o segundo Arquivo", filetypes=tipo_de_arquivo)
        
        arquivo1 = pd.read_excel(nome_do_arquivo1)
        arquivo2 = pd.read_excel(nome_do_arquivo2)
        
        self.df = pd.concat([arquivo1, arquivo2])
        
        self.atualiza_treeview()
        self.soma_colunas_valor()
        
    def inner_join_left(self) -> None:
        tipo_de_arquivo = (('Excel files', '*.xlsx;*.xls'), ('All files', '*.*'))
        nome_do_arquivo1 = filedialog.askopenfilename(title="Selecione o primeiro Arquivo", filetypes=tipo_de_arquivo)
        nome_do_arquivo2 = filedialog.askopenfilename(title="Selecione o segundo Arquivo", filetypes=tipo_de_arquivo)
        
        coluna_join = simpledialog.askstring("Coluna de Join", "Digite o nome da coluna que deseja usar para o join:")
        
        arquivo1 = pd.read_excel(nome_do_arquivo1)
        arquivo2 = pd.read_excel(nome_do_arquivo2)
        
        self.df = pd.merge(arquivo1, arquivo2, on=coluna_join, how='left')  # left join
        self.df = self.df.dropna()
        
        self.atualiza_treeview()
        self.soma_colunas_valor()
        
    def merge_outer(self) -> None:
        tipo_de_arquivo = (('Excel files', '*.xlsx;*.xls'), ('All files', '*.*'))
        nome_do_arquivo1 = filedialog.askopenfilename(title="Selecione o primeiro Arquivo", filetypes=tipo_de_arquivo)
        nome_do_arquivo2 = filedialog.askopenfilename(title="Selecione o segundo Arquivo", filetypes=tipo_de_arquivo)
        
        coluna_join = simpledialog.askstring("Coluna de Join", "Digite o nome da coluna que deseja usar para o join:")
        
        arquivo1 = pd.read_excel(nome_do_arquivo1)
        arquivo2 = pd.read_excel(nome_do_arquivo2)
        
        self.df = pd.merge(arquivo1, arquivo2, on=coluna_join, how='outer')
        self.df = self.df.dropna()
        
        self.atualiza_treeview()
        self.soma_colunas_valor()
        
    def salvar_como(self) -> None:
        tipo_de_arquivo = (('Excel files', '*.xlsx;*.xls'), ('All files', '*.*'))
        nome_do_arquivo = filedialog.asksaveasfilename(title="Salvar como", filetypes=tipo_de_arquivo, defaultextension=".xlsx")
        
        if nome_do_arquivo:
            self.df.to_excel(nome_do_arquivo, index=False)
        else:
            messagebox.showerror("Erro", "Nome do arquivo não pode ser vazio")
            
    def editar_itens(self, event) -> None:
        try:
            item_selecionado = self.tree.selection()[0]
            valores = self.tree.item(item_selecionado, 'values')
            
            janela_editar_itens = tk.Toplevel(self.master)
            janela_editar_itens.title("Editar Itens")
            janela_editar_itens.configure(bg=self.cor_secundaria)
            
            # Centralizar a janela
            largura_janela = 400
            altura_janela = 400
            largura_tela = self.master.winfo_screenwidth()
            altura_tela = self.master.winfo_screenheight()
            posicao_x = (largura_tela // 2) - (largura_janela // 2)
            posicao_y = (altura_tela // 2) - (altura_janela // 2)
            janela_editar_itens.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
            
            # Frame para organizar os widgets
            frame_edicao = Frame(janela_editar_itens, bg=self.cor_secundaria, padx=20, pady=20)
            frame_edicao.pack(fill=BOTH, expand=True)
            
            entries = []  # Lista para armazenar as entries
            
            for i, coluna in enumerate(self.df.columns):
                label_coluna = Label(frame_edicao, 
                                   text=coluna, 
                                   font=("Segoe UI", 12),
                                   bg=self.cor_secundaria,
                                   fg=self.cor_primaria)
                label_coluna.grid(row=i, column=0, padx=10, pady=5, sticky='e')
                
                entry_coluna = Entry(frame_edicao, 
                                   font=("Segoe UI", 12),
                                   bg="white",
                                   fg=self.cor_primaria)
                entry_coluna.insert(0, valores[i])
                entry_coluna.grid(row=i, column=1, padx=10, pady=5, sticky='ew')
                entries.append(entry_coluna)
            
            frame_edicao.grid_columnconfigure(1, weight=1)
            
            # Frame para botões
            frame_botoes = Frame(frame_edicao, bg=self.cor_secundaria)
            frame_botoes.grid(row=len(self.df.columns), column=0, columnspan=2, pady=20)
            
            botao_salvar = Button(frame_botoes, 
                                text="Salvar", 
                                font=("Segoe UI", 12),
                                bg=self.cor_primaria,
                                fg=self.cor_secundaria,
                                activebackground=self.cor_destaque,
                                activeforeground="white",
                                command=lambda: self.salvar_alteracoes(item_selecionado, entries, janela_editar_itens))
            
            botao_salvar.pack(side=LEFT, padx=5)
            
            botao_cancelar = Button(frame_botoes,
                                  text="Cancelar",
                                  font=("Segoe UI", 12),
                                  bg=self.cor_primaria,
                                  fg=self.cor_secundaria,
                                  activebackground=self.cor_destaque,
                                  activeforeground="white",
                                  command=janela_editar_itens.destroy)
            
            botao_cancelar.pack(side=LEFT, padx=5)
            
        except IndexError:
            messagebox.showerror("Erro", "Por favor, selecione um item para editar.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao editar: {str(e)}")

    def salvar_alteracoes(self, item_selecionado, entries, janela_editar_itens) -> None:
        try:
            novo_valor = [entry.get() for entry in entries]
            
            # Converter valores para tipos compatíveis
            for i, valor in enumerate(novo_valor):
                coluna = self.df.columns[i]
                if pd.api.types.is_numeric_dtype(self.df[coluna]):
                    try:
                        novo_valor[i] = pd.to_numeric(valor)
                    except ValueError:
                        messagebox.showerror("Erro", f"Valor inválido para a coluna {coluna}")
                        return
            
            indice = self.tree.index(item_selecionado)
            self.df.iloc[indice] = novo_valor
            self.tree.item(item_selecionado, values=novo_valor)
            self.soma_colunas_valor()
            janela_editar_itens.destroy()
            messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar alterações: {str(e)}")
        
    def consolidar_arquivos(self) -> None:
        try:
            
            """seleciona a pasta que contém os arquivos a serem consolidados"""
            
            caminho_pasta = filedialog.askdirectory(title="Selecione a pasta que contém os arquivos a serem consolidados")
            lista_arquivos = os.listdir(caminho_pasta)
            
            lista_caminho_e_arquivos_excel = [caminho_pasta + "\\" + arquivo for arquivo in lista_arquivos if arquivo.endswith('.xlsx') or arquivo.endswith('.xls')]
            
            dados_arquivos = pd.DataFrame()
            
            for arquivo in lista_caminho_e_arquivos_excel:
                dados = pd.read_excel(arquivo)
                dados_arquivos = pd.concat([dados_arquivos, dados], ignore_index=True)
                
            self.df = dados_arquivos
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consolidar arquivos: {e}")
        
        self.atualiza_treeview()
        self.soma_colunas_valor()
        
    def quebrar_arquivos(self) -> None:
        coluna = simpledialog.askstring("Coluna de Quebra", "Digite o nome da coluna que deseja usar para quebrar o arquivo:")
        
        if coluna:
            grupos = self.df.groupby(coluna)
            pasta_salvar = filedialog.askdirectory(title="Selecione a pasta onde deseja salvar os arquivos quebrados")
            
            if pasta_salvar:
                for valor, grupo in grupos:
                    nome_arquivo = re.sub(r'[^\w\-_\. ]', '_', f'{coluna}_{valor}.xlsx')
                    caminho_arquivo = os.path.join(pasta_salvar, nome_arquivo)
                    grupo.to_excel(caminho_arquivo, index=False)
                    
                messagebox.showinfo("Sucesso", "Arquivos quebrados com sucesso")
            else:
                messagebox.showerror("Erro", "Pasta de salvamento não selecionada")
        else:
            messagebox.showerror("Erro", "Nome da coluna não pode ser vazio")

def main():
    janela = Tk()
    janela.title("Editor de Excel com Pandas")
    janela.geometry("800x600")
    
    # Configurando o ícone da janela (opcional)
    # janela.iconbitmap('caminho_para_seu_icone.ico')
    
    # Definindo um tamanho mínimo para a janela
    janela.minsize(600, 400)
    
    editor = ExcelEditor(janela)
    janela.mainloop()

if __name__ == "__main__":
    main()
    