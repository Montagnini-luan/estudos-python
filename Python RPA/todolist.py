"""
Crie um menu para as opções: adicionar tarefa, remover tarefa e visualizar tarefas.

Armazene as tarefas em uma lista.

Adicione funcionalidades para:

Adicionar uma nova tarefa.

Remover uma tarefa existente.

Exibir todas as tarefas.
"""

class ToDoList:
    def __init__(self):
        self.to_do = []

    def adicionar_lista(self, item):
        if item:
            self.to_do.append(item)
            print("Item adicionado com sucesso!")
        else:
            print("Não é possível adicionar um item vazio.")

    def remover_lista(self, item):
        if item in self.to_do:
            self.to_do.remove(item)
            print("Item removido com sucesso!")
        else:
            print("Item não está na lista")

    def exibir_lista(self):
        if not self.to_do:
            print("Lista de tarefas está vazia.")
        else:
            print("Lista de tarefas:")
            for index, item in enumerate(self.to_do, start=1):
                print(f"{index}. {item}")

def menu():
    td = ToDoList()

    while True:
        print("\nTo-Do List")
        print("1- Adicionar um item à lista")
        print("2- Remover um item da lista")
        print("3- Exibir lista")
        print("5- Sair")

        nav = input("Digite uma opção válida: ")

        if nav == "1":
            item = input("Digite o nome do item que você deseja adicionar: ")
            td.adicionar_lista(item)
        
        elif nav == "2":
            item_remover = input("Digite o nome do item que você deseja remover: ")
            td.remover_lista(item_remover)
        
        elif nav == "3":
            td.exibir_lista()
        
        elif nav == "5":
            print("Saindo do programa... Até logo!")
            break
        
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()
