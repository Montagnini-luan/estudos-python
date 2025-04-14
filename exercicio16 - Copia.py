altura  = 5

for i in range(altura):

    espacos = altura - i - 1
    
    asteriscos = 2 * i + 1

    print(" " * espacos + "*" * asteriscos)