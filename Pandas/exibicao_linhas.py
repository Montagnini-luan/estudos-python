import pandas as pd

vendas_dataframe = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Vendas_Jan.xlsx')

#print(vendas_dataframe)  # exibe a planilha

#print(vendas_dataframe.index)  # exibe o numero de linhas

#print(vendas_dataframe.columns)  # exibe as colunas

#print(vendas_dataframe.head(8))  # exibe os 5 primeiros itens no valor padrao, entre aspas seleciona o numero desejado

#print(vendas_dataframe.tail(4))  # exibe as ultimas linhas

#print(vendas_dataframe[["Vendedor", "Total Vendas"]].head())  #exibe uma coluna especifico fincona com o head ou tail

#print(vendas_dataframe.loc[2:7])  #seleciona um chunk especifico

#Localiza um elemento especifico e limita as colunas a exibir
#vendas_Leonardo_Almeida_DF = vendas_dataframe.loc[vendas_dataframe["Vendedor"] == "Leonardo Almeida", ["Vendedor", "Total Vendas"]]
#print(vendas_Leonardo_Almeida_DF)

print(vendas_dataframe.shape)  #Mostra quantas linhas e colunas ecistem





