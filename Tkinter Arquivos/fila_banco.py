import tkinter as tk
from tkinter import ttk, messagebox

class FilaBanco:
    def __init__(self):
        self.fila = []
        self.contador_normal = 0
        self.contador_prioritario = 0
    
    def inserir_cliente(self, tipo_senha):
        if tipo_senha == 'p':
            self.contador_prioritario += 1
            senha = f'Senha Prioritária - {self.contador_prioritario}'
            self.fila.insert(0, senha)
        else:
            self.contador_normal += 1
            senha = f'Senha Normal - {self.contador_normal}'
            self.fila.append(senha)
        return senha
    
    def remover_cliente(self):
        if self.fila:
            return self.fila.pop(0)
        return None
    
    def atender_cliente(self):
        return self.remover_cliente()
    
    def obter_fila(self):
        return self.fila.copy()

class FilaBancoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Fila de Banco")
        self.root.geometry("600x400")
        self.fila_banco = FilaBanco()
        
        # Configuração do estilo
        self.style = ttk.Style()
        self.style.configure('TButton', padding=5)
        self.style.configure('TLabel', padding=5)
        
        self.criar_widgets()
        
    def criar_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Botões
        ttk.Button(main_frame, text="Senha Normal", 
                  command=lambda: self.inserir_cliente('n')).grid(row=0, column=0, padx=5, pady=5)
        
        ttk.Button(main_frame, text="Senha Prioritária", 
                  command=lambda: self.inserir_cliente('p')).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(main_frame, text="Atender Cliente", 
                  command=self.atender_cliente).grid(row=0, column=2, padx=5, pady=5)
        
        # Lista de senhas
        self.lista_frame = ttk.LabelFrame(main_frame, text="Fila Atual", padding="5")
        self.lista_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # Listbox para mostrar a fila
        self.listbox = tk.Listbox(self.lista_frame, height=10, width=50)
        self.listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar para a listbox
        scrollbar = ttk.Scrollbar(self.lista_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.listbox.configure(yscrollcommand=scrollbar.set)
        
        # Status
        self.status_label = ttk.Label(main_frame, text="Sistema pronto")
        self.status_label.grid(row=2, column=0, columnspan=3, pady=5)
        
        # Configurar expansão de grid
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        self.lista_frame.columnconfigure(0, weight=1)
        
    def atualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for senha in self.fila_banco.obter_fila():
            self.listbox.insert(tk.END, senha)
    
    def inserir_cliente(self, tipo):
        senha = self.fila_banco.inserir_cliente(tipo)
        self.status_label.config(text=f"Cliente inserido: {senha}")
        self.atualizar_lista()
    
    def atender_cliente(self):
        cliente = self.fila_banco.atender_cliente()
        if cliente:
            self.status_label.config(text=f"Cliente atendido: {cliente}")
            self.atualizar_lista()
        else:
            messagebox.showinfo("Aviso", "Não há clientes na fila!")

def main():
    root = tk.Tk()
    app = FilaBancoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
