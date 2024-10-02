import pandas as pd
import os

arquivoTextoConsolidado = open("C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\Arquivo_Exercicio_Bloco_Notas_Consolidado.txt", "w")

caminhoArquivos = "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\Arquivos_Consolidar"

listaArquivos = os.listdir(caminhoArquivos)

listaCaminhoEArquivoBlocoNotas = [caminhoArquivos + '\\' + arquivo for arquivo in listaArquivos if arquivo[-3:] == 'txt']

dadosArquivo = pd.DataFrame()

arquivoTextoConsolidado.write('Linha;Escola;ID;Aluno;Primeiro Nome;Sobrenome;CPF;Idade\n')

for arquivo in listaCaminhoEArquivoBlocoNotas:
    
    dados = pd.read_csv(arquivo)
    
    for pulaTitulo, linha in dados.iterrows():
        
        linha = [item.split(';', 0)[0] for item in linha]
        
        separaLinhasEmColunas = linha[0].split(';')
        
        escola = separaLinhasEmColunas[0]
        idAluno = separaLinhasEmColunas[1]
        aluno = separaLinhasEmColunas[2]
        cpf = separaLinhasEmColunas[3]
        idade = separaLinhasEmColunas[4]
        
        primeiroNome = aluno.split(' ')[0]
        
        sobrenome = aluno.split(' ')[-1]
        
        cpf_parte1 = cpf[5:8]
        cpf_parte2 = cpf[8:11]
        cpf_parte3 = cpf[11:14]
        cpf_parte4 = cpf[14:16] 
        
        cpf = str(cpf_parte1) + "." + str(cpf_parte2) + "." + str(cpf_parte3) + "-" + str(cpf_parte4)
              
        arquivoTextoConsolidado.write(';' + escola + ';' + idAluno + ';' + aluno + ';' + primeiroNome + ';' + sobrenome + ';' + cpf + ';' + idade + '\n')
        

arquivoTextoConsolidado.close 

idiomaParaAcentosDoArquivo = 'cp1252'

lerArquivoBlocoNotasConsolidado = pd.read_csv("C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\Arquivos_Consolidar\\Arquivo_Exercicio_Bloco_Notas_Consolidado.txt", encoding=idiomaParaAcentosDoArquivo)

lerArquivoBlocoNotasConsolidado.to_csv('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\Arquivos_Consolidar\\Arquivo Final Exercicio Texto.csv', encoding='utf-8-sig')