import pyodbc
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Constantes
BG_COLOR = '#C0C0C0'
FONT = ('MS Sans Serif', 8)
TITLE_FONT = ('MS Sans Serif', 12, 'bold')
TITLE_BG = '#000080'
TITLE_FG = 'white'
BUTTON_STYLE = {
    'bg': BG_COLOR,
    'fg': 'black',
    'font': FONT,
    'relief': 'raised',
    'borderwidth': 1,
    'width': 10,
    'height': 1,
    'padx': 2
}

def criar_conexao():
    try:
        return pyodbc.connect('Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto_Compras.db')
    except pyodbc.Error as erro:
        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao banco de dados: {erro}")
        return None
    
def listar_dados():
    global treeview
    for i in treeview.get_children():
        treeview.delete(i)
    
    try:
        conexao = criar_conexao()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM Produtos")
            valores = cursor.fetchall()
    except pyodbc.Error as erro:
        messagebox.showerror("Erro", f"Erro ao listar produtos: {erro}")
    
    for valor in valores:
        treeview.insert('', 'end', values=(valor[0], valor[1], valor[2], valor[3]))

def centralizar_janela(janela, largura, altura):
    pos_x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    pos_y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

def salvar_dados(nome, descricao, preco, janela_cadastro):
    try:
        conexao = criar_conexao()
        if conexao:
            cursor = conexao.cursor()
            novo_produto = (nome.get(), descricao.get(), preco.get())
            
            cursor.execute("""
                INSERT INTO Produtos (NomeProduto, Descricao, Preco) 
                VALUES (?, ?, ?)""", novo_produto)
            
            conexao.commit()
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            janela_cadastro.destroy()
            
            cursor.close()
            conexao.close()
            
            # Atualiza a lista de produtos após cadastrar
            listar_dados()
    except pyodbc.Error as erro:
        messagebox.showerror("Erro", f"Erro ao cadastrar produto: {erro}")
        
def salvar_dados_editar(nome, descricao, preco, janela_editar_produto):
    try:
        conexao = criar_conexao()
        if conexao:
            cursor = conexao.cursor()
            nome_produto = (nome.get())
            nova_descricao = (descricao.get())
            novo_preco = (preco.get())
            
            treeview.item(item_selecionado, values=(valores_selecionados[0], nome_produto, nova_descricao, novo_preco))
            
            cursor.execute("""UPDATE Produtos SET NomeProduto = ?, Descricao = ?, Preco = ? WHERE ID = ?""", 
                (nome_produto, nova_descricao, novo_preco, valores_selecionados[0]))
            
            conexao.commit()
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            janela_editar_produto.destroy()
            
            cursor.close()
            conexao.close()
            
            # Atualiza a lista de produtos após cadastrar
            listar_dados()
    except pyodbc.Error as erro:
        messagebox.showerror("Erro", f"Erro ao cadastrar produto: {erro}")

def cadastrar_produto():
    janela_cadastro_produto = Toplevel()
    janela_cadastro_produto.title('Cadastro de Produtos')
    janela_cadastro_produto.configure(bg=BG_COLOR)
    centralizar_janela(janela_cadastro_produto, 300, 250)

    frame_cadastro = Frame(janela_cadastro_produto, bg=BG_COLOR, relief='raised', borderwidth=1)
    frame_cadastro.place(relx=0.5, rely=0.5, anchor='center')
    
    Label(frame_cadastro, text='Cadastro de Produto', 
          bg=TITLE_BG, fg=TITLE_FG, font=TITLE_FONT, 
          padx=5, pady=2).grid(row=0, column=0, columnspan=2, 
                              sticky='ew', padx=1, pady=(1, 10))

    Label(frame_cadastro, text='Nome:', 
          bg=BG_COLOR, font=FONT).grid(row=1, column=0, 
                                      sticky='e', padx=(5, 2), pady=2)
    nome = Entry(frame_cadastro, font=FONT, relief='sunken', borderwidth=1)
    nome.grid(row=1, column=1, sticky='w', padx=(0, 5), pady=2)
    
    Label(frame_cadastro, text='Descrição:', 
          bg=BG_COLOR, font=FONT).grid(row=2, column=0, 
                                      sticky='e', padx=(5, 2), pady=2)
    descricao = Entry(frame_cadastro, font=FONT, relief='sunken', borderwidth=1)
    descricao.grid(row=2, column=1, sticky='w', padx=(0, 5), pady=2)
    
    Label(frame_cadastro, text='Preço:', 
          bg=BG_COLOR, font=FONT).grid(row=3, column=0, 
                                      sticky='e', padx=(5, 2), pady=2)
    preco = Entry(frame_cadastro, font=FONT, relief='sunken', borderwidth=1)
    preco.grid(row=3, column=1, sticky='w', padx=(0, 5), pady=2)

    botao_salvar = Button(frame_cadastro, text='Cadastrar',
           command=lambda: salvar_dados(nome, descricao, preco, janela_cadastro_produto),
           **BUTTON_STYLE)
    botao_salvar.grid(row=4, column=0, columnspan=2, pady=10)
    
    botao_cancelar = Button(frame_cadastro, text='Cancelar',
           command=janela_cadastro_produto.destroy,
           **BUTTON_STYLE)
    botao_cancelar.grid(row=5, column=0, columnspan=2, pady=(0, 5))
    
