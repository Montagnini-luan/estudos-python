from PyPDF2 import PdfReader
import datetime

try:
    arquivo_pdf = PdfReader("C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\PDF\\Mercado_Livre.pdf")

    dados = arquivo_pdf.metadata

    numero_paginas = len(arquivo_pdf.pages)

    print("Autor:", dados.author if dados.author else "Nao disponivel")
    print("Criador:", dados.creator if dados.creator else "Nao disponivel")
    print("Produtor:", dados.producer if dados.producer else "Nao disponivel")
    print("Assunto:", dados.subject if dados.subject else "Nao disponivel")
    print("Titulo:", dados.title if dados.title else "Nao disponivel")

    print(f"Numero total de paginas: {numero_paginas}")

    print(f"Documento Criptografado:", "sim" if arquivo_pdf.is_encrypted else "Nao")

    data_criacao = dados.get("/CreationDate", "Nao disponivel")
    data_modificacao = dados.get("/ModDate", "Nao disponivel")

    if data_criacao != "Nao disponivel":

        data_criacao = datetime.datetime.strptime(data_criacao[2:-7], '%Y%m%d%H%M%S')
        print("Data de criacao", data_criacao)

    else:

        print("data de criacao: Nao disponivel")

except FileNotFoundError:

    print("Arquivo PDF nao enctrado. Verifique o caminho do arquivo")

except Exception as e:

    print(f"Aconteceu um erro: {e}")

