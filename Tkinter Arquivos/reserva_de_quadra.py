import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import date, datetime, timedelta
import openpyxl
import os
import pandas as pd
from ttkthemes import ThemedTk

# Definição das cores e estilos
CORES = {
    'bg_principal': '#f0f0f0',
    'bg_secundario': '#ffffff',
    'destaque': '#4a90e2',
    'texto': '#333333',
    'sucesso': '#28a745',
    'erro': '#dc3545',
    'aviso': '#ffc107',
    'reservado': '#ffd700',
    'disponivel': '#90EE90'
}

ESTILOS = {
    'titulo': ('Helvetica', 24, 'bold'),
    'subtitulo': ('Helvetica', 18, 'bold'),
    'texto_normal': ('Helvetica', 12),
    'botao': ('Helvetica', 12, 'bold')
}

class EstiloFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(style='Card.TFrame')

# Atualização da função principal
def criar_janela_principal():
    root = ThemedTk(theme="arc")  # Usando um tema moderno
    root.title("Sistema de Reservas")
    
    # Configuração do estilo
    style = ttk.Style()
    style.configure('Card.TFrame', background=CORES['bg_secundario'])
    style.configure('Primary.TButton',
                   font=ESTILOS['botao'],
                   background=CORES['destaque'])
    
    # Frame principal com padding e sombra
    main_frame = EstiloFrame(root)
    main_frame.pack(padx=20, pady=20, fill='both', expand=True)
    
    # Título com estilo moderno
    titulo = ttk.Label(main_frame,
                      text="Sistema de Reservas",
                      font=ESTILOS['titulo'],
                      foreground=CORES['texto'])
    titulo.pack(pady=(0, 20))
    
    # Frame para botões com layout em grid
    botoes_frame = EstiloFrame(main_frame)
    botoes_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Botões estilizados
    botoes = [
        ("Fazer Reserva", fazer_reserva),
        ("Ver Reservas", ver_reservas),
        ("Detalhes", detalhe_reservas),
        ("Sair", root.quit)
    ]
    
    for i, (texto, comando) in enumerate(botoes):
        btn = ttk.Button(botoes_frame,
                        text=texto,
                        style='Primary.TButton',
                        command=comando)
        btn.pack(fill='x', pady=5, padx=20)
    
    return root

# Adicione esta função antes da função fazer_reserva
def salvar_reserva(entries, janela):
    try:
        # Validar dados
        data = entries["Data"].get()
        hora_inicial = entries["Hora Inicial"].get()
        hora_final = entries["Hora Final"].get()
        cpf = entries["CPF"].get()
        nome = entries["Nome"].get()
        
        # Validar campos vazios
        if not all([data, hora_inicial, hora_final, cpf, nome]):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return
            
        # Validar horário
        if hora_inicial < "09:00" or hora_final > "23:00" or hora_inicial >= hora_final:
            messagebox.showerror("Erro", "Horário inválido! O horário deve estar entre 09:00 e 23:00")
            return
            
        # Calcular preço
        hora_inicial_obj = datetime.strptime(hora_inicial, "%H:%M")
        hora_final_obj = datetime.strptime(hora_final, "%H:%M")
        duracao = (hora_final_obj - hora_inicial_obj).seconds / 3600  # duração em horas
        preco = duracao * 8  # R$ 8 por hora
        
        # Verificar conflito de horário
        if verificar_conflito_reserva(data, hora_inicial, hora_final):
            messagebox.showerror("Erro", "Já existe uma reserva neste horário!")
            return
            
        # Salvar no Excel
        try:
            if not os.path.exists("Dados.xlsx"):
                wb = openpyxl.Workbook()
                ws = wb.active
                ws.append(["Data", "Hora Inicial", "Hora Final", "CPF", "Nome", "Preço"])
            else:
                wb = openpyxl.load_workbook("Dados.xlsx")
                ws = wb.active
                
            ws.append([data, hora_inicial, hora_final, cpf, nome, preco])
            wb.save("Dados.xlsx")
            
            messagebox.showinfo("Sucesso", 
                              f"Reserva realizada com sucesso!\nValor total: R${preco:.2f}")
            janela.destroy()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar reserva: {str(e)}")
            
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar reserva: {str(e)}")

