def fibonacci(n):
    if n <= 0:
        return "Entrada inválida"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    seq = [0, 1]
    for i in range(2, n):
        next_number = seq[i-1] + seq[i-2]
        seq.append(next_number)
    return seq

# Teste a função com n elementos
n = 15
print(fibonacci(n))
