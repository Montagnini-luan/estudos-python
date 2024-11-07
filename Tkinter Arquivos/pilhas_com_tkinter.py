import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class PilhaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Pilha")
        self.pilha = []
        
        # Frame principal
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Campo de entrada
        self.entrada = ttk.Entry(self.frame, width=20)
        self.entrada.grid(row=0, column=0, padx=5, pady=5)
        
        # Botões
        ttk.Button(self.frame, text="Adicionar", command=self.adicionar).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.frame, text="Remover", command=self.remover).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(self.frame, text="Ver Topo", command=self.ver_topo).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.frame, text="Verificar Vazia", command=self.verificar_vazia).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(self.frame, text="Tamanho", command=self.obter_tamanho).grid(row=2, column=1, padx=5, pady=5)
        
        # Lista para visualização da pilha
        self.lista_pilha = tk.Listbox(self.frame, height=10, width=30)
        self.lista_pilha.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        # Label para indicar o topo
        self.label_topo = ttk.Label(self.frame, text="↑ TOPO DA PILHA ↑")
        self.label_topo.grid(row=4, column=0, columnspan=2)
        
    def atualizar_lista(self):
        self.lista_pilha.delete(0, tk.END)
        for item in reversed(self.pilha):
            self.lista_pilha.insert(tk.END, str(item))
            
    def adicionar(self):
        try:
            valor = int(self.entrada.get())
            self.pilha.append(valor)
            self.entrada.delete(0, tk.END)
            self.atualizar_lista()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número inteiro válido!")
            
    def remover(self):
        if self.pilha:
            valor = self.pilha.pop()
            self.atualizar_lista()
            messagebox.showinfo("Removido", f"O valor {valor} foi removido do topo da pilha!")
        else:
            messagebox.showwarning("Aviso", "A pilha está vazia!")
            
    def ver_topo(self):
        if self.pilha:
            messagebox.showinfo("Topo", f"O valor no topo da pilha é: {self.pilha[-1]}")
        else:
            messagebox.showwarning("Aviso", "A pilha está vazia!")
            
    def verificar_vazia(self):
        if not self.pilha:
            messagebox.showinfo("Status", "A pilha está vazia!")
        else:
            messagebox.showinfo("Status", "A pilha não está vazia!")
            
    def obter_tamanho(self):
        messagebox.showinfo("Tamanho", f"A pilha possui {len(self.pilha)} elemento(s).")

if __name__ == "__main__":
    root = tk.Tk()
    app = PilhaApp(root)
    root.mainloop()
