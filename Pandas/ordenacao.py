import pandas as pd

data_frame = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Ordenacao.xlsx')

ordenar_vendedor = data_frame.sort_values(by="Total Vendas")  #ordena de A - Z
print(ordenar_vendedor)

ordenar_duas_colunas = data_frame.sort_values(by=["Vendedor", "Produto"])  #Ordenando duas colunas 
print(ordenar_duas_colunas)

ordenar_vendedor = data_frame.sort_values(by="Vendedor", ascending=False)  #ordena de Z - A
print(ordenar_vendedor)