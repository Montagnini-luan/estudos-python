"""
Exercício: Fábrica de Funções de Operações Matemáticas

Imagine que você está construindo uma calculadora. Porém, ao invés de 
implementar cada operação matemática (soma, subtração, multiplicação e divisão) 
diretamente, você decide criar uma "fábrica de funções". Esta fábrica, quando fornecida 
com o nome de uma operação, deve retornar uma função que realiza a operação desejada.

Instruções:

    - Escreva uma função chamada fábrica_de_operacoes que aceite uma 
    string: 'soma', 'subtracao', 'multiplicacao' ou 'divisao'.
    
    - Dependendo do argumento fornecido, sua função deve retornar uma das 
    operações matemáticas. Por exemplo, se o argumento for 'soma', a função 
    retornada deve ser capaz de somar dois números.
    
    - Se a operação não for reconhecida, retorne uma função que 
    imprima "Operação não suportada.".
    
    
Desafio Extra:
Adapte a fábrica para aceitar operações com 
mais de dois números. Por exemplo, a operação de soma deve 
ser capaz de somar três, quatro ou mais números de uma só vez.

Dica: Utilize argumentos variáveis (*args) para essa adaptação.
"""

def fábrica_de_operacoes(operacao):

    def soma(*args):
        return sum(args)
    
    def subtracao(*args):
        resultado = args[0]
        for num in args[1:]:
            resultado -= num
        return resultado
    
    def multiplicacao(*args):
            resultado = 1
            for num in args:
                resultado *= num
            return resultado
    
    def divisao(*args):
        resultado = args[0]
        for num in args[1:]:
            if num != 0:
                resultado /= num
            else:
                return "Erro: Divisão por zero"
        return resultado
    
    if operacao == "soma":
        return soma
    
    elif operacao == "subtracao":
        return subtracao
    
    elif operacao == "multiplicacao":
        return multiplicacao
    
    elif operacao == "divisao":
        return divisao

    else:
        def nao_suportada(*args):
            return "Operação não suportada."
        return nao_suportada

    
operacao_soma = fábrica_de_operacoes('soma')
print(operacao_soma(1, 2, 3, 4)) 

operacao_subtracao = fábrica_de_operacoes('subtracao')
print(operacao_subtracao(10, 5, 1)) 

operacao_multiplicacao = fábrica_de_operacoes('multiplicacao')
print(operacao_multiplicacao(2, 3, 4)) 

operacao_divisao = fábrica_de_operacoes('divisao')
print(operacao_divisao(100, 5, 2)) 

operacao_invalida = fábrica_de_operacoes('modulo')
print(operacao_invalida(5, 3)) 






