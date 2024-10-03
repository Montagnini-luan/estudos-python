import pandas as pd

base_data_frame = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Base_Vendas.xlsx')

#resumo_unicos = base_data_frame.nunique()  #Deixando apenas valore unicos
#print(resumo_unicos)

#confere_duplicidade = base_data_frame.duplicated(subset="Vendedor", keep="first")  #identificando valore duplicados
#print(confere_duplicidade)

#base_data_frame["Confere Duplicidade"] = base_data_frame.duplicated(subset="Vendedor", keep="first") #creiando uma nova coluna para conferir duplicidade
#print(base_data_frame)

remover_diplicidade = base_data_frame.drop_duplicates(subset="Vendedor", keep="first")  #removendo duplicidades
print(remover_diplicidade)


