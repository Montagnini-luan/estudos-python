
arquivo_carolina = open('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\ProfessoraCarolina.txt', 'w')
arquivo_rosiane = open('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\ProfessoraRosiane.txt', 'w')
arquivo = open('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\Alunos.txt', 'r')

linhas = arquivo.readlines()

nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
faltas = 0

for linha in linhas:
    
    quebra_linha = linha.split(',')

    linha = [item.split(';', 1)[1] for item in quebra_linha]

    separa_linha = linha[0].split(';')

    professora = separa_linha[0]

    if professora == "Carolina":

        print("Professora: ", professora)

        nome = separa_linha[2]

        print(nome)

        if separa_linha[3] == "Nota 1":
            pass

        else:
            nota1 = int(separa_linha[3])
            nota2 = int(separa_linha[4])
            nota3 = int(separa_linha[5])
            nota4 = int(separa_linha[6])
            faltas = int(separa_linha[7])

            print("Nota 1: ", nota1)
            print("Nota 2: ", nota2)
            print("Nota 3: ", nota3)
            print("Nota 4: ", nota4)
            print("Faltas: ", faltas)

            media = (nota1 + nota2 + nota3 + nota4) / 4

            print("Media:", media)

            if faltas >= 4:

                print("reprovado(a) por falta")

                arquivo_carolina.write(nome + ', Media: ' + str(media) + ', Faltas: ' + str(faltas) + ' - reprovado(a) por falta\n')

            else:

                if media >= 6:

                    print("Aprovado")

                    arquivo_carolina.write(nome + ', Media: ' + str(media) + ', Faltas: ' + str(faltas) + ' - Aprovado(a)\n')


                elif media >= 4:

                    print("Recuperacao")

                    arquivo_carolina.write(nome + ', Media: ' + str(media) + ', Faltas: ' + str(faltas) + ' - Recuperacao\n')


                else:

                    print("reprovado(a) por media")

                    arquivo_carolina.write(nome + ', Media: ' + str(media) + ', Faltas: ' + str(faltas) + ' - reprovado(a) por media\n')

            print('----------------------------------------')

    elif professora == "Rosiane":

        print("Professora: ", professora)

        nome = separa_linha[2]

        print(nome)

        if separa_linha[3] == "Nota 1":
            pass

        else:
            nota1 = int(separa_linha[3])
            nota2 = int(separa_linha[4])
            nota3 = int(separa_linha[5])
            nota4 = int(separa_linha[6])
            faltas = int(separa_linha[7])

            print("Nota 1: ", nota1)
            print("Nota 2: ", nota2)
            print("Nota 3: ", nota3)
            print("Nota 4: ", nota4)
            print("Faltas: ", faltas)

            media = (nota1 + nota2 + nota3 + nota4) / 4

            print("Media:", media)

            if faltas >= 4:

                print("reprovado(a) por falta")

                arquivo_rosiane.write(nome + ', Media: ' + str(media) + ', Faltas: ' + str(faltas) + ' - reprovado(a) por falta\n')

            else:

                if media >= 6:

                    print("Aprovado")

                    arquivo_rosiane.write(nome + ', Media: ' + str(media) + ', Faltas: ' + str(faltas) + ' - Aprovado(a)\n')


                elif media >= 4:

                    print("Recuperacao")

                    arquivo_rosiane.write(nome + ', Media: ' + str(media) + ', Faltas: ' + str(faltas) + ' - Recuperacao\n')


                else:

                    print("reprovado(a) por media")

                    arquivo_rosiane.write(nome + ', Media: ' + str(media) + ', Faltas: ' + str(faltas) + ' - reprovado(a) por media\n')

            print('----------------------------------------')