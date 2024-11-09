"""
Arvore Binaria de busca ABB
"""

import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configuração para melhor resolução do matplotlib
plt.rcParams['figure.dpi'] = 100
plt.style.use('default')  # Mudando de 'seaborn' para 'default'

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
     
        
class ABB:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)
    
    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivo(no.direita, valor)
    
    def tamanho_da_subarvore(self, no):
        if no is None:
            return 0
        return 1 + self.tamanho_da_subarvore(no.esquerda) + self.tamanho_da_subarvore(no.direita)
    
    def calcular_posicoes(self, no, profundidade=0, posicao=0, posicoes=None, delocamento=1.5):
        if posicoes is None:
            posicoes = {}
        if no:
            posicoes[no.valor] = (posicao, -profundidade)
            deslocamento_esquerda = self.tamanho_da_subarvore(no.esquerda)
            deslocamento_direita = self.tamanho_da_subarvore(no.direita)
            
            if no.esquerda:
                posicoes = self.calcular_posicoes(no.esquerda, profundidade+1, posicao-delocamento*(deslocamento_esquerda+1), posicoes)
            if no.direita:
                posicoes = self.calcular_posicoes(no.direita, profundidade+1, posicao+delocamento*(deslocamento_direita+1), posicoes)
                
        return posicoes
                
    def criar_grafo(self, no=None, grafo=None):
        if grafo is None:
            grafo = nx.DiGraph()
        if no:
            if no.esquerda:
                grafo.add_edge(no.valor, no.esquerda.valor)
                self.criar_grafo(no.esquerda, grafo)
            if no.direita:
                grafo.add_edge(no.valor, no.direita.valor)
                self.criar_grafo(no.direita, grafo)
        return grafo
    
    def excluir(self, valor):
        self.raiz = self._excluir_recursivo(self.raiz, valor)
        
    def _excluir_recursivo(self, no, valor):
        if not no:
            return no
        if valor < no.valor:
            no.esquerda = self._excluir_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._excluir_recursivo(no.direita, valor)
        else:
            if not no.esquerda:
                return no.direita
            elif not no.direita:
                return no.esquerda
            
            no.valor = self._valor_minimo(no.direita)
            no.direita = self._excluir_recursivo(no.direita, no.valor)
            
        return no
    
    def _valor_minimo(self, no):
        valor_atual = no.valor
        while no.esquerda:
            valor_atual = no.esquerda.valor
            no = no.esquerda
        return valor_atual
    
    def atualizar(self, valor_antigo, valor_novo):
        self.excluir(valor_antigo)
        self.inserir(valor_novo)
        
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        if valor < no.valor:
            return self._buscar_recursivo(no.esquerda, valor)
        return self._buscar_recursivo(no.direita, valor)


