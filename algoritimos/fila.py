import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
"""

fila

"""
    
class FilaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Fila com Prioridade")
        self.fila = []
        
        # Frame principal
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Frame para entrada de dados
        entrada_frame = ttk.Frame(self.frame)
        entrada_frame.grid(row=0, column=0, columnspan=2, pady=5)
        
        # Campo de entrada para valor
        ttk.Label(entrada_frame, text="Valor:").grid(row=0, column=0, padx=5)
        self.entrada = ttk.Entry(entrada_frame, width=15)
        self.entrada.grid(row=0, column=1, padx=5)
        
        # Campo de entrada para prioridade
        ttk.Label(entrada_frame, text="Prioridade:").grid(row=0, column=2, padx=5)
        self.prioridade = ttk.Combobox(entrada_frame, width=12, 
                                     values=["Alta", "Média", "Baixa"])
        self.prioridade.set("Baixa")
        self.prioridade.grid(row=0, column=3, padx=5)
        
        # Botões
        ttk.Button(self.frame, text="Adicionar à Fila", 
                  command=self.adicionar).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(self.frame, text="Remover da Fila", 
                  command=self.remover).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.frame, text="Ver Primeiro", 
                  command=self.ver_primeiro).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(self.frame, text="Ver Último", 
                  command=self.ver_ultimo).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(self.frame, text="Tamanho da Fila", 
                  command=self.obter_tamanho).grid(row=3, column=0, columnspan=2, pady=5)
        
        # Lista para visualização da fila
        self.lista_fila = ttk.Treeview(self.frame, columns=('Valor', 'Prioridade'), 
                                     show='headings', height=10)
        self.lista_fila.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        # Configurar colunas
        self.lista_fila.heading('Valor', text='Valor')
        self.lista_fila.heading('Prioridade', text='Prioridade')
        self.lista_fila.column('Valor', width=100)
        self.lista_fila.column('Prioridade', width=100)
        
        # Labels indicadores
        self.label_primeiro = ttk.Label(self.frame, text="↑ PRIMEIRO DA FILA ↑")
        self.label_primeiro.grid(row=5, column=0, columnspan=2)
        self.label_ultimo = ttk.Label(self.frame, text="↓ ÚLTIMO DA FILA ↓")
        self.label_ultimo.grid(row=6, column=0, columnspan=2)
        
    def prioridade_valor(self, prioridade):
        return {'Alta': 3, 'Média': 2, 'Baixa': 1}[prioridade]
        
    def atualizar_lista(self):
        for item in self.lista_fila.get_children():
            self.lista_fila.delete(item)
            
        for valor, prioridade in self.fila:
            self.lista_fila.insert('', 'end', values=(valor, prioridade))
            
    def adicionar(self):
        try:
            valor = int(self.entrada.get())
            prioridade = self.prioridade.get()
            
            # Inserir mantendo a ordem de prioridade
            indice = 0
            for i, (_, prio_existente) in enumerate(self.fila):
                if self.prioridade_valor(prioridade) > self.prioridade_valor(prio_existente):
                    break
                indice = i + 1
                
            self.fila.insert(indice, (valor, prioridade))
            self.entrada.delete(0, tk.END)
            self.prioridade.set("Baixa")
            self.atualizar_lista()
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número inteiro válido!")
            
    def remover(self):
        if self.fila:
            valor, prioridade = self.fila.pop(0)
            self.atualizar_lista()
            messagebox.showinfo("Removido", 
                              f"O valor {valor} (Prioridade: {prioridade}) foi removido do início da fila!")
        else:
            messagebox.showwarning("Aviso", "A fila está vazia!")
            
    def ver_primeiro(self):
        if self.fila:
            valor, prioridade = self.fila[0]
            messagebox.showinfo("Primeiro", 
                              f"Primeiro da fila: {valor} (Prioridade: {prioridade})")
        else:
            messagebox.showwarning("Aviso", "A fila está vazia!")
            
    def ver_ultimo(self):
        if self.fila:
            valor, prioridade = self.fila[-1]
            messagebox.showinfo("Último", 
                              f"Último da fila: {valor} (Prioridade: {prioridade})")
        else:
            messagebox.showwarning("Aviso", "A fila está vazia!")
            
    def obter_tamanho(self):
        messagebox.showinfo("Tamanho", f"A fila possui {len(self.fila)} elemento(s).")

if __name__ == "__main__":
    root = tk.Tk()
    app = FilaApp(root)
    root.mainloop()
