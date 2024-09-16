"""
# Solicitando ao usuário o número
N = int(input("Digite um número inteiro positivo: "))

# Inicializando a variável para armazenar a soma
soma_pares = 0

# Utilizando um loop for para somar os números pares de 1 até N
for i in range(1, N + 1):
    
    # Verificando se o número é par
    if i % 2 == 0: 
        
        #Imprime cada etapa
        print(f"Número: {i} + {soma_pares} = {i+soma_pares}")
        
        soma_pares += i
        
# Imprimindo o resultado
print(f"A soma dos números pares de 1 até {N} é: {soma_pares}")
"""

numero = int(input("Digite o número de somas dos pares: "))
resultado = 0

for i in range(0 , numero + 1, 2):

    print(f"Número: {i} + {resultado} = {i+resultado}")

    resultado += i

print(f"A soma dos números pares de 1 até {numero} é: {resultado}")