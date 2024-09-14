frase = "Python é uma linguagem de programação poderosa e versátil"

print(frase)


##texto_conta = len(frase)
texto_conta = frase.count("")

print("O tamanho da frase é: ", texto_conta)

palavra = frase.split()[0]

print("Primeira palavra da frase: ", palavra)

###upper
frase_maiuscula = frase.upper()

print(frase_maiuscula)

frase_subistituida = frase.replace("poderosa", "incrivel")

print(frase_subistituida)