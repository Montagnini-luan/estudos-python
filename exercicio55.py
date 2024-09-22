"""
Exercício Cálculo do Salário com Horas Extras e Imposto de Renda

Objetivo: Desenvolver um programa que ajude o usuário a entender a 
composição do seu salário mensal. O programa deve considerar o valor 
recebido por hora, as horas trabalhadas no mês, o cálculo de horas 
extras e o desconto do imposto de renda.

Instruções:

    1. Solicite ao usuário o valor que ele ganha por hora.
    2. Pergunte quantas horas foram trabalhadas no mês.
    3. Calcule o salário bruto multiplicando o valor por hora 
    pelas horas trabalhadas.
    
    4. Se o usuário tiver trabalhado mais de 160 horas no mês, 
    calcule o valor das horas extras. Cada hora extra deve ser 
    compensada com um adicional de 50% sobre o valor da hora comum.
    
    5. Calcule o imposto de renda sobre o salário (considerando as horas extras). 
    O imposto de renda tem uma taxa fixa de 11% sobre o salário.
    
    6. Mostre ao usuário uma descrição detalhada contendo:
        - Salário Bruto.
        - Valor das Horas Extras (se aplicável).
        - Valor do Imposto de Renda.
        - Salário Líquido (Salário Bruto + Horas Extras - Imposto de Renda).
"""


valor_hora = float(input("Digite o quando voce ganha por hora: "))
horas_mes = float(input("Digite quantas horas foram trabaladas por mes: "))

salario_bruto = valor_hora * horas_mes

print(f"Seu salario bruto e: {salario_bruto:.2f}")

if horas_mes > 160:

    hora_extra = horas_mes - 160

    valor_extra = (valor_hora * 1.5) * hora_extra

    print(f"Voce recebeu de horas extra esse mes: {valor_extra:.2f}")

imposto_renda = (salario_bruto + valor_extra) * 0.11

print(f"Voce pagou {imposto_renda:.2f} de imoposto de renda esse mes")

print(f"Seu salario liquido e de {salario_bruto + valor_extra - imposto_renda:.2f}")

