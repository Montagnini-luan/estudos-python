"""
Conversor de Valores para Extenso

Escreva um programa que faça a seguinte tarefa:

    1. Solicite ao usuário a entrada de um valor inteiro 
    em reais, sem considerar os centavos e com um limite de até 1 trilhão.
    
    2. O programa deve converter esse valor numérico para sua representação 
    por extenso na língua portuguesa.
    
    3. Exibir o valor por extenso, seguido da palavra "reais".
    
    4. Por exemplo, se o usuário inserir 150, o programa deve 
    exibir Cento e cinquenta reais.
    
    5. O programa deve tratar possíveis erros na entrada, 
    informando ao usuário quando ele não inserir um número válido.
    
    6. Após a conversão, o programa deve perguntar ao usuário se 
    ele deseja converter outro valor. Se a resposta não for "sim", o 
    programa deve ser encerrado.

Restrições:

    - O programa deve aceitar números de 0 a 999.999.999.999 (um trilhão menos um).
    - Não considere valores negativos ou com centavos.
    - As entradas inválidas devem ser tratadas apropriadamente, solicitando ao usuário que insira novamente o valor.
"""

def unidade_extenso(n):
    unidade = [" ", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]

    return unidade[n]

def dezena_extenso(n):
    dezenas = [" ", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sesenta", "setenta", "oitenta", "noventa"]

    especiais = {11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezessei", 17: "dezessete", 18: "dezoito", 19:"dezenove"}
    
    if 10 < n < 20:
        return especiais[n]

    else:
        unidade = n % 10

        dezena = n // 10

        if unidade == 0:
            return dezenas[dezena]

        else:
            return dezenas[dezena] + " e " + unidade_extenso(unidade)
        
def centena_extenso(n):

    if n == 100:
        return "cem"
    
    centenas = [" ", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    centena = n // 100

    resto = n % 100

    if resto == 0:
        return centenas[centena]

    elif resto < 10:
        return centenas[centena] + " e " + unidade_extenso(resto)
    
    else:
        return centenas[centena] + " e " + dezena_extenso(resto)

def centavo_extenso(n):
    
    if n == 1:
        
        return "Um Centavo"
    
    elif n < 10:
        
        return unidade_extenso(n) + " Centavos"
    
    else:
        
        return dezena_extenso(n) + " Centavos"
    
def converter_extenso(n):
    
    if n < 10:   
        return unidade_extenso(n)
    
    elif n < 100:
        return dezena_extenso(n)
    
    elif n < 1000:
        return centena_extenso(n)
    
    elif n < 10**6:
        
        milhares = n // 1000
        resto = n % 1000

        if milhares == 1: 
            return "mil" + (" e " + converter_extenso(resto) if resto > 0 else "")
        
        else:        
            return converter_extenso(milhares) + " mil" + (" e " + converter_extenso(resto) if resto > 0 else "")    
       
    elif n < 10**9: 
        
        milhoes = n // 10**6 
        resto = n % 10**6  


        if milhoes == 1:
            return "um milhão" + (" e " + converter_extenso(resto) if resto > 0 else "")
        
        else:
            return converter_extenso(milhoes) + " milhões" + (" e " + converter_extenso(resto) if resto > 0 else "") 
        
    elif n < 10**12: 
        
        bilhoes = n // 10**9
        resto = n % 10**9

        if bilhoes == 1:
            return "um bilhão" + (" e " + converter_extenso(resto) if resto > 0 else "")
        
        else:
            return converter_extenso(bilhoes) + " bilhões" + (" e " + converter_extenso(resto) if resto > 0 else "")

while True:

    try:

        numero = input("Digite um numero inteiro: ")

        resultado = numero.partition('.')

        reais = resultado[0]
        _ = resultado[1]
        centavos = resultado[2]

        if reais:
            numero_reais = int(reais)

        else:
            numero_reais = 0
        
        if centavos:
            numero_centavos = int(centavos)

        else:
            numero_centavos = 0
        
        if 0 <= numero_reais < 10**12 and 0 <= numero_centavos < 100:

            if numero_reais > 0:
                extenso_reais = converter_extenso(numero_reais)

                if numero_reais > 1:
                    extenso_reais += " Reais"
                        
                else:  
                    extenso_reais += " Real"
                    
            else:
                extenso_reais = ""  
                    
            extenso_centavos = ""

            if numero_centavos > 0:
                extenso_centavos = centavo_extenso(numero_centavos)
                    
            if extenso_reais and extenso_centavos:      
                extenso = extenso_reais + " e " + extenso_centavos
                    
            else:   
                extenso = extenso_reais + extenso_centavos        
                    
            print(extenso)  

        else:
            print("Por favor, insira um número válido e menor que 1 trilhão.")

    except ValueError:
        print("Digite um valor valido!")

    opcao = input("Voce deseja digitar um novo numeor (sim/nao)?: ").strip().lower()
    if opcao != "sim":
        break