def editar_dados(event):
    global item_selecionado
    global valores_selecionados
    
    item_selecionado = treeview.selection()[0]  # obtem o item selecionado
    valores_selecionados = treeview.item(item_selecionado)['values']
    
    janela_editar_produto = Toplevel()
    janela_editar_produto.title('Editar Produto')
    janela_editar_produto.configure(bg=BG_COLOR)
    centralizar_janela(janela_editar_produto, 300, 250)

    frame_editar = Frame(janela_editar_produto, bg=BG_COLOR, relief='raised', borderwidth=1)
    frame_editar.place(relx=0.5, rely=0.5, anchor='center')
    
    Label(frame_editar, text='Editar Produto', 
          bg=TITLE_BG, fg=TITLE_FG, font=TITLE_FONT, 
          padx=5, pady=2).grid(row=0, column=0, columnspan=2, 
                              sticky='ew', padx=1, pady=(1, 10))

    Label(frame_editar, text='Nome:', 
          bg=BG_COLOR, font=FONT).grid(row=1, column=0, 
                                      sticky='e', padx=(5, 2), pady=2)
    nome_editado = Entry(frame_editar, font=FONT, relief='sunken', borderwidth=1, textvariable=StringVar(value=valores_selecionados[1]))
    nome_editado.grid(row=1, column=1, sticky='w', padx=(0, 5), pady=2)
    
    Label(frame_editar, text='Descrição:', 
          bg=BG_COLOR, font=FONT).grid(row=2, column=0, 
                                      sticky='e', padx=(5, 2), pady=2)
    descricao_editada = Entry(frame_editar, font=FONT, relief='sunken', borderwidth=1, textvariable=StringVar(value=valores_selecionados[2]))
    descricao_editada.grid(row=2, column=1, sticky='w', padx=(0, 5), pady=2)
    
    Label(frame_editar, text='Preço:', 
          bg=BG_COLOR, font=FONT).grid(row=3, column=0, 
                                      sticky='e', padx=(5, 2), pady=2)
    preco_editado = Entry(frame_editar, font=FONT, relief='sunken', borderwidth=1, textvariable=StringVar(value=valores_selecionados[3]))
    preco_editado.grid(row=3, column=1, sticky='w', padx=(0, 5), pady=2)

    botao_salvar = Button(frame_editar, text='Salvar',
           command=lambda: salvar_dados_editar(nome_editado, descricao_editada, preco_editado, janela_editar_produto),
           **BUTTON_STYLE)
    botao_salvar.grid(row=4, column=0, columnspan=2, pady=10)
    
    botao_deletar = Button(frame_editar, text='Deletar',
           command=lambda: excluir_produto(janela_editar_produto),
           **BUTTON_STYLE)
    botao_deletar.grid(row=5, column=0, columnspan=2, pady=(0, 5))
    
def excluir_produto(janela_editar_produto):
    selected_item = treeview.selection()[0]
    id = treeview.item(selected_item)['values'][0]  
    
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Produtos WHERE ID = ?", (id,))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
        janela_editar_produto.destroy()
        listar_dados()
        
def deletar_produto():
    selected_item = treeview.selection()[0]
    id = treeview.item(selected_item)['values'][0]  
    
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Produtos WHERE ID = ?", (id,))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
        listar_dados()
        
def filtrar_dados(nome_produto, descricao_produto):
    if not nome_produto.get() and not descricao_produto.get():
        listar_dados()
        return
    else:
        sql = "SELECT * FROM Produtos"
        parametros = []
        
        if nome_produto.get():
            sql += " WHERE NomeProduto LIKE ?"
            parametros.append('%' + nome_produto.get() + '%')
            
        if descricao_produto.get():
            if nome_produto.get():
                sql += " AND"
            else:
                sql += " WHERE"
            sql += " Descricao LIKE ?"
            parametros.append('%' + descricao_produto.get() + '%')
        
    conecxao = criar_conexao()
    if conecxao:
        cursor = conecxao.cursor()
        cursor.execute(sql, tuple(parametros))
        produtos = cursor.fetchall()
            
        limpar_dados()
            
        for dado in produtos:
            treeview.insert('', 'end', values=(dado[0], dado[1], dado[2], dado[3]))
                
