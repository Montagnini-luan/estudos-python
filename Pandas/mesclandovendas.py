import pandas as pd

base_vendas_janeiro_df = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Vendas_Jan.xlsx')

base_vendas_fevereiro_df = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Vendas_Fev.xlsx')

base_vendas_marco_df = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Vendas_Mar.xlsx')

base_vendas_janeiro_df = base_vendas_janeiro_df._append(base_vendas_fevereiro_df)  #unindo as duas planilhas
print(base_vendas_janeiro_df)

resumindo_df = base_vendas_janeiro_df[["Vendedor", "Data Venda", 'Total Vendas']]
print(resumindo_df)

vendas_geral_df = pd.concat([base_vendas_janeiro_df, base_vendas_fevereiro_df, base_vendas_marco_df])  #junta varias planilias usando o concat
print(vendas_geral_df)

resumindo_df = vendas_geral_df[["Vendedor", "Data Venda", 'Total Vendas']]
print(resumindo_df)

#Keys conselhe separar os dataframes e criar gupos para nomealos
vendas_com_grupos = pd.concat([base_vendas_janeiro_df, base_vendas_fevereiro_df, base_vendas_marco_df], keys=["Janeiro", "Favereiro", "Marco"])  #junta varias planilias usando o concat
print(vendas_com_grupos)

extraindo_fevereiro = vendas_com_grupos.loc["Favereiro"]
print(extraindo_fevereiro)
