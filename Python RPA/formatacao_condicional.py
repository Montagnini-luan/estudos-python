import xlsxwriter as opcoesDoXlsxWriter
import os

nomeCaminhoArquivo = 'C:\\Users\luanm\OneDrive\Desktop\Sites\Estudos\estudos python\Python RPA\Formtacao_condicional.xlsx'
planilhaExcel = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetDados = planilhaExcel.add_worksheet("Dados")

formatoMaior = planilhaExcel.add_format({'bg_color': 'green',
                                        'font_color': 'white'})

formatoMenor = planilhaExcel.add_format({'bg_color': 'red',
                                        'font_color': 'white'})

inserirDados = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
    [34, 50, 12, 34],
    [59, 58, 76, 51],
    [43, 80, 34, 12],
    [91, 58, 73, 19],
]

sheetDados.write('A1', "Células com valores >= 50 estão em verde e < 50 estão em vermelho")

for linha, range in enumerate(inserirDados):
    sheetDados.write_row(linha + 2, 1, range)
    
sheetDados.conditional_format('B4:E7', {'type': 'cell',
                                       'criteria': '>=',
                                       'value': 50,
                                       'format': formatoMaior})

sheetDados.conditional_format('B4:E7', {'type': 'cell',
                                       'criteria': '<',
                                       'value': 50,
                                       'format': formatoMenor})

planilhaExcel.close()

os.startfile(nomeCaminhoArquivo)