class PilhaDeLivros:
    '''
    Criando uma pilha de livros
    '''
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Adicionando livro: {livro}')

    def remover_livro(self):
        if not self.livros:
            return "A pilha está vazia"
        return print(f'Removendo livro: {self.livros.pop()}')

    def ver_topo(self):
        if not self.livros:
            return "A pilha está vazia"
        return self.livros[-1]
    
    def esta_vazia(self):
        return len(self.livros) == 0
    
    def quantidade_livros(self):
        return len(self.livros)


'''
executando o programa
'''
def main():
    minha_pilha_de_livros = PilhaDeLivros()

    minha_pilha_de_livros.adicionar_livro("Livro A")
    minha_pilha_de_livros.adicionar_livro("Livro B")
    minha_pilha_de_livros.adicionar_livro("Livro C")
    minha_pilha_de_livros.adicionar_livro("Livro D")
    minha_pilha_de_livros.adicionar_livro("Livro E")

    minha_pilha_de_livros.remover_livro()
    minha_pilha_de_livros.remover_livro()
    minha_pilha_de_livros.remover_livro()

    minha_pilha_de_livros.adicionar_livro("Livro F")
    minha_pilha_de_livros.adicionar_livro("Livro G")

    minha_pilha_de_livros.remover_livro()
    minha_pilha_de_livros.remover_livro()

    print(minha_pilha_de_livros.quantidade_livros())

if __name__ == "__main__":
    main()





