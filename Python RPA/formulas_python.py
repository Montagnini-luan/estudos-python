import xlsxwriter as opcoesDoXlsxWriter
import os

nomeCaminhoArquivo = 'C:\\Users\luanm\OneDrive\Desktop\Sites\Estudos\estudos python\Python RPA\Formulas.xlsx'

minhaPlanilha = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetDados = minhaPlanilha.add_worksheet("Dados")

sheetDados.write("A1", "numero 1")
sheetDados.write("B1", "numero 2")
sheetDados.write("C1", "formula")

sheetDados.write("A2", 10)
sheetDados.write("A3", 6)
sheetDados.write("A4", 8)
sheetDados.write("A5", 6)
sheetDados.write("A8", "luan")

sheetDados.write("B2", 7)
sheetDados.write("B3", 5)
sheetDados.write("B4", 3)
sheetDados.write("B5", 1)
sheetDados.write("B8", "Montagnini")

sheetDados.write_formula("C2", "=A2+B2")
sheetDados.write_formula("C3", "=A3-B3")
sheetDados.write_formula("C4", "=A4*B4")
sheetDados.write_formula("C5", "=A5/B5")
sheetDados.write_formula("C8", '=CONCATENATE(A8," ",B8)')

sheetDados.set_column('A:C', 15)

minhaPlanilha.close()

os.startfile(nomeCaminhoArquivo)