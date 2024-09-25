"""
Exercicio Verificação de CPF

Desenvolva um programa que solicite a digitação 
de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido 
ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

https://www.geradordecpf.org/
"""

def calcula_digito(cpf, multiplicadores):
    
    soma = 0

    for i in range(len(multiplicadores)):
        
        soma += int(cpf[i]) * multiplicadores[i]

    resto = soma % 11
    
    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto 

    return str(digito)

cpf = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")

if len(cpf) != 14 or cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':

    print("Formato invalido!")

else:
     
    cpf_numerico = cpf.replace('.', '').replace('-', '')
        
    primeiro_digito = calcula_digito(cpf_numerico[:9], list(range(10, 1, -1)))

    segundo_digito = calcula_digito(cpf_numerico[:10], list(range(11, 1, -1)))

    if cpf_numerico[9] == primeiro_digito and cpf_numerico[10] == segundo_digito:
            print("Parabéns o CPF é válido!")
    else:
        print("CPF inválido!")






