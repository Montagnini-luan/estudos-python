from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import pyautogui as tempoEspera
import pyautogui as teclasTeclado
from selenium.webdriver.common.by import By
from openpyxl import load_workbook


nome_arquivo_contato = "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\Disparando msg pelo whatsweb\\Contatos.xlsx"

planilha_dados_contatos = load_workbook(nome_arquivo_contato)

sheet_selecionada = planilha_dados_contatos['Dados']

path_to_driver = 'C:\\edgedriver_win64\\msedgedriver.exe'

service = Service(executable_path=path_to_driver)

driver = webdriver.Edge(service=service)

driver.get("https://web.whatsapp.com/")

while len(driver.find_elements(By.ID, 'side')) < 1:
    tempoEspera.sleep(3)

tempoEspera.sleep(3)

for linha in range(2 , len(sheet_selecionada['A']) + 1):

    nome_contato = sheet_selecionada['A%s' % linha].value
    mensagem_contato = sheet_selecionada['B%s' % linha].value

    tempoEspera.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys(nome_contato)
    tempoEspera.sleep(3)

    teclasTeclado.press('enter')

    tempoEspera.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p').send_keys(mensagem_contato)

    tempoEspera.sleep(3)

    teclasTeclado.press('enter')

    tempoEspera.sleep(3)


driver.quit()