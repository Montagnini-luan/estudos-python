
from selenium import webdriver as opcoes_selenium
from selenium.webdriver.common.keys import Keys

import pyautogui as tempoPausaComputador

from selenium.webdriver.common.by import By

meuNavegador = opcoes_selenium.Chrome()
meuNavegador.get("https://www.google.com.br/")

tempoPausaComputador.sleep(2)

meuNavegador.find_element(By.NAME, "q").send_keys("Dolar hoje")

tempoPausaComputador.sleep(2)

meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

tempoPausaComputador.sleep(2)

valorDolarPeloGoogle = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

tempoPausaComputador.sleep(2)

print(valorDolarPeloGoogle)

tempoPausaComputador.sleep(1)

meuNavegador.find_element(By.NAME, "q").send_keys("")

tempoPausaComputador.sleep(1)

tempoPausaComputador.press('tab')

tempoPausaComputador.press('enter')

meuNavegador.find_element(By.NAME, "q").send_keys("Euro hoje")

tempoPausaComputador.sleep(2)

valorEuroPeloGoogle = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

print(valorEuroPeloGoogle)