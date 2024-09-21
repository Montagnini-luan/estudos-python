"""
Exercício Operações Matemáticas Básicas

Objetivo: Desenvolver um programa que solicite ao usuário a entrada
de dois números e, com base nesses números, realize as seguintes operações:

    1. Calcular e mostrar a soma dos dois números.
    
    2. Calcular e mostrar a subtração do primeiro número pelo segundo.
    
    3. Calcular e mostrar a multiplicação dos dois números.
    
    4. Calcular e mostrar a divisão do primeiro número pelo 
    segundo (se o segundo número não for zero).
    
    5. Verificar e informar se algum dos números (ou ambos) é zero.
    
    6. Calcular e mostrar a média dos dois números.
    
    7. Comparar os dois números e informar qual é maior ou se são iguais.
    
"""

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

soma = num1 + num2
print(f"A soma dos dois numeros e {soma}")

subtracao = num1 - num2
print(f"A subtracao dos dois numeros e {subtracao}")

multiplicacao = num1 * num2
print(f"A multiplicacao dos dois numeros e {multiplicacao}")

if num2 != 0:
    divisao = num1 / num2
    print(f"A divisao dos dois numeros e {divisao}")
else:
    print("Impossivel dividir por '0' selecione outro numero!")

if num1 == 0:
    print(f"O primeiro número informado é zero.")
if num2 == 0:
    print(f"O segundo número informado é zero.")
if num1 == 0 and num2 == 0:
    print(f"Ambos os números são iguais a zero.")

media = soma / 2

if num1 > num2:
    print(f"O numero {num1} e maior que o {num2} ")
elif num2 > num1:
    print(f"O numero {num2} e maior que o {num1} ")
else:
    print(f"O {num1} e {num2} sao iguais")