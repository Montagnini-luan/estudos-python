import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime
from tkcalendar import DateEntry
import os

class SistemaReservas:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Reservas de Passagens")
        
        # Definindo cores
        self.cor_bg = "#f0f2f5"
        self.cor_primaria = "#1a237e"
        self.cor_secundaria = "#283593"
        self.cor_destaque = "#3949ab"
        self.cor_texto = "#212121"
        
        # Configurando a janela
        self.master.configure(bg=self.cor_bg)
        self.master.geometry("800x800")
        
        # Inicializando o banco de dados
        self.arquivo_db = 'reservas.xlsx'
        self.carregar_reservas()
        
        # Configurando estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configurar_estilos()
        
        self.criar_widgets()
        
    def carregar_reservas(self):
        """Carrega as reservas do arquivo Excel ou cria um novo se não existir"""
        if os.path.exists(self.arquivo_db):
            self.df_reservas = pd.read_excel(self.arquivo_db)
        else:
            self.df_reservas = pd.DataFrame(columns=['Data', 'Lugar', 'Nome', 'Status'])
        
        # Inicializa lugares para o dia atual
        self.data_atual = datetime.now().strftime('%Y-%m-%d')
        self.lugares = [0] * 20
        self.atualizar_lugares_por_data(self.data_atual)
    
    def atualizar_lugares_por_data(self, data):
        """Atualiza o status dos lugares para uma data específica"""
        self.lugares = [0] * 20
        reservas_do_dia = self.df_reservas[self.df_reservas['Data'] == data]
        
        for _, reserva in reservas_do_dia.iterrows():
            if reserva['Status'] == 'Ocupado':
                self.lugares[reserva['Lugar']-1] = 1
    
    def salvar_reservas(self):
        """Salva as reservas no arquivo Excel"""
        self.df_reservas.to_excel(self.arquivo_db, index=False)
        
    def criar_widgets(self):
        # Frame principal
        self.frame_principal = ttk.Frame(self.master, style='Principal.TFrame')
        self.frame_principal.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Título
        titulo = ttk.Label(
            self.frame_principal,
            text="Sistema de Reservas de Passagens",
            style='Principal.TLabel',
            font=('Segoe UI', 16, 'bold')
        )
        titulo.pack(pady=20)
        
        # Frame para seleção de data
        self.frame_data = ttk.Frame(self.frame_principal, style='Principal.TFrame')
        self.frame_data.pack(pady=10)
        
        ttk.Label(
            self.frame_data,
            text="Selecione a data:",
            style='Principal.TLabel'
        ).pack(side=tk.LEFT, padx=5)
        
        self.calendario = DateEntry(
            self.frame_data,
            width=12,
            background=self.cor_primaria,
            foreground='white',
            borderwidth=2,
            date_pattern='dd-mm-yyyy'
        )
        self.calendario.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            self.frame_data,
            text="Buscar Reservas",
            command=self.buscar_reservas_data,
            style='Botao.TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        # Frame para botões
        self.frame_botoes = ttk.Frame(self.frame_principal, style='Principal.TFrame')
        self.frame_botoes.pack(pady=20)
        
        # Botões
        botoes = [
            ("Exibir Mapa de Lugares", self.exibir_mapa),
            ("Reservar Lugar", self.reservar_lugar),
            ("Cancelar Reserva", self.cancelar_reserva),
            ("Sair", self.master.destroy)
        ]
        
        for texto, comando in botoes:
            ttk.Button(
                self.frame_botoes,
                text=texto,
                command=comando,
                style='Botao.TButton'
            ).pack(pady=5, padx=20, fill='x')
        
        # Frame para o mapa de lugares
        self.frame_mapa = ttk.Frame(self.frame_principal, style='Principal.TFrame')
        self.frame_mapa.pack(pady=20, expand=True)
        
        # Adicionar notebook para abas
        self.notebook = ttk.Notebook(self.frame_principal)
        self.notebook.pack(fill='both', expand=True, pady=10)
        
        # Aba do mapa de lugares
        self.aba_mapa = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_mapa, text='Mapa de Lugares')
        
        # Frame para o mapa de lugares (mova o frame_mapa para dentro da aba)
        self.frame_mapa = ttk.Frame(self.aba_mapa, style='Principal.TFrame')
        self.frame_mapa.pack(pady=20, expand=True)
        
        # Aba do banco de dados
        self.aba_bd = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_bd, text='Banco de Dados')
        
        # Frame para filtros
        self.frame_filtros = ttk.Frame(self.aba_bd, style='Principal.TFrame')
        self.frame_filtros.pack(fill='x', padx=10, pady=5)
        
        # Filtros
        ttk.Label(
            self.frame_filtros,
            text="Filtrar por:",
            style='Principal.TLabel'
        ).pack(side=tk.LEFT, padx=5)
        
        # Filtro por data
        ttk.Label(
            self.frame_filtros,
            text="Data:",
            style='Principal.TLabel'
        ).pack(side=tk.LEFT, padx=5)
        
        self.filtro_data = DateEntry(
            self.frame_filtros,
            width=12,
            background=self.cor_primaria,
            foreground='white',
            borderwidth=2,
            date_pattern='yyyy-mm-dd'
        )
        self.filtro_data.pack(side=tk.LEFT, padx=5)
        
        # Filtro por lugar
        ttk.Label(
            self.frame_filtros,
            text="Lugar:",
            style='Principal.TLabel'
        ).pack(side=tk.LEFT, padx=5)
        
        self.filtro_lugar = ttk.Entry(self.frame_filtros, width=5)
        self.filtro_lugar.pack(side=tk.LEFT, padx=5)
        
        # Filtro por nome
        ttk.Label(
            self.frame_filtros,
            text="Nome:",
            style='Principal.TLabel'
        ).pack(side=tk.LEFT, padx=5)
        
        self.filtro_nome = ttk.Entry(self.frame_filtros, width=20)
        self.filtro_nome.pack(side=tk.LEFT, padx=5)
        
        # Botão de filtrar
        ttk.Button(
            self.frame_filtros,
            text="Filtrar",
            command=self.aplicar_filtros,
            style='Botao.TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        # Botão de limpar filtros
        ttk.Button(
            self.frame_filtros,
            text="Limpar Filtros",
            command=self.limpar_filtros,
            style='Botao.TButton'
        ).pack(side=tk.LEFT, padx=5)
        
        # Frame para a tabela
        self.frame_tabela = ttk.Frame(self.aba_bd, style='Principal.TFrame')
        self.frame_tabela.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Criar Treeview
        self.tree = ttk.Treeview(
            self.frame_tabela,
            columns=('Data', 'Lugar', 'Nome', 'Status'),
            show='headings'
        )
        
        # Configurar cabeçalhos
        for col in ('Data', 'Lugar', 'Nome', 'Status'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        # Adicionar scrollbars
        scrolly = ttk.Scrollbar(self.frame_tabela, orient='vertical', command=self.tree.yview)
        scrollx = ttk.Scrollbar(self.frame_tabela, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        # Posicionar elementos
        scrolly.pack(side='right', fill='y')
        scrollx.pack(side='bottom', fill='x')
        self.tree.pack(fill='both', expand=True)
        
        # Atualizar tabela
        self.atualizar_tabela()
    
    def buscar_reservas_data(self):
        """Atualiza o mapa de lugares para a data selecionada"""
        data_selecionada = self.calendario.get_date().strftime('%Y-%m-%d')
        self.data_atual = data_selecionada
        self.atualizar_lugares_por_data(data_selecionada)
        self.exibir_mapa()
            
    def reservar_lugar(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Reservar Lugar")
        dialog.geometry("300x250")
        dialog.configure(bg=self.cor_bg)
        
        ttk.Label(
            dialog,
            text="Número do lugar (1-20):",
            style='Principal.TLabel'
        ).pack(pady=10)
        
        entrada_lugar = ttk.Entry(dialog)
        entrada_lugar.pack(pady=5)
        
        ttk.Label(
            dialog,
            text="Nome do passageiro:",
            style='Principal.TLabel'
        ).pack(pady=10)
        
        entrada_nome = ttk.Entry(dialog)
        entrada_nome.pack(pady=5)
        
        def confirmar():
            try:
                lugar = int(entrada_lugar.get())
                nome = entrada_nome.get()
                
                if not nome:
                    messagebox.showerror("Erro", "Por favor, digite o nome do passageiro!")
                    return
                
                if lugar < 1 or lugar > 20:
                    messagebox.showerror("Erro", "Lugar inválido!")
                    return
                
                if self.lugares[lugar-1] == 1:
                    messagebox.showerror("Erro", "Lugar indisponível!")
                    return
                
                # Adiciona nova reserva ao DataFrame
                nova_reserva = pd.DataFrame({
                    'Data': [self.data_atual],
                    'Lugar': [lugar],
                    'Nome': [nome],
                    'Status': ['Ocupado']
                })
                
                self.df_reservas = pd.concat([self.df_reservas, nova_reserva], ignore_index=True)
                self.lugares[lugar-1] = 1
                self.salvar_reservas()
                
                messagebox.showinfo("Sucesso", "Lugar reservado com sucesso!")
                dialog.destroy()
                self.exibir_mapa()
                
            except ValueError:
                messagebox.showerror("Erro", "Por favor, digite um número válido!")
        
        ttk.Button(
            dialog,
            text="Confirmar",
            command=confirmar,
            style='Botao.TButton'
        ).pack(pady=20)
        
    def cancelar_reserva(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Cancelar Reserva")
        dialog.geometry("300x150")
        dialog.configure(bg=self.cor_bg)
        
        ttk.Label(
            dialog,
            text="Número do lugar para cancelar:",
            style='Principal.TLabel'
        ).pack(pady=20)
        
        entrada = ttk.Entry(dialog)
        entrada.pack(pady=10)
        
        def confirmar():
            try:
                lugar = int(entrada.get())
                if lugar < 1 or lugar > 20:
                    messagebox.showerror("Erro", "Lugar inválido!")
                    return
                
                if self.lugares[lugar-1] == 0:
                    messagebox.showerror("Erro", "Este lugar não está reservado!")
                    return
                
                # Atualiza o status da reserva no DataFrame
                mascara = (self.df_reservas['Data'] == self.data_atual) & (self.df_reservas['Lugar'] == lugar)
                self.df_reservas.loc[mascara, 'Status'] = 'Cancelado'
                
                self.lugares[lugar-1] = 0
                self.salvar_reservas()
                
                messagebox.showinfo("Sucesso", "Reserva cancelada com sucesso!")
                dialog.destroy()
                self.exibir_mapa()
                
            except ValueError:
                messagebox.showerror("Erro", "Por favor, digite um número válido!")
        
        ttk.Button(
            dialog,
            text="Confirmar",
            command=confirmar,
            style='Botao.TButton'
        ).pack(pady=10)

    def configurar_estilos(self):
        """Configura os estilos personalizados para os widgets"""
        # Estilo para botões
        self.style.configure(
            'Botao.TButton',
            background=self.cor_primaria,
            foreground='white',
            padding=10,
            font=('Segoe UI', 10),
            borderwidth=0
        )
        self.style.map('Botao.TButton',
            background=[('active', self.cor_destaque)],
            foreground=[('active', 'white')]
        )
        
        # Estilo para frames
        self.style.configure(
            'Principal.TFrame',
            background=self.cor_bg
        )
        
        # Estilo para labels
        self.style.configure(
            'Principal.TLabel',
            background=self.cor_bg,
            foreground=self.cor_texto,
            font=('Segoe UI', 10)
        )
        
        # Estilo para entradas
        self.style.configure(
            'Principal.TEntry',
            fieldbackground=self.cor_bg,
            foreground=self.cor_texto
        )

    def exibir_mapa(self):
        """Exibe o mapa visual dos lugares"""
        # Limpar frame do mapa
        for widget in self.frame_mapa.winfo_children():
            widget.destroy()
            
        # Criar grid de lugares
        for i in range(20):
            cor = self.cor_destaque if self.lugares[i] == 0 else 'red'
            texto = f"Lugar {i+1}\n{'Livre' if self.lugares[i] == 0 else 'Ocupado'}"
            
            btn = tk.Button(
                self.frame_mapa,
                text=texto,
                bg=cor,
                fg='white',
                width=10,
                height=2,
                relief='raised',
                bd=3
            )
            btn.grid(row=i//4, column=i%4, padx=5, pady=5)
            
            # Adiciona tooltip com informações da reserva
            if self.lugares[i] == 1:
                reserva = self.df_reservas[
                    (self.df_reservas['Data'] == self.data_atual) & 
                    (self.df_reservas['Lugar'] == i+1) & 
                    (self.df_reservas['Status'] == 'Ocupado')
                ].iloc[0]
                self.criar_tooltip(btn, f"Reservado por: {reserva['Nome']}")
                
    def criar_tooltip(self, widget, texto):
        """Cria um tooltip para o widget"""
        def mostrar_tooltip(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            
            label = ttk.Label(
                tooltip,
                text=texto,
                background=self.cor_primaria,
                foreground='white',
                padding=5
            )
            label.pack()
            
            def esconder_tooltip():
                tooltip.destroy()
                
            widget.tooltip = tooltip
            widget.bind('<Leave>', lambda e: esconder_tooltip())
            
        widget.bind('<Enter>', mostrar_tooltip)

    def atualizar_tabela(self, df=None):
        """Atualiza a tabela com os dados filtrados ou todos os dados"""
        # Limpar tabela atual
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Usar DataFrame filtrado ou completo
        df_exibir = df if df is not None else self.df_reservas
        
        # Inserir dados
        for _, row in df_exibir.iterrows():
            self.tree.insert('', 'end', values=(
                row['Data'],
                row['Lugar'],
                row['Nome'],
                row['Status']
            ))

    def aplicar_filtros(self):
        """Aplica os filtros selecionados"""
        df_filtrado = self.df_reservas.copy()
        
        # Filtro por data
        data_filtro = self.filtro_data.get_date().strftime('%Y-%m-%d')
        if data_filtro:
            df_filtrado = df_filtrado[df_filtrado['Data'] == data_filtro]
        
        # Filtro por lugar
        lugar_filtro = self.filtro_lugar.get()
        if lugar_filtro:
            try:
                lugar = int(lugar_filtro)
                df_filtrado = df_filtrado[df_filtrado['Lugar'] == lugar]
            except ValueError:
                pass
        
        # Filtro por nome
        nome_filtro = self.filtro_nome.get()
        if nome_filtro:
            df_filtrado = df_filtrado[df_filtrado['Nome'].str.contains(nome_filtro, case=False, na=False)]
        
        # Atualizar tabela com dados filtrados
        self.atualizar_tabela(df_filtrado)

    def limpar_filtros(self):
        """Limpa todos os filtros"""
        self.filtro_data.set_date(datetime.now())
        self.filtro_lugar.delete(0, 'end')
        self.filtro_nome.delete(0, 'end')
        self.atualizar_tabela()

def main():
    root = tk.Tk()
    app = SistemaReservas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
