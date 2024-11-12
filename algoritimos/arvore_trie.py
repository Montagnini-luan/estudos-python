import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configuração para melhor resolução do matplotlib
plt.rcParams['figure.dpi'] = 100
plt.style.use('default')

class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False

class Trie:
    def __init__(self):
        self.raiz = NoTrie()
        
    def insert(self, palavra):
        no = self.raiz
        for char in palavra:
            if char not in no.filhos:
                no.filhos[char] = NoTrie()
            no = no.filhos[char]
        no.fim_palavra = True

class AppTrie(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Visualização da Árvore Trie")
        self.geometry("800x700")
        
        # Configurando o estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        self.configure(bg='#f0f0f0')
        
        self.trie = Trie()

        # Frame principal
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame para entrada e botão
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(pady=10)
        
        # Entrada de texto
        self.entrada = ttk.Entry(input_frame, width=50)
        self.entrada.pack(side=tk.LEFT, padx=5)
        
        # Botão de inserir
        self.botao_inserir = ttk.Button(input_frame, text="Inserir Palavra", 
                                      command=self.inserir_palavra)
        self.botao_inserir.pack(side=tk.LEFT, padx=5)
        
        # Frame para o canvas
        self.canvas_frame = ttk.Frame(main_frame)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configurando o gráfico inicial
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        self.fig.patch.set_facecolor('#f0f0f0')
        self.ax.set_facecolor('#f0f0f0')
        
        self.canvas = FigureCanvasTkAgg(self.fig, self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def inserir_palavra(self):
        palavra = self.entrada.get()
        if palavra:
            self.trie.insert(palavra)
            self.mostrar_trie()
            self.entrada.delete(0, tk.END)
            
    def mostrar_trie(self):
        self.ax.clear()
        G = nx.DiGraph()
        labels = {}
        posicao = {}
        niveis = {}
        
        def visitar_no(no, parent_name, caminho_atual, nivel):
            nome_no_atual = parent_name if parent_name else "raiz"
            
            if nome_no_atual not in G:
                G.add_node(nome_no_atual)
                
            for char, filho_no in no.filhos.items():
                nome_no = caminho_atual + char
                G.add_edge(nome_no_atual, nome_no)
                labels[nome_no] = char
                
                if nivel not in niveis:
                    niveis[nivel] = []
                niveis[nivel].append(nome_no)
                
                visitar_no(filho_no, nome_no, nome_no, nivel + 1)
                
        visitar_no(self.trie.raiz, "", "", 1)
        
        # Calculando posições
        for nivel, nos in niveis.items():
            total_nos = len(nos)
            for idx, no in enumerate(nos):
                x = idx - total_nos / 2
                y = -nivel
                posicao[no] = (x, y)
                
        # Adicionando posição para a raiz
        if G.nodes:
            posicao["raiz"] = (0, 0)
            labels["raiz"] = "○"

        nx.draw(G, pos=posicao, labels=labels, with_labels=True, 
               node_size=3000, node_color='skyblue', 
               font_size=12, alpha=0.7, ax=self.ax)
        
        self.canvas.draw()

def main():
    app = AppTrie()
    app.mainloop()

if __name__ == "__main__":
    main()
        
        
