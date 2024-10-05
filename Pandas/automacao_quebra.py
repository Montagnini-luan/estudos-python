import pandas as pd
import xlsxwriter

base_dados_df = pd.read_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Pandas\\Vendas_Jan.xlsx')

removendo_duplicidades = base_dados_df.drop_duplicates(subset="Vendedor", keep="first")

for linha in removendo_duplicidades["Vendedor"]:

    
    vendas_funcionario = base_dados_df.loc[base_dados_df["Vendedor"] == linha]
    #vendas_funcionario.to_csv("Relatorio Vendas" + linha + ".csv")

    arquivo_exel = pd.ExcelWriter("Relatorio Vendas" + linha + ".xlsx", engine="xlsxwriter")
    arquivo_exel._save()

    data_frame = pd.DataFrame(vendas_funcionario)

    arquivo_exel = pd.ExcelWriter("Relatorio Vendas" + linha + ".xlsx", engine="xlsxwriter")

    data_frame.to_excel(arquivo_exel, sheet_name="Dados", index=False)

    arquivo_exel._save()



print("relatorio separadao com sucesso")
