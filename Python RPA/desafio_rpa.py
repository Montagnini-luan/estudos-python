from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import pyautogui as tempoEspera
import pyautogui as teclasTeclado
from selenium.webdriver.common.by import By
from openpyxl import load_workbook

caminho_planilha_dados = 'C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\challenge.xlsx'

planilha_dados = load_workbook(caminho_planilha_dados)

sheet_selecionada = planilha_dados['Sheet1']

caminho_driver = 'C:\\edgedriver_win64\\msedgedriver.exe'

service = Service(caminho_executavel=caminho_driver)

driver = webdriver.Edge(service=service)

driver.get("https://rpachallenge.com/")

tempoEspera.sleep(3)

for linha in range(2, len(sheet_selecionada['A']) + 1):

    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(sheet_selecionada['A%s' % linha].value)

    tempoEspera.sleep(1)

    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(sheet_selecionada['B%s' % linha].value)

    tempoEspera.sleep(1)

    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys(sheet_selecionada['C%s' % linha].value)

    tempoEspera.sleep(1)

    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys(sheet_selecionada['D%s' % linha].value)

    tempoEspera.sleep(1)

    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys(sheet_selecionada['E%s' % linha].value)

    tempoEspera.sleep(1)

    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys(sheet_selecionada['F%s' % linha].value)

    tempoEspera.sleep(1)

    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(sheet_selecionada['G%s' % linha].value)

    tempoEspera.sleep(1)

    driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()

    tempoEspera.sleep(1)

    print("Dados enviados com sucesso!")

driver.quit()
