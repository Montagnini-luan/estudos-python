import pandas as pd

# Carregar os dados
vendas_df = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Groupby.xlsx')

# Filtrar apenas colunas numéricas
dados_numericos = vendas_df.select_dtypes(include='number')

# Adicionar novamente a coluna 'Vendedor' para o agrupamento
dados_numericos[['Vendedor', 'Produto']] = vendas_df[['Vendedor', 'Produto']]

# Calcular a média por vendedor mean = media ou sum para soma
#dropna=False deixa os valores em brancos
media_vendedor = dados_numericos.groupby(["Vendedor", "Produto"]).mean()

print(media_vendedor)



