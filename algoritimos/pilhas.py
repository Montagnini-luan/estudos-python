class Pilha:
    def __init__(self):
        self.pratos = []
        
    def adicionar_prato(self, prato):
        self.pratos.append(prato)
        
    def remover_prato(self):
        if not self.esta_vazia():
            return self.pratos.pop()
        else:
            return "A pilha está vazia"
        
    def esta_vazia(self):
        return len(self.pratos) == 0
    
    def ver_topo(self):
        if not self.esta_vazia():
            return self.pratos[-1]
        else:
            return "A pilha está vazia"
        
    def quantidade_pratos(self):
        return len(self.pratos)
    
minha_pilha = Pilha()

minha_pilha.adicionar_prato("Prato 1")

print('Adicionando prato 1')

minha_pilha.adicionar_prato("Prato 2")

print('Adicionando prato 2')

minha_pilha.adicionar_prato("Prato 3")

print('Adicionando prato 3')

print(minha_pilha.ver_topo())

print(minha_pilha.remover_prato())

print(minha_pilha.ver_topo())
    
    
