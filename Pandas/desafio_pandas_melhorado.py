import pandas as pd

# ID da planilha no Google Sheets
planilha_id = '1uxYa8NKhoPQVAO_LNqNWxyn30qn5S_qD'

# Carregando os dados da planilha
dados_DF = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{planilha_id}/export?format=csv")

print(dados_DF)

# Desafio
# 1 - Deixe somente as colunas de Vendedor e Total de Vendas
dados_DF = dados_DF[['Vendedor', 'Total Vendas']]

# 2 - Converter "Total Vendas" para float após substituir vírgulas por pontos
dados_DF['Total Vendas'] = dados_DF['Total Vendas'].str.replace(',', '.').astype(float)

# 3 - Criar um resumo do vendedor com a soma total das vendas usando groupby
soma_dados = dados_DF.groupby(['Vendedor']).sum()

# Mostrar o resultado
print(soma_dados)

# 4 - Salvar o DataFrame como um arquivo de Excel
with pd.ExcelWriter("Resposta_Desafio.xlsx", engine="xlsxwriter") as arquivoExcel:
    soma_dados.to_excel(arquivoExcel, sheet_name="Dados")

# Opcional: também pode salvar como CSV
soma_dados.to_csv("Resposta_Desafio.csv")

print("Relatórios gerados com sucesso!")