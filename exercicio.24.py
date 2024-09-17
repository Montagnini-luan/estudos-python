a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

combinacoes = [(x, y) for x in a for y in b if x + y == 5]
print(combinacoes)

"""
combinacoes = []


for x in a:
    

    for y in b:
        

        if x + y == 5:
            

            combinacoes.append((x, y))


print(combinacoes)
"""
