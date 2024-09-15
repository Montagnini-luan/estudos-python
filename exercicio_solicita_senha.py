"""
Exercício:

Crie um algoritmo que solicite ao usuário uma senha, e só sai do
looping do While quando for digitado a senha corretamente
"""

senha = 123

solicta_senha = int(input("Coloque a senha correta: "))


while (solicta_senha != senha):
    print("Senha incorreta tente novamente")
    solicta_senha = int(input("\nColoque a senha correta: "))

print("\nVocê acertou a senha!")