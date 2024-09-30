import xlsxwriter as opcoesDoXlsxWriter
import os

nomeCaminhoArquivo = 'C:\\Users\luanm\OneDrive\Desktop\Sites\Estudos\estudos python\Python RPA\Grafico.xlsx'
planilhaExcel = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetDados = planilhaExcel.add_worksheet("Resumo")

linhaNegrito = planilhaExcel.add_format({'bold': 1})

titulos = ['Vendedores', 'Total Vendas']
dadosTabela = [
    ["Deni", "Jorge", "Nicolas", "Ogamar"],
    [400, 300, 89, 350]
]

sheetDados.write_row('A1', titulos, linhaNegrito)
sheetDados.write_column('A2', dadosTabela[0])
sheetDados.write_column('B2', dadosTabela[1])

graficoColunas = planilhaExcel.add_chart({'type': 'column'})

graficoColunas.add_series({
    'name': '=Resumo!$B$1',
    'categories': '=Resumo!$A$2:$A$5',
    'values': '=Resumo!$B$2:$B$5',
})

graficoColunas.set_title({'name': 'Gráfico total de vendas' })
graficoColunas.set_x_axis({'name': 'Vendedores' })
graficoColunas.set_y_axis({'name': 'Vendas' })


graficoColunas.set_style(11)

sheetDados.insert_chart('D2', graficoColunas, {'x_offset': 25, 'y_offset': 10})

graficoEmpilhado = planilhaExcel.add_chart({'type': 'area', 'subtype': 'stacked'})

graficoEmpilhado.add_series({
    'name': '=Resumo!$B$1',
    'categories': '=Resumo!$A$2:$A$5',
    'values': '=Resumo!$B$2:$B$5',
})

graficoEmpilhado.set_title({'name': 'Gráfico Empilhado' })
graficoEmpilhado.set_x_axis({'name': 'Funcionários' })
graficoEmpilhado.set_y_axis({'name': 'Vendas' })

graficoEmpilhado.set_style(12)

sheetDados.insert_chart('L2', graficoEmpilhado, {'x_offset': 25, 'y_offset': 10})

planilhaExcel.close()

os.startfile(nomeCaminhoArquivo)