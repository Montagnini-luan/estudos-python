import pandas as pd
from regex import D

vendas_df = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Vendas_Merge.xlsx')
vendedores_df = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Vendedores_Merge.xlsx')

produtos_df = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Produtos_Merge.xlsx')


vendas_df = vendas_df.merge(vendedores_df)

vendas_df = vendas_df.merge(produtos_df)

resumo_df = vendas_df[["Vendedor", "Produto", "Total Vendas"]]

print(resumo_df)
