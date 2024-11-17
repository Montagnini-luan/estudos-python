import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk


class GrafoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Grafo")
        self.root.geometry("800x600")
        
        self.criar_grafo()
        self.criar_widgets()
        
    def criar_grafo(self):
        self.g = nx.DiGraph()
        
        self.g.add_edge('0', '1')
        self.g.add_edge('1', '2')
        self.g.add_edge('2', '3')
        self.g.add_edge('3', '0')
        self.g.add_edge('0', '2')
        
        self.pos = {
            '0': (-1, 1),
            '1': (1, 1),
            '2': (1, -1),
            '3': (-1, -1)
        }
        
    def desenhar_grafo(self):
        plt.clf()
        nx.draw(
            self.g,
            self.pos,
            with_labels=True,
            node_size=1000,
            node_color='skyblue',
            font_size=10,
            font_weight='bold',
            edge_color='gray',
            arrows=True,
            arrowstyle='-|>',
            arrowsize=10
        )
        self.canvas.draw()
        
    def adicionar_aresta(self):
        origem = self.entrada_origem.get()
        destino = self.entrada_destino.get()
        
        if origem and destino:
            self.g.add_edge(origem, destino)
            self.desenhar_grafo()
            self.entrada_origem.delete(0, tk.END)
            self.entrada_destino.delete(0, tk.END)
            
    def remover_aresta(self):
        origem = self.entrada_origem.get()
        destino = self.entrada_destino.get()
        
        if origem and destino and self.g.has_edge(origem, destino):
            self.g.remove_edge(origem, destino)
            self.desenhar_grafo()
            self.entrada_origem.delete(0, tk.END)
            self.entrada_destino.delete(0, tk.END)
            
    def criar_widgets(self):
        frame_controles = ttk.Frame(self.root, padding="10")
        frame_controles.pack(fill=tk.X)
        
        ttk.Label(frame_controles, text="Origem:").pack(side=tk.LEFT, padx=5)
        self.entrada_origem = ttk.Entry(frame_controles, width=5)
        self.entrada_origem.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(frame_controles, text="Destino:").pack(side=tk.LEFT, padx=5)
        self.entrada_destino = ttk.Entry(frame_controles, width=5)
        self.entrada_destino.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_controles, text="Adicionar Aresta", 
                  command=self.adicionar_aresta).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_controles, text="Remover Aresta", 
                  command=self.remover_aresta).pack(side=tk.LEFT, padx=5)
        
        frame_grafo = ttk.Frame(self.root)
        frame_grafo.pack(fill=tk.BOTH, expand=True)
        
        fig = plt.figure(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(fig, master=frame_grafo)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.desenhar_grafo()


def main():
    root = tk.Tk()
    app = GrafoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
