import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl import workbook

caminho_arquivos = "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\Arquivos_Consolidar"

lista_arquivos = os.listdir(caminho_arquivos)

caminho_consolidado = r'C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\Arquivos_Consolidar\\Arquivo Consolidado.xlsx'
planilha_consolidada = load_workbook(filename=caminho_consolidado)

lista_arquivo_bloco = [caminho_arquivos + '\\' + arquivo for arquivo in lista_arquivos if arquivo[-3:] == 'txt']

dados_arquivos = pd.DataFrame()

for arquivo in lista_arquivo_bloco:

    quebraLinha = arquivo.split(',')

    dados = pd.read_csv(arquivo)

    dados_arquivos = pd.concat([dados_arquivos, dados])

dados_arquivos.to_excel('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\Arquivos_Consolidar\\Arquivo Consolidado.xlsx')
##dados_arquivos.to_csv('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\Arquivos_Consolidar\\Arquivo Consolidado.csv')
