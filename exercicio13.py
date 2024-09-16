numero = int(input("Digite um número positivo e inteiro: "))

if numero < 0:

    print("O número não pode ser negativo!")

else:

    fatorial = 1

    print("Cálculo do fatorial de", numero, ":")

for multiplicador in range(1, numero + 1):
        
    fatorial *= multiplicador
        
    print(f"{multiplicador}! =", end=" ")

    for i in range(1, multiplicador + 1):
            
            print(i, end="")
            
            if i != multiplicador:
                
                print(" * ", end="")
                
    print(" = ", fatorial)

print("O fatorial de", numero, "é:", fatorial)
