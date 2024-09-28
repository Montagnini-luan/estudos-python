import xlsxwriter
import os

nomeCaminhoArquivo = "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\Dolar e Euro Google.xlsx"
planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)
sheet1 = planilhaCriada.add_worksheet()

sheet1.write("A1", "Nome")
sheet1.write("B1", "Idade")
sheet1.write("A2", "Amanda")
sheet1.write("B2", 28)
sheet1.write("A3", "Roberto")
sheet1.write("B3", 25)

planilhaCriada.close()

os.startfile(nomeCaminhoArquivo)

import xlsxwriter
import os

nomeCaminhoArquivo = "A:\\Python RPA\\Extraindo Valor do Dolar e Euro e Salvando no Excel\\Dolar e Euro Google.xlsx"
planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)
sheet1 = planilhaCriada.add_worksheet()

#Escrevendo nas células
sheet1.write("A1", "Nome")
sheet1.write("B1", "Idade")
sheet1.write("A2", "Amanda")
sheet1.write("B2", 28)
sheet1.write("A3", "Roberto")
sheet1.write("B3", 25)

#Fechando o arquivo do Excel que está em segundo plano
planilhaCriada.close()

#Abro o arquivo
os.startfile(nomeCaminhoArquivo)


