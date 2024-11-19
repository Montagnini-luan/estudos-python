import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

grafo = nx.DiGraph()

vertices_atributos = {
    0: {"cor": "blue", "tamanho": 300},   # Vértice 0 terá cor azul e tamanho 300
    1: {"cor": "green", "tamanho": 400},  # Vértice 1 terá cor verde e tamanho 400
    2: {"cor": "red", "tamanho": 500},    # Vértice 2 terá cor vermelha e tamanho 500
    3: {"cor": "yellow", "tamanho": 600}, # Vértice 3 terá cor amarela e tamanho 600
    4: {"cor": "orange", "tamanho": 700}  # Vértice 4 terá cor laranja e tamanho 700
}

for vertice, atributos in vertices_atributos.items():
    grafo.add_node(vertice, **atributos)

arestas_atributos = {
    (0, 1): {"peso": 5},
    (0, 2): {"peso": 3},
    (1, 3): {"peso": 2},
    (2, 4): {"peso": 4},
    (3, 4): {"peso": 1},
}
    
grafo.add_edges_from(arestas_atributos.keys())

for aresta, atributos in arestas_atributos.items():
    grafo[aresta[0]][aresta[1]].update(atributos)

graus = dict(grafo.degree())

valores_graus = list(graus.values())

media_graus = np.mean(valores_graus)
print(f"Média dos graus dos vértices: {media_graus:.2f}")

densidade_do_grafo = nx.density(grafo)
print(f"Densidade do grafo: {densidade_do_grafo:.2f}")

print("informacao dos vertices")
vertices_df = pd.DataFrame(vertices_atributos).T
print(vertices_df)

print("informacao das arestas")
arestas_df = pd.DataFrame(arestas_atributos).T
print(arestas_df)

cores = []

for vertice, atributos in grafo.nodes(data=True):
    cor_do_vertice = atributos["cor"]
    cores.append(cor_do_vertice)
    
tamanhos = []

for vertice, atributos in grafo.nodes(data=True):
    tamanho_do_vertice = atributos["tamanho"]
    tamanhos.append(tamanho_do_vertice)
    
pesos = []

for origem, destino, atributos in grafo.edges(data=True):
    peso_atual = atributos["peso"]
    pesos.append(peso_atual)

posicionamento = nx.spring_layout(grafo)
nx.draw_networkx_nodes(grafo, posicionamento, node_color=cores, node_size=tamanhos)
nx.draw_networkx_edges(grafo, posicionamento, arrows=True, arrowsize=20, width=pesos)
nx.draw_networkx_labels(grafo, posicionamento)
plt.title("Grafo com Lista de Adjacência")
plt.show()
