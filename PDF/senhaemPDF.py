from PyPDF2 import PdfReader, PdfWriter
import os

try:

    arquivo = PdfReader("C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\PDF\\Mercado_Livre.pdf")

    novo_arquvo_pdf = PdfWriter()

    for pagina in arquivo.pages:

        novo_arquvo_pdf.add_page(pagina)

    novo_arquvo_pdf.add_metadata(
        {
            "/Author": "Luan",
            "/Creator": "Python PdfWeiter",
            "/Producer": "Curso de python PDF",
            "/Subject": "Ensinando a trabalhar com PDF",
            "/Title": "Curso RPA Python"
        }
    )

    novo_arquivo = "Arquivo_alterado_mercado_livre.pdf"

    with open(novo_arquivo, "wb") as dados_arquivo:
        
        novo_arquvo_pdf.write(dados_arquivo)

        if os.path.exists(novo_arquivo):

            print(f"Arquivo '{novo_arquivo}' criado com sucesso!")

        else:

            print("Erro ao criar o arquivo")

except FileNotFoundError:

    print("Arquivo PDF nao encontrado. Verifique o caminho do arquivo")

except Exception as e:

    print(f"Ocorreu um erro? {e}")