"""
Exercício: Comparação de Tuplas

Dadas as seguintes tuplas:

Responda as seguintes questões:

    1. Qual é maior: t1 ou t2?
    2. t3 é maior que t1?
    3. Compare t4 e t1. Qual é menor?
    4. t1 e t5 são iguais?

Nota: O objetivo deste exercício é fazer com que entendam o conceito
de comparação de tuplas em profundidade, observando 
a ordem dos elementos e como os diferentes elementos em diferentes posições 
influenciam o resultado da comparação.
"""
t1 = (3, 5)
t2 = (3, 4, 10)
t3 = (3, 6)
t4 = (2, 100)
t5 = (3, 5)

## 1 
print("Qual é maior: t1 ou t2?", "T1 é maior" if t1 > t2 else "T2 é maior")

##2
print("t3 é maior que t1?", "T3 é maior" if t3 > t1 else "T1 é maior")

##3
print("Compare t4 e t1. Qual é menor?", "T4 é memor" if t4 < t1 else "T1 é menor")

##4
print("t1 e t5 são iguais?", "T1 é igual a T5" if t1 == t5 else "São diferentes")