def verificar_conflito_reserva(data, hora_inicial, hora_final):
    try:
        if not os.path.exists("Dados.xlsx"):
            return False
            
        df = pd.read_excel("Dados.xlsx")
        reservas_do_dia = df[df["Data"] == data]
        
        for _, reserva in reservas_do_dia.iterrows():
            if (hora_inicial < reserva["Hora Final"] and 
                hora_final > reserva["Hora Inicial"]):
                return True
        return False
        
    except Exception:
        return False

# Atualização da função fazer_reserva
def fazer_reserva():
    janela = tk.Toplevel()
    janela.title("Nova Reserva")
    
    style = ttk.Style()
    style.configure('Form.TFrame', background=CORES['bg_secundario'])
    
    main_frame = EstiloFrame(janela)
    main_frame.pack(padx=20, pady=20, fill='both', expand=True)
    
    # Título
    titulo = ttk.Label(main_frame,
                      text="Nova Reserva",
                      font=ESTILOS['titulo'],
                      foreground=CORES['texto'])
    titulo.pack(pady=(0, 20))
    
    # Frame do formulário
    form_frame = EstiloFrame(main_frame)
    form_frame.pack(fill='both', expand=True)
    
    # Campos do formulário com estilo
    campos = [
        ("Data", "date"),
        ("Hora Inicial", "time"),
        ("Hora Final", "time"),
        ("CPF", "text"),
        ("Nome", "text")
    ]
    
    entries = {}
    for i, (label_text, campo_tipo) in enumerate(campos):
        label = ttk.Label(form_frame,
                         text=label_text,
                         font=ESTILOS['texto_normal'])
        label.grid(row=i, column=0, pady=5, padx=5, sticky='e')
        
        entry = ttk.Entry(form_frame, font=ESTILOS['texto_normal'])
        entry.grid(row=i, column=1, pady=5, padx=5, sticky='ew')
        entries[label_text] = entry
    
    # Botões de ação
    botoes_frame = EstiloFrame(main_frame)
    botoes_frame.pack(fill='x', pady=(20, 0))
    
    ttk.Button(botoes_frame,
               text="Confirmar",
               style='Primary.TButton',
               command=lambda: salvar_reserva(entries, janela)).pack(side='right', padx=5)
    
    ttk.Button(botoes_frame,
               text="Cancelar",
               command=janela.destroy).pack(side='right', padx=5)

# Atualização da função ver_reservas
def ver_reservas():
    janela = tk.Toplevel()
    janela.title("Visualizar Reservas")
    
    main_frame = EstiloFrame(janela)
    main_frame.pack(padx=20, pady=20, fill='both', expand=True)
    
    # Cabeçalho
    titulo = ttk.Label(main_frame,
                      text="Reservas",
                      font=ESTILOS['titulo'],
                      foreground=CORES['texto'])
    titulo.pack(pady=(0, 20))
    
    # Frame para filtro de data
    filtro_frame = EstiloFrame(main_frame)
    filtro_frame.pack(fill='x', padx=10, pady=10)
    
    ttk.Label(filtro_frame,
             text="Data:",
             font=ESTILOS['texto_normal']).pack(side='left', padx=5)
    
    entry_data = ttk.Entry(filtro_frame, font=ESTILOS['texto_normal'])
    entry_data.pack(side='left', padx=5)
    entry_data.insert(0, date.today().strftime("%d/%m/%Y"))
    
    # Treeview estilizada
    style = ttk.Style()
    style.configure("Treeview",
                   background=CORES['bg_secundario'],
                   foreground=CORES['texto'],
                   fieldbackground=CORES['bg_secundario'])
    
    style.configure("Treeview.Heading",
                   font=ESTILOS['texto_normal'],
                   background=CORES['destaque'],
                   foreground='white')
    
    # Criação do Treeview com todas as colunas
    colunas = ("Data", "Hora Inicial", "Hora Final", "CPF", "Nome", "Preço")
    tree = ttk.Treeview(main_frame, columns=colunas, show='headings')
    
    # Configuração das colunas
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    tree.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=tree.yview)
    scrollbar.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scrollbar.set)
    
    def carregar_reservas():
        # Limpar dados existentes
        for item in tree.get_children():
            tree.delete(item)
            
        try:
            data_filtro = entry_data.get()
            
            # Carregar dados do Excel
            if os.path.exists("Dados.xlsx"):
                df = pd.read_excel("Dados.xlsx")
                
                # Filtrar por data se houver filtro
                if data_filtro:
                    df = df[df["Data"] == data_filtro]
                
                # Inserir dados na tabela
                for _, row in df.iterrows():
                    valores = (
                        row["Data"],
                        row["Hora Inicial"],
                        row["Hora Final"],
                        row["CPF"],
                        row["Nome"],
                        f"R$ {row['Preço']:.2f}"
                    )
                    tree.insert("", "end", values=valores)
                    
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar reservas: {str(e)}")
    
    # Frame para botões
    botoes_frame = EstiloFrame(main_frame)
    botoes_frame.pack(fill='x', pady=10)
    
    ttk.Button(botoes_frame,
               text="Filtrar",
               style='Primary.TButton',
               command=carregar_reservas).pack(side='left', padx=5)
    
    ttk.Button(botoes_frame,
               text="Fechar",
               command=janela.destroy).pack(side='right', padx=5)
    
    # Carregar dados iniciais
    carregar_reservas()

