import xlsxwriter as opcoesDoXlsxWriter
import os

nomeCaminhoArquivo = 'C:\\Users\luanm\OneDrive\Desktop\Sites\Estudos\estudos python\Python RPA\PrimeiroExemplo.xlsx'

workbook = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetPadrao = workbook.add_worksheet()

sheetPadrao.write("A1", "Nome")
sheetPadrao.write("B1", "Idade")
sheetPadrao.write("A2", "Luan")
sheetPadrao.write("B2", 25)

workbook.close()

os.startfile(nomeCaminhoArquivo)