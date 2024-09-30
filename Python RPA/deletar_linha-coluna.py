from openpyxl import load_workbook
import os

caminho_nome_arquivo = 'C:\\Users\luanm\OneDrive\Desktop\Sites\Estudos\estudos python\Python RPA\DeletarLinhaColuna.xlsx'
planilha_aberta = load_workbook(filename=caminho_nome_arquivo)

sheet_selecionada = planilha_aberta['Aluno']

sheet_selecionada.delete_rows(3)
sheet_selecionada.delete_rows(3)
sheet_selecionada.delete_rows(5)

sheet_selecionada.delete_cols(2)

planilha_aberta.save(filename=caminho_nome_arquivo)

os.startfile(caminho_nome_arquivo)