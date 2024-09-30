from openpyxl import load_workbook
import os

caminho_nome_arquivo = 'C:\\Users\luanm\OneDrive\Desktop\Sites\Estudos\estudos python\Python RPA\Formulas1.xlsx'
planilha_aberta = load_workbook(filename=caminho_nome_arquivo)

sheet_selecionada = planilha_aberta['Aluno']

sheet_selecionada['A6'] = "=SUM(A2:A5)"
sheet_selecionada['B6'] = "=SUM(B2:B5)"
sheet_selecionada['D2'] = "=A2+B2"
sheet_selecionada['D3'] = "=A3-B3"
sheet_selecionada['D4'] = "=A4*B4" 
sheet_selecionada['D5'] = "=A5/B5"

sheet_selecionada['B12'] = "=MID(A12,1,3)"
sheet_selecionada['C12'] = "=MID(A12,5,3)"
sheet_selecionada['D12'] = "=MID(A12,9,3)"
sheet_selecionada['E12'] = "=MID(A12,13,2)"


planilha_aberta.save(filename=caminho_nome_arquivo)

os.startfile(caminho_nome_arquivo)