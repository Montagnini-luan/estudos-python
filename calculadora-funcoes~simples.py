# Definindo as funções para as operações básicas

# Definindo a função para adicionar dois números
def adicionar(a, b):
    
    # Retorna a soma de a e b
    return a + b  

# Definindo a função para subtrair um número do outro
def subtrair(a, b):
    
    # Retorna a diferença entre a e b
    return a - b  

# Definindo a função para multiplicar dois números
def multiplicar(a, b):
    
    # Retorna o produto de a e b
    return a * b  

# Definindo a função para dividir um número pelo outro
def dividir(a, b):
    
    # Retorna a divisão de a por b
    return a / b  

# Solicitando ao usuário o primeiro número e convertendo-o para float
num1 = float(input("Digite o primeiro número: "))

# Solicitando ao usuário o segundo número e convertendo-o para float
num2 = float(input("Digite o segundo número: "))

# Solicitando ao usuário que escolha uma das operações definidas
op = input("Escolha uma operação (adicionar, subtrair, multiplicar, dividir): ")

# Usando condicionais para determinar qual função chamar com base na escolha do usuário
if op == "adicionar":
    
    # Chama a função de adição se o usuário escolheu 'adicionar'
    resultado = adicionar(num1, num2)  
    
elif op == "subtrair":
    
    # Chama a função de subtração se o usuário escolheu 'subtrair'
    resultado = subtrair(num1, num2)   
    
elif op == "multiplicar":
    
    # Chama a função de multiplicação se o usuário escolheu 'multiplicar'
    resultado = multiplicar(num1, num2) 
    
elif op == "dividir":
    
    # Chama a função de divisão se o usuário escolheu 'dividir'
    resultado = dividir(num1, num2)    

    if num2 == 0:

        print("não é possivél dividir por 0: ")

else:
    
    # Imprime uma mensagem de erro se o usuário não escolheu uma operação válida
    print("Operação inválida.")         

# Imprime o resultado da operação escolhida
print("Resultado:", resultado)
