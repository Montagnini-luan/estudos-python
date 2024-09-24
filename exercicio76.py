"""
Exercício Data com mês por extenso e validação

Desenvolva um programa que atenda às seguintes especificações:

    1. Solicite ao usuário que insira uma data. A data pode ser no 
    formato "DD/MM/AAAA", "DD-MM-AAAA" ou "DD.MM.AAAA".

    2. Valide se a data é válida. Isso inclui verificar:
        Se o dia é válido para o mês específico.
        Se o mês é válido (isto é, está entre 1 e 12).
        Se o ano é bissexto e o dia é válido para fevereiro.

    3. Caso a data seja inválida, retorne "NULL".

    4. Se a data for válida, converta-a para o formato "D de mesPorExtenso de AAAA".

    5. Crie uma função chamada dataPorExtenso que aceite a data inserida e retorne a 
        data no formato desejado ou "NULL" caso seja inválida.

    6. Exiba o resultado para o usuário.
"""

data_digitada = input("Digite uma data no formato (DD/MM/AAAA, DD-MM-AAAA ou DD.MM.AAAA): ")

def bissexto(ano):

    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def validar_data(dia, mes, ano):

    if mes < 1 or mes > 12:
        return False
    
    if dia < 1:
        return False
    
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    
    if mes == 2:
        if bissexto(ano) and dia > 29:
            return False
        
        if not bissexto(ano) and dia > 28:
            return False
    
    if dia > 31:
        return False

    return True

meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]

def dataPorExtenso(data):

    if "/" in data:

        dia, mes, ano = data.split("/")

    elif "-" in data:

        dia, mes, ano = data.split("-")

    elif "." in data:

        dia, mes, ano = data.split(".")
    
    else:
        return "Null"
    
    dia, mes, ano = int(dia), int(mes), int(ano)

    if not validar_data(dia, mes, ano):

        return "Null"
    
    return f"{dia} de {meses[mes-1]} de {ano}"

resultado = dataPorExtenso(data_digitada)

print(resultado)