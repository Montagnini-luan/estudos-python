import xlsxwriter as opcoesDoXlsxWriter
import os

nomeCaminhoArquivo = 'C:\\Users\luanm\OneDrive\Desktop\Sites\Estudos\estudos python\Python RPA\PintaFundoEFonte.xlsx'

minhaPlanilha = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetDados = minhaPlanilha.add_worksheet("Dados")

#corFundo = minhaPlanilha.add_format({'fg_color':'yellow'})

corFonte = minhaPlanilha.add_format()
corFonte.set_font_color('blue')

corFonteFundo = minhaPlanilha.add_format({'align': 'center',
                                          'font_color': 'white',
                                          'bold': True,
                                          'bg_color':'gray',})

sheetDados.write("A1", "Nome", corFonteFundo)
sheetDados.write("B1", "Idade", corFonteFundo)
sheetDados.write("A2", "Luan", corFonte)
sheetDados.write("B2", 25, corFonte)
sheetDados.write("A3", "Bruna", corFonte)
sheetDados.write("B3", 24, corFonte)

minhaPlanilha.close()

os.startfile(nomeCaminhoArquivo)