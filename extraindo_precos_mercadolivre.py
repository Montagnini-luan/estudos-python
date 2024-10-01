from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
from openpyxl import load_workbook
import os

nome_arquivo_tabela = "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\Mercado Livre.xlsx"
planilha_dados_tabela = load_workbook(nome_arquivo_tabela)

sheet_selecionada = planilha_dados_tabela['Dados']

navegador = opcoesSelenium.Chrome()
navegador.get("https://www.mercadolivre.com.br/")

navegador.find_element(By.NAME, 'as_word').send_keys("carteira")

tempoEspera.sleep(2)

navegador.find_element(By.XPATH, '/html/body/header/div/div[2]/form/button').click()

tempoEspera.sleep(4)

dados_produto = navegador.find_elements(By.CLASS_NAME, 'ui-search-layout__item')

linha = 2
for informacoes in dados_produto:

    sheet_dados = planilha_dados_tabela['Dados']

    nome_produto = informacoes.find_element(By.CLASS_NAME, 'ui-search-item__brand-discoverability').text
    preco_produto = informacoes.find_element(By.CLASS_NAME, 'andes-money-amount__fraction').text
    try:
        centavos_produto = informacoes.find_element(By.CLASS_NAME, 'andes-money-amount__cents').text
    except:
        centavos_produto = "0"
    url_produto = informacoes.find_element(By.TAG_NAME, 'a').get_attribute("href")

    #print(nome_produto + " - " + preco_produto + "," + centavos_produto + " - " + url_produto)
    linha = len(sheet_dados['A']) + 1

    colunaA = "A" + str(linha)
    colunaB = "B" + str(linha)
    colunaC = "C" + str(linha)
    
    sheet_dados['A1'] = 'Produto'
    sheet_dados['B1'] = 'Preco'
    sheet_dados['C1'] = 'Url'

    preco_texto = preco_produto + "," + centavos_produto

    preco_sem_ponto = preco_texto.replace('.', '')
    preco_sem_ponto2 = preco_sem_ponto.replace(',', '.')

    preco_sem_ponto2 = float(preco_sem_ponto2)

    sheet_dados[colunaA] = nome_produto
    sheet_dados[colunaB] = preco_sem_ponto2
    sheet_dados[colunaC] = url_produto

planilha_dados_tabela.save(filename=nome_arquivo_tabela)

os.startfile(nome_arquivo_tabela)