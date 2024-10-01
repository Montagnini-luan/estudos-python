from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
from openpyxl import load_workbook
import os

nome_arquivo_tabela = "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\Planilha Dados WEB.xlsx"
planila_dados_tabela = load_workbook(nome_arquivo_tabela)

sheet_selecionada = planila_dados_tabela['Dados']

navegador = opcoesSelenium.Chrome()
navegador.get("https://rpachallengeocr.azurewebsites.net/")



linha = 1

i = 1

while i < 4:

    sheet_dados = planila_dados_tabela['Dados']

    elemento_tabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    linhas = elemento_tabela.find_elements(By.TAG_NAME, "tr")
    colunas = elemento_tabela.find_elements(By.TAG_NAME, "td")

    for linha_atual in linhas:

        print(linha_atual.text)
        linha += 1
        linha = len(sheet_dados['A']) + 1

        coluna_a = 'A' + str(linha)
        coluna_b = 'B' + str(linha)
        coluna_c = 'C' + str(linha)

        texto = linha_atual.text
        texto2 = texto.split(" ")

        sheet_dados[coluna_a] = texto2[0]
        sheet_dados[coluna_b] = texto2[1]
        sheet_dados[coluna_c] = texto2[2]
    
    i += 1

    tempoEspera.sleep(1)

    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    tempoEspera.sleep(1)

else:
    print("pronto!")

planila_dados_tabela.save(filename=nome_arquivo_tabela)

os.startfile(nome_arquivo_tabela)