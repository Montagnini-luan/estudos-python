import pandas as pd

data_frame = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Deletar_Linhas_Colunas.xlsx')

deletando_linhas_branco = data_frame.dropna()  #Deleta as linhas em branco
#print(deletando_linhas_branco)

#del deletando_linhas_branco['Produto']  #Deleta uma coluna especifica
#rint(deletando_linhas_branco)

deletando_duas_colunas = deletando_linhas_branco.drop(columns=["Produto", "Data Venda"])

excluir_linha_3 = deletando_duas_colunas.drop(2, axis=0)
excluir_linha_3 = excluir_linha_3.drop([0 , 1], axis=0)  #Axis = eixo(1 - Coluna, 0 - linha)

print(excluir_linha_3)




