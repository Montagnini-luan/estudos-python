import pandas as pd

arquivoProfessoraCarolina = open('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\ProfessoraCarolina.txt', 'w')
arquivo = open('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\Alunos.txt', 'r')
arquivoBlocoDeNotas = arquivo.readlines()

nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
faltas = 0

arquivoProfessoraCarolina.write('ID;Aluno;Média;Faltas;Situação\n')

for linha in arquivoBlocoDeNotas:
    
    quebraLinha = linha.split(',')
    
    linha = [item.split(';', 1)[1] for item in quebraLinha]
    
    separaLinhaEmColunas = linha[0].split(';')
    
    professora = separaLinhaEmColunas[0]  
    
    if professora == "Carolina":
        
        print("Professora: ", professora)
    
        nome = separaLinhaEmColunas[2]    

        if separaLinhaEmColunas[3] == "Nota 1":

            print("------ Título ---------")

        else:

            print(nome)

            nota1 = int(separaLinhaEmColunas[3])
            nota2 = int(separaLinhaEmColunas[4])
            nota3 = int(separaLinhaEmColunas[5])
            nota4 = int(separaLinhaEmColunas[6])
            faltas = int(separaLinhaEmColunas[7])

            print("Nota 1: ", nota1)
            print("Nota 2: ", nota2)
            print("Nota 3: ", nota3)
            print("Nota 4: ", nota4)
            print("Faltas: ", faltas)

            media = (nota1 + nota2 + nota3 + nota4) / 4

            print("Média: ", media)

            if faltas >= 4:

                print("Reprovado(a) por falta")
                
                arquivoProfessoraCarolina.write(';' + nome + '; Média: ' + str(media) + '; Faltas: ' + str(faltas) + '; Reprovado(a) por falta\n')

            else:

                if media >= 6:

                    print("Aprovado(a)")
                    
                    arquivoProfessoraCarolina.write(';' + nome + '; Média: ' + str(media) + '; Faltas: ' + str(faltas) + '; Aprovado(a)\n')

                elif media >= 4:

                    print("Recuperação")
                    
                    arquivoProfessoraCarolina.write(';' + nome + '; Média: ' + str(media) + '; Faltas: ' + str(faltas) + '; Recuperação\n')

                else:

                    print("Reprovado(a) por Média")
                    
                    arquivoProfessoraCarolina.write(';' + nome + '; Média: ' + str(media) + '; Faltas: ' + str(faltas) + '; Reprovado(a) por Média\n')

            print("-----------------------")

arquivoProfessoraCarolina.close()

configacaoIdioma = 'cp1252'
arquivoDataFrame = pd.read_csv('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\ProfessoraCarolina.txt', encoding=configacaoIdioma)

arquivoDataFrame.to_csv('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\ProfessoraCarolina.csv', encoding='utf-8-sig')

