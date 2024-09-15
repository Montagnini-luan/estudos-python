"""
Exercício:

Classificação de Notas

Neste exercício, seu objetivo é executar um programa que 
classifica as notas de um estudante em diferentes categorias.

    Execute o programa.
    
    Insira a nota do estudante quando solicitado (entre 0 e 100).
    
    O programa irá informar a classificação da nota de acordo com os seguintes critérios:
        Excelente: 90-100
        Bom: 70-89
        Satisfatório: 50-69
        Insuficiente: 0-49
"""

nota = int(input("Por favor, digite a nota do estudante (0-100): "))

if nota >= 90 and nota <= 100:
    print("Sua nota é exelente!")
elif nota >= 70 and nota <= 89:
    print("Sua nota é boa!")
elif nota >= 50 and nota <= 69:
    print("Sua nota é  satisfatoria.")
else:
    print("Sua nota é insuficiente.")