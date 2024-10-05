import pandas as pd

planilha_id = '1uxYa8NKhoPQVAO_LNqNWxyn30qn5S_qD'

dados_DF = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{planilha_id}/export?format=csv")

print(dados_DF)

"""
Desafio

1 - Após carregar os dados, deixe somente as colunas de Vendedor e Total de Vendas
2 - Com o groupby, use a coluna de vendedor para criar um resumo do vendedor e a soma total das vendas
3 - Salve o dataFrame como um arquivo de Excel

Parece fácil, mas não é! Boa sorte!

"""

excluir_colunas = dados_DF.drop(columns=["Produto", "Data Venda"])  #excluindo colunas

dados_numericos = excluir_colunas.select_dtypes(include='number')  # Pegando apenas os dados numericos

excluir_colunas['Total Vendas'] = excluir_colunas['Total Vendas'].str.replace(',','.')  # Subistituindo as , por .

excluir_colunas['Total Vendas'] = excluir_colunas['Total Vendas'].astype(float)  # Convertendo os numeros para float

soma_dados = excluir_colunas.groupby(["Vendedor"]).sum()  #Somando os numeros

print(soma_dados)  # Mostrando os numeros

arquivoExcel = pd.ExcelWriter("Resposta Desafio.xlsx", engine="xlsxwriter")
arquivoExcel._save()  # Criando a pasta e salvando ela usan o motor xlsxwriter

soma_dados.to_csv("Resposta Desafio.csv")  # Criando um arquivo .csv

dataFrame = pd.DataFrame(soma_dados)  #Transformando os dados em dataFrame

arquivoExcel = pd.ExcelWriter("Resposta Desafio.xlsx", engine="xlsxwriter")  #Criando o arquivo excel 
    

dataFrame.to_excel(arquivoExcel, sheet_name="Dados", index=True)  #Mudando o nome da planilha e salvando
arquivoExcel._save()

