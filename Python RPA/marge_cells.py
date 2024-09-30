import xlsxwriter as opcoesDoXlsxWriter
import os

nomeCaminhoArquivo = 'C:\\Users\luanm\OneDrive\Desktop\Sites\Estudos\estudos python\Python RPA\MergeCells.xlsx'
workbook = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetPadrao = workbook.add_worksheet()

add_merge_celulas = workbook.add_format({
        'bold': True,
        'border': 6,
        'align': 'center',
        'valign': 'vcenter',
        'size': 30,
        'fg_color': 'blue',
        'font_color': 'white'
})

sheetPadrao.merge_range('B3:I5', 'Aula Merge Cells', add_merge_celulas)

workbook.close()

os.startfile(nomeCaminhoArquivo)