import pyautogui
import pyautogui as escolha_opcao

opcao = pyautogui.confirm('Clique no botão desejado', buttons = ['Excel', 'Word', "Notepad"])

if opcao == "Excel":
    
    #O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
    #Nesse caso é a mesma coisa que precionar Windows + R
    escolha_opcao.hotkey('win', 'r')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(1)
    
    #Digitamos a palavra Excel
    escolha_opcao.typewrite('Excel')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(1)
    
    #Precionamos a tecla Enter
    escolha_opcao.press('Enter')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)
    
    #CLiquei na opção para abrir um excel em branco
    escolha_opcao.click(x=600, y=241)
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)
    
    escolha_opcao.typewrite('Escolhi abrir o Excel')
    
    #print(escolha_opcao.position())
    
    
elif opcao == "Word":
    
    #O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
    #Nesse caso é a mesma coisa que precionar Windows + R
    escolha_opcao.hotkey('win', 'r')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(1)
    
    #Digitamos a palavra Excel
    escolha_opcao.typewrite('winword')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(1)
    
    #Precionamos a tecla Enter
    escolha_opcao.press('Enter')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)
    
    #CLiquei na opção para abrir um excel em branco
    escolha_opcao.click(x=447, y=334)
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)
    
    escolha_opcao.typewrite('Escolhi abrir o Word')
    
    #print(escolha_opcao.position())
    
elif opcao == "Notepad":
    
    #O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
    #Nesse caso é a mesma coisa que precionar Windows + R
    escolha_opcao.hotkey('win', 'r')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(1)
    
    #Digitamos a palavra Excel
    escolha_opcao.typewrite('Notepad')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(1)
    
    #Precionamos a tecla Enter
    escolha_opcao.press('Enter')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)
    
    escolha_opcao.typewrite('Escolhi abrir o notepad')
    
    #print(escolha_opcao.position())
