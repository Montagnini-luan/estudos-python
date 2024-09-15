"""
Exercício

Entrada para um Evento Exclusivo

Você foi convidado para um evento exclusivo. Para entrar, você deve 
atender a pelo menos uma das seguintes condições:

    Ter um convite VIP.
    Estar na lista de convidados.
    Ser um membro do clube.

    Execute o programa.
    
    Responda às perguntas fornecidas com 'sim' ou 'não'.
    O programa irá informar se você pode entrar no evento ou não.
    
    
    Bem-vindo(a) ao evento!
    Desculpe, você não pode entrar no evento.
    
"""

vip = input("Você tem um convite VIP? (sim ou não) ")
membro = input("Você é um membro do clube? (sim ou não) ")
convidado = input("Vocé está na lista de convidado? (sim ou não) ")

if vip == "sim" or membro == "sim" or convidado == "sim":
    print("Bem-vindo(a) ao evento!")

else:
    print("Desculpe, você não pode entrar no evento.")
