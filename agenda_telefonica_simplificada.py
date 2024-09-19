def menu_agenda():
    print("\nMinha Agenda de Contatos")
    print("1. Adicionar contato")
    print("2. Alterar contato")
    print("3. Remover contato")
    print("4. Listar contatos")
    print("5. Sair\n")

def adicionar_contato(contatos):
    
    nome = input("\nDigite o nome do contato: ")
    
    telefone = input("Digite o número de telefone: ")
    
    contatos[nome] = telefone
    print(contatos)
    print("\nContato adicionado com sucesso!")


def alterar_contato(contatos):
    
    nome_atual = input("\nDigite o nome do contato que deseja alterar: ")

    if nome_atual in contatos:
        
        novo_nome = input("Digite o novo nome para o contato (deixe em branco para manter o nome atual): ")
        novo_telefone = input("Digite o novo número de telefone (deixe em branco para manter o atual): ")
        
        if novo_nome:
            
            if novo_nome in contatos:
                
                print("\nO nome informado já está em uso. Por favor, tente um nome diferente.")
                
                return
            
            contatos[novo_nome] = contatos[nome_atual]
            
            del contatos[nome_atual]
            
        else:
            
            novo_nome = nome_atual
        
        if novo_telefone:
            
            contatos[novo_nome] = novo_telefone
        
        print("\nContato atualizado com sucesso!")
        
    else:
        
        print("\nContato não encontrado!")

def listar_contatos(contatos):

    if not contatos:
        
        print("\nNenhum contato registrado!")
        
    for nome, telefone in contatos.items():
        
        print(f"\nNome: {nome}")
        print(f"Telefone: {telefone}")

def remover_contato(contatos):
    
    nome = input("\nDigite o nome do contato que deseja remover: ")

    if nome in contatos:
        
        del contatos[nome]
        
        print("\nContato removido com sucesso!")
        
    else:
        
        print("\nContato não encontrado!")


contatos= {}

while True:

    menu_agenda()

    nav_menu = int(input("Escolha uma opação: ")) 

    if nav_menu == 1:
        
        adicionar_contato(contatos)

    elif nav_menu == 2:

        alterar_contato(contatos)


    elif nav_menu == 3:
        
        remover_contato(contatos)

    elif nav_menu ==4:

        print(contatos)

    elif nav_menu == 5:
        break
