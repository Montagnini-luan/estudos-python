import pandas as pd

data_frame = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Tratamento_Dados.xlsx')

data_frame["Total Vendas"] = data_frame["Total Vendas"].fillna(data_frame["Total Vendas"].mean())  #preenche todos os espacos vazios com a media

print(data_frame)