# Adicione esta função junto com as outras funções
def detalhe_reservas():
    janela = tk.Toplevel()
    janela.title("Detalhes das Reservas")
    
    main_frame = EstiloFrame(janela)
    main_frame.pack(padx=20, pady=20, fill='both', expand=True)
    
    # Título
    titulo = ttk.Label(main_frame,
                      text="Detalhes das Reservas",
                      font=ESTILOS['titulo'],
                      foreground=CORES['texto'])
    titulo.pack(pady=(0, 20))
    
    # Frame para filtros
    filtros_frame = EstiloFrame(main_frame)
    filtros_frame.pack(fill='x', padx=10, pady=10)
    
    # Campos de filtro
    campos_filtro = ["Data", "CPF", "Nome"]
    entries = {}
    
    for i, campo in enumerate(campos_filtro):
        frame = ttk.Frame(filtros_frame)
        frame.pack(side='left', padx=10)
        
        ttk.Label(frame,
                 text=campo + ":",
                 font=ESTILOS['texto_normal']).pack(side='left', padx=5)
        
        entry = ttk.Entry(frame, font=ESTILOS['texto_normal'])
        entry.pack(side='left')
        entries[campo] = entry
    
    # Frame para a tabela
    table_frame = EstiloFrame(main_frame)
    table_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Configuração do Treeview
    style = ttk.Style()
    style.configure("Treeview",
                   background=CORES['bg_secundario'],
                   foreground=CORES['texto'],
                   fieldbackground=CORES['bg_secundario'],
                   font=ESTILOS['texto_normal'])
    
    style.configure("Treeview.Heading",
                   font=ESTILOS['texto_normal'],
                   background=CORES['destaque'],
                   foreground='white')
    
    colunas = ("Data", "Hora Inicial", "Hora Final", "CPF", "Nome", "Preço")
    tree = ttk.Treeview(table_frame, columns=colunas, show='headings')
    
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    tree.pack(side='left', fill='both', expand=True)
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=tree.yview)
    scrollbar.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scrollbar.set)
    
    # Frame para botões
    botoes_frame = EstiloFrame(main_frame)
    botoes_frame.pack(fill='x', pady=10)
    
    def filtrar_dados():
        # Limpar dados existentes
        for item in tree.get_children():
            tree.delete(item)
            
        try:
            # Carregar dados do Excel
            df = pd.read_excel("Dados.xlsx")
            
            # Aplicar filtros
            filtros = {k: v.get() for k, v in entries.items() if v.get()}
            
            for _, row in df.iterrows():
                if all(str(row[k]).lower().startswith(v.lower()) for k, v in filtros.items()):
                    tree.insert("", "end", values=tuple(row))
                    
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar dados: {str(e)}")
    
    def exportar_dados():
        try:
            df = pd.DataFrame([tree.item(item)['values'] for item in tree.get_children()],
                            columns=colunas)
            df.to_excel("Reservas_Exportadas.xlsx", index=False)
            messagebox.showinfo("Sucesso", "Dados exportados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar dados: {str(e)}")
    
    # Botões
    ttk.Button(botoes_frame,
               text="Filtrar",
               style='Primary.TButton',
               command=filtrar_dados).pack(side='left', padx=5)
    
    ttk.Button(botoes_frame,
               text="Exportar",
               style='Primary.TButton',
               command=exportar_dados).pack(side='left', padx=5)
    
    ttk.Button(botoes_frame,
               text="Fechar",
               command=janela.destroy).pack(side='right', padx=5)
    
    # Carregar dados iniciais
    filtrar_dados()

# Inicialização do programa
if __name__ == "__main__":
    root = criar_janela_principal()
    root.mainloop()
