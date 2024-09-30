from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

nomeCaminhoArquivo = "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\DadosFormulario.xlsx"

planilha_aberta = load_workbook(filename=nomeCaminhoArquivo)

sheet_selecionada = planilha_aberta['Dados']

for linha in range(2, len(sheet_selecionada['A']) + 1):

    nome = sheet_selecionada[f'A{linha}'].value
    email = sheet_selecionada[f'A{linha}'].value
    telefone = sheet_selecionada[f'A{linha}'].value
    sexo = sheet_selecionada[f'A{linha}'].value
    escreva = sheet_selecionada[f'A{linha}'].value

    navegadorFormulario = opcoesSelenium.Chrome()

    navegadorFormulario.get("https://pt.surveymonkey.com/r/WLXYDX2")

    espera = WebDriverWait(navegadorFormulario, 10)

    campo_nome = espera.until(EC.presence_of_element_located((By.NAME, "166517069")))
    campo_nome.send_keys(nome)

    campo_email = espera.until(EC.presence_of_element_located((By.NAME, "166517072")))
    campo_email.send_keys(email)

    campo_telefone = espera.until(EC.presence_of_element_located((By.NAME, "166517070")))
    campo_telefone.send_keys(telefone)

    campo_escreva = espera.until(EC.presence_of_element_located((By.NAME, "166517073")))
    campo_escreva.send_keys(escreva)

    if sexo == "Feminino":
        botao_feminino = espera.until(EC.element_to_be_clickable((By.ID, "166517071_1215509813_label")))
        botao_feminino.click()
    else:
        botao_masculino = espera.until(EC.element_to_be_clickable((By.ID, "166517071_1215509812_label")))
        botao_masculino.click()

    botao_enviar = espera.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button')))

    botao_enviar.click()

print("Pronto!")