class InterfaceGrafica:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Árvore Binária de Busca")
        
        # Configurando o estilo
        style = ttk.Style()
        style.theme_use('clam')  # Usando o tema 'clam' que é mais moderno
        
        # Configurando cores e estilos personalizados
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TButton',
                       padding=6,
                       relief="flat",
                       background="#2196F3",
                       foreground="black",
                       hover=True,
                       font=('Helvetica', 9, 'bold'))
        
        style.configure('TLabel',
                       background='#f0f0f0',
                       font=('Helvetica', 10))
        
        style.configure('TEntry',
                       fieldbackground='white',
                       font=('Helvetica', 10))
        
        # Configurando a janela principal
        self.janela.configure(bg='#f0f0f0')
        self.janela.geometry("800x700")
        
        self.arvore = ABB()
        
        # Frame principal com borda e padding
        frame_entrada = ttk.Frame(janela, padding="10", relief="solid")
        frame_entrada.pack(pady=20, padx=20, fill=tk.X)
        
        # Seção de Inserção/Exclusão
        frame_insercao = ttk.LabelFrame(frame_entrada, text="Inserção/Exclusão", padding="10")
        frame_insercao.grid(row=0, column=0, columnspan=4, pady=(0,10), sticky="ew")
        
        ttk.Label(frame_insercao, text="Valor:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_valor = ttk.Entry(frame_insercao, width=15)
        self.entry_valor.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(frame_insercao, text="Inserir").grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(frame_insercao, text="Excluir").grid(row=0, column=3, padx=5, pady=5)
        
        # Seção de Atualização
        frame_atualizacao = ttk.LabelFrame(frame_entrada, text="Atualização", padding="10")
        frame_atualizacao.grid(row=1, column=0, columnspan=4, pady=(0,10), sticky="ew")
        
        ttk.Label(frame_atualizacao, text="Valor Atual:").grid(row=0, column=0, padx=5, pady=5)
        self.compo_valor_antigo = ttk.Entry(frame_atualizacao, width=15)
        self.compo_valor_antigo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_atualizacao, text="Novo Valor:").grid(row=0, column=2, padx=5, pady=5)
        self.compo_valor_novo = ttk.Entry(frame_atualizacao, width=15)
        self.compo_valor_novo.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Button(frame_atualizacao, text="Atualizar").grid(row=0, column=4, padx=5, pady=5)
        
        # Seção de Busca
        frame_busca = ttk.LabelFrame(frame_entrada, text="Busca", padding="10")
        frame_busca.grid(row=2, column=0, columnspan=4, pady=(0,10), sticky="ew")
        
        ttk.Label(frame_busca, text="Valor:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_buscar = ttk.Entry(frame_busca, width=15)
        self.entry_buscar.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(frame_busca, text="Buscar").grid(row=0, column=2, padx=5, pady=5)
        
        # Configurando o gráfico
        self.fig, self.eixo = plt.subplots(figsize=(10, 8))
        self.fig.patch.set_facecolor('#f0f0f0')
        self.eixo.set_facecolor('#f0f0f0')
        
        self.canvas = FigureCanvasTkAgg(self.fig, janela)
        self.canvas.get_tk_widget().pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Reconectando os comandos dos botões
        for child in frame_entrada.winfo_children():
            if isinstance(child, ttk.LabelFrame):
                for button in child.winfo_children():
                    if isinstance(button, ttk.Button):
                        if button['text'] == "Inserir":
                            button.configure(command=self.inserir_valor)
                        elif button['text'] == "Excluir":
                            button.configure(command=self.excluir_valor)
                        elif button['text'] == "Atualizar":
                            button.configure(command=self.atualizar_valor)
                        elif button['text'] == "Buscar":
                            button.configure(command=self.buscar_valor)
        
    def inserir_valor(self):
        try:
            valor = int(self.entry_valor.get())
            self.arvore.inserir(valor)
            self.atualizar_grafico()
            self.entry_valor.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Digite um número inteiro.")
            
    def excluir_valor(self):
        try:
            valor = int(self.entry_valor.get())
            self.arvore.excluir(valor)
            self.atualizar_grafico()
            self.entry_valor.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Digite um número inteiro.")
            
    def atualizar_valor(self):
        try:
            valor_antigo = int(self.compo_valor_antigo.get())
            valor_novo = int(self.compo_valor_novo.get())
            self.arvore.atualizar(valor_antigo, valor_novo)
            self.atualizar_grafico()
            self.compo_valor_antigo.delete(0, tk.END)
            self.compo_valor_novo.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Digite um número inteiro.")
            
    def atualizar_grafico(self):
        self.eixo.clear()
        grafo = self.arvore.criar_grafo(self.arvore.raiz)
        posicoes = self.arvore.calcular_posicoes(self.arvore.raiz)
        
        nx.draw(grafo, pos=posicoes, with_labels=True, arrows=False, 
                node_size=3000, node_color="skyblue", alpha=0.7, ax=self.eixo)
        self.canvas.draw()
        
    def buscar_valor(self):
        try:
            valor = int(self.entry_buscar.get())
            resultado = self.arvore.buscar(valor)
            
            if resultado:
                messagebox.showinfo("Resultado da busca", f"Valor encontrado: {valor}")
            else:
                messagebox.showinfo("Resultado da busca", f"Valor não encontrado: {valor}")
                
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Digite um número inteiro.")
        

if __name__ == "__main__":
    janela = tk.Tk()
    interface = InterfaceGrafica(janela)
    janela.mainloop()
