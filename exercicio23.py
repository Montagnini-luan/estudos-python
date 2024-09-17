
quadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
print(quadrados_pares)


quadrados_pares = []


for x in range(10):
    if x % 2 == 0:
        quadrados_pares.append(x**2)
print(quadrados_pares)

    