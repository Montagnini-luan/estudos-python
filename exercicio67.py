"""
Exercicío Programa de Validação de Senha

Seu desafio é criar um programa que solicite ao usuário um nome e uma senha. 
No entanto, existem regras específicas para a senha ser considerada válida:

    1. A senha não pode ser igual ao nome do usuário.
    2. A senha deve ter pelo menos 8 caracteres.
    3. A senha deve conter pelo menos um caractere numérico.
    4. A senha deve conter pelo menos um caractere especial (como !, @, #, etc.).
    5. O usuário tem um máximo de 3 tentativas para inserir uma senha válida.

Caso a senha inserida não atenda a um ou mais critérios, o programa deve exibir uma mensagem 
de erro e pedir que o usuário insira a senha novamente. Se o usuário exceder o limite de 
tentativas, o programa deve informá-lo e encerrar.

Seu programa deve continuar solicitando as informações até que o usuário insira uma senha 
válida ou atinja o limite de tentativas.

Dicas:

    Utilize estruturas de repetição para permitir múltiplas tentativas.
    A biblioteca re do Python pode ser útil para as verificações numéricas e 
    de caracteres especiais na senha.

Bônus:

    Implemente uma função que, além das verificações acima, verifique se a senha contém 
    pelo menos uma letra maiúscula e uma letra minúscula. Atualize as instruções do programa de acordo.
    
"""
import re

tentativas = 3

def validacao_senha(nome, senha):
        
    if senha.strip().lower() == nome.strip().lower():
        return "A senha nao pode ser igual ao nome"

    if len(senha) <= 8:
        return "A senha deve ter mais de 8 caracters"
    
    tem_numero = False

    for letra in senha:

        if letra.isdigit():
            tem_numero = True
            break

    if tem_numero == False:
        return print("A senha deve conter um numero")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return print("A senha deve conter ao menos um caractere especial.")

    tem_maiusculo = False

    for letra in senha:

        if letra.isupper():
            tem_maiusculo = True
            break

    if tem_maiusculo == False:
        return print("A senha deve conter pele menos un caracter maiusculo")
    
    tem_minusculo = False

    for letra in senha:

        if letra.islower():
            tem_minusculo = True
            break

    if tem_minusculo == False:
        return print("A senha deve conter pele menos un caracter minusculo")

    return ""

while tentativas > 0:
    
    nome = input("Digite o nome de usuario: ")
    senha = input("Digite sua senha: ")

    resultado = validacao_senha(nome, senha)

    if resultado:
        print(resultado)
        print(f"{tentativas} restantes")

        tentativas -= 1

    else:
        print("Senha valida!")
        break

    if tentativas == 0:
        print("Número máximo de tentativas atingido!")
    