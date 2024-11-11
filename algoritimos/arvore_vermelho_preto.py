import networkx as nx
import matplotlib.pyplot as plt

class No:
    def __init__(self, dado, cor, pai=None) -> None:
        self.dado = dado
        self.cor = cor
        self.pai = pai
        
        self.esquerda = None
        self.direita = None
        
class ArvoreVemelhoPreto:
    def __init__(self) -> None:
        self.raiz = None
        
    def _rotacionar_direita(self, no):
        temp = no.esquerda
        no.esquerda = temp.direita
        
        if temp.direita:
            temp.direita.pai = no
            
        temp.pai = no.pai
        
        if not no.pai:
            self.raiz = temp
            
        elif no == no.pai.esquerda:
            no.pai.esquerda = temp

        else:
            no.pai.direita = temp
            
        temp.direita = no
        no.pai = temp
        
    def _rotacionar_esquerda(self, no):
        temp = no.direita
        no.direita = temp.esquerda
        
        if temp.esquerda:
            temp.esquerda.pai = no
            
        temp.pai = no.pai
        
        if not no.pai:
            self.raiz = temp
            
        elif no == no.pai.esquerda:
            no.pai.esquerda = temp
            
        else:
            no.pai.direita = temp
            
        temp.esquerda = no
        no.pai = temp
        
        
    def inserir(self, valor):
        if not self.raiz:
            self.raiz = No(valor, "preto")
        
        else:
            self.inserir(self.raiz, valor)
            self.balancear(self.raiz)
            
    def _inserir(self, no, valor):
        if valor < no.dado:
            if no.esquerda:
                self._inserir(no.esquerda, valor)
                
            else:
                no.esquerda = No(valor, "vermelho", no)
                self.balancear(no.esquerda)
                
        elif valor > no.dado:
            if not no.direita:
                self._inserir(no, valor)
                
            else:
                no.direita = No(valor, "vermelho", no)
                self.balancear(no.direita)
                
    def balancear(self, no):
        while no.pai and no.pai.cor == "vermelho":
            if no.pai == no.pai.pai.esquerda:
                tio = no.pai.pai.direita
                
                if tio and tio.cor == "vermelho":
                    no.pai.cor = "preto"
                    tio.cor = "preto"
                    no.pai.pai.cor = "vermelho"
                    no = no.pai.pai
                    
                else:
                    if no == no.pai.direita:
                        no = no.pai
                        self.rotacionar_esquerda(no)
                        
                    no.pai.cor = "preto"
                    no.pai.pai.cor = "vermelho"
                    self.rotacionar_direita(no.pai.pai)
                    
            else:
                tio = no.pai.pai.esquerda
                
                if tio and tio.cor == "vermelho":
                    no.pai.cor = "preto"
                    tio.cor = "preto"
                    no.pai.pai.cor = "vermelho"
                    no = no.pai.pai
                    
                else:
                    if no == no.pai.esquerda:
                        no = no.pai
                        self.rotacionar_direita(no)
                        
                    no.pai.cor = "preto"
                    no.pai.pai.cor = "vermelho"
                    self.rotacionar_esquerda(no.pai.pai)
                    
        self.raiz.cor = "preto"

def adicionar_ao_grafo(no, grafo):
        if no is not None:
            grafo.add_node(no, color=no.cor, valor=no.dado)
            
            if no.pai:
                grafo.add_edge(no.pai, no)
                
            adicionar_ao_grafo(no.esquerda, grafo)
            
            adicionar_ao_grafo(no.direita, grafo)

def converter_cores_para_ingles(cores):
    mapeamento = {
        "preto": "black",
        "vermelho": "red"
    }
    
    return [mapeamento[cor] for cor in cores]

ordem_no = 0
def calcular_posicoes(raiz, ps={}, y=0):
    global ordem_no
    
    if raiz is not None:
        calcular_posicoes(raiz.esquerda, ps, y-1)
        ps[raiz] = (ordem_no, y)
        ordem_no += 1
        calcular_posicoes(raiz.direita, ps, y-1)
        
    return ps
  
def desenhar_arvore(arvore):
    grafo = nx.DiGraph()
    adicionar_ao_grafo(arvore.raiz, grafo)
    cores = []
    
    for no in grafo.nodes():
        cor = nx.get_node_attributes(grafo, "cor")[no]
        cores.append(cor)
        
    cores = converter_cores_para_ingles(cores)
    cores_borda = []

    for cor in cores:
        if cor == "black":
            cores_borda.append("white")
            
        else:
            cores_borda.append("black")
            
    pos = calcular_posicoes(arvore.raiz)
            
    nx.draw(grafo, pos, with_labels=False, node_color=cores, node_size=1000, edge_color='black',
            width=1.5, edgecolors=cores_borda, linewidths=2, font_size=10, font_weight="bold")
    
    for no, (x, y) in pos.items():
        plt.text(x, y, str(no.dado), fontsize=10, ha='center', va='center', color='white' if grafo.nodes[no]['cor'] == 'preto' else 'white')
        
    plt.show()
        
def main():
    arvore = ArvoreVemelhoPreto()
    
    valores = [10, 20, 30, 15, 25, 5, 35]
        
    for valor in valores:
        arvore.inserir(valor)
            
    desenhar_arvore(arvore)

if __name__ == "__main__":
    main()
