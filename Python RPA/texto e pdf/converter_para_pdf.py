from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size = 15)

pdf.cell(200, 20, txt = "Escola ABC", ln = 1,
        align = 'C')

pdf.cell(200, 20, txt = "Turma 5 / 2024", ln = 1,
        align = 'C')

pdf.set_font("Arial", size = 12)

arquivo = open('C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\ProfessoraRosiane.txt', 'r')

w = 0

h = 0


for linha in arquivo:

    pdf.cell(w,h = 10, txt = linha, border = 1, ln = 1,
             align = 'L', fill = False, link = 'https://www.google.com/' )
    
#salva o arquvo PDF
pdf.output("C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\texto e pdf\\ProfessoraRosiane.pdf")

print("PDF criado com sucesso!")