def limpar_dados():
    for i in treeview.get_children():
        treeview.delete(i)
        
def main():
    global treeview
    
    janela = Tk()
    janela.title('Sistema de Produtos')
    janela.configure(bg=BG_COLOR)
    
    # Frame principal
    frame_principal = Frame(janela, bg=BG_COLOR, relief='raised', borderwidth=1)
    frame_principal.pack(expand=True, fill='both', padx=5, pady=5)
    
    # Barra de menu
    menu_barra = Menu(janela)
    janela.config(menu=menu_barra)

    menu_arquivo = Menu(menu_barra, tearoff=0)
    menu_barra.add_cascade(label='Arquivo', menu=menu_arquivo)
    menu_arquivo.add_command(label='Cadastrar Produto', command=cadastrar_produto)
    menu_arquivo.add_separator()
    menu_arquivo.add_command(label='Sair', command=janela.destroy)
    
    # Frame de pesquisa
    frame_pesquisa = Frame(frame_principal, bg=BG_COLOR, relief='ridge', borderwidth=1)
    frame_pesquisa.pack(fill='x', padx=5, pady=5)
    
    Label(frame_pesquisa, text='Pesquisar Produtos', 
          bg=TITLE_BG, fg=TITLE_FG, 
          font=TITLE_FONT).pack(fill='x', padx=1, pady=1)
    
    frame_campos = Frame(frame_pesquisa, bg=BG_COLOR)
    frame_campos.pack(fill='x', padx=5, pady=5)
    
    Label(frame_campos, text='Nome:', bg=BG_COLOR, font=FONT).grid(row=0, column=0, padx=5, pady=5)
    nome_produto = Entry(frame_campos, font=FONT, relief='sunken', borderwidth=1)
    nome_produto.grid(row=0, column=1, padx=5, pady=5)
    
    Label(frame_campos, text='Descrição:', bg=BG_COLOR, font=FONT).grid(row=0, column=2, padx=5, pady=5)
    descricao_produto = Entry(frame_campos, font=FONT, relief='sunken', borderwidth=1)
    descricao_produto.grid(row=0, column=3, padx=5, pady=5)
    
    # Frame da lista de produtos
    frame_lista = Frame(frame_principal, bg=BG_COLOR, relief='ridge', borderwidth=1)
    frame_lista.pack(expand=True, fill='both', padx=5, pady=5)
    
    Label(frame_lista, text='Lista de Produtos', 
          bg=TITLE_BG, fg=TITLE_FG, 
          font=TITLE_FONT).pack(fill='x', padx=1, pady=1)
    
    # Configuração do Treeview
    style = ttk.Style()
    style.theme_use('default')
    style.configure('mystyle.Treeview',
                   font=FONT,
                   rowheight=20,
                   background=BG_COLOR,
                   fieldbackground=BG_COLOR)
    style.configure('mystyle.Treeview.Heading', 
                   font=FONT,
                   relief='raised')
    
    treeview = ttk.Treeview(frame_lista, 
                           style='mystyle.Treeview',
                           columns=('ID', 'NomeProduto', 'Descricao', 'Preco'),
                           show='headings',
                           height=15)
    
    treeview.heading('ID', text='ID')
    treeview.heading('NomeProduto', text='Nome do Produto')
    treeview.heading('Descricao', text='Descrição')
    treeview.heading('Preco', text='Preço')
    
    treeview.column('#0', width=0, stretch=NO)
    treeview.column('ID', width=50, anchor=CENTER)
    treeview.column('NomeProduto', width=200)
    treeview.column('Descricao', width=300)
    treeview.column('Preco', width=100, anchor=CENTER)
    
    treeview.pack(expand=True, fill='both', padx=5, pady=5)
    
    # Frame de botões
    frame_botoes = Frame(frame_principal, bg=BG_COLOR)
    frame_botoes.pack(fill='x', padx=5, pady=5)
    
    Button(frame_botoes, text='Novo', 
           command=cadastrar_produto, 
           **BUTTON_STYLE).pack(side=LEFT, padx=5)
    
    Button(frame_botoes, text='Excluir', 
           command=deletar_produto, 
           **BUTTON_STYLE).pack(side=LEFT, padx=5)
    
    # Carrega os dados iniciais
    listar_dados()
    
    """Configuração dos eventos"""
    treeview.bind('<Double-1>', editar_dados)
    nome_produto.bind('<KeyRelease>', lambda e: filtrar_dados(nome_produto, descricao_produto))
    descricao_produto.bind('<KeyRelease>', lambda e: filtrar_dados(nome_produto, descricao_produto))
    
    # Ajusta o tamanho inicial da janela
    janela.geometry('800x600')
    centralizar_janela(janela, 800, 600)
    
    return janela

if __name__ == '__main__':
    janela = main()
    janela.mainloop()
