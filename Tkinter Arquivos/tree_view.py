from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from openpyxl import load_workbook
import os

janela = Tk()

janela.geometry("950x350")

janela.title("TreeView")

id = Label(text="ID", font="Arial 12")
id.grid(row=1, column=0, stick="W")
campoDigitavelID = Entry(font="Arial 12")
campoDigitavelID.grid(row=1, column=1, stick="W")

nome = Label(text="Nome", font="Arial 12")
nome.grid(row=1, column=2, stick="W")
campoDigitavelnome = Entry(font="Arial 12")
campoDigitavelnome.grid(row=1, column=3, stick="W")

idade = Label(text="Idade", font="Arial 12")
idade.grid(row=1, column=4, stick="W")
campoDigitavelidade = Entry(font="Arial 12")
campoDigitavelidade.grid(row=1, column=5, stick="W")

sexo = Label(text="Sexo", font="Arial 12")
sexo.grid(row=1, column=6, stick="W")
campoDigitavelsexo = Entry(font="Arial 12")
campoDigitavelsexo.grid(row=1, column=7, stick="W")

def addItemTreeview():

    if str(campoDigitavelID.get()) == "":
        messagebox.showerror("Erro", "Digite algo no campo ID")
        
    elif str(campoDigitavelnome.get()) == "":
        messagebox.showerror("Erro", "Digite algo no campo Nome")
        
    elif str(campoDigitavelidade.get()) == "":
        messagebox.showerror("Erro", "Digite algo no campo Idade")
        
    elif str(campoDigitavelsexo.get()) == "":
        messagebox.showerror("Erro", "Digite algo no campo Sexo")

    else:
        treeViewDados.insert("", "end",
                            values=(str(campoDigitavelID.get()),
                                    str(campoDigitavelnome.get()),
                                    str(campoDigitavelidade.get()),
                                    str(campoDigitavelsexo.get())))
        campoDigitavelnome.delete(0, "end")
        campoDigitavelidade.delete(0, "end")
        campoDigitavelsexo.delete(0, "end")
        campoDigitavelID.delete(0, "end")

    contarNumeroLinhas()

botaoAdicionar = Button(text="Cadastrar",
                        font="Arial 20",
                        command= addItemTreeview)

botaoAdicionar.grid(row=2, column=0, columnspan=2, sticky="NSEW")

estiloDaTreeview = ttk.Style() 
estiloDaTreeview.theme_use('alt')
estiloDaTreeview.configure(".", font = "Arial 14")

treeViewDados = ttk.Treeview(janela, columns=(1,2,3,4), show="headings")

treeViewDados.column("1", anchor=CENTER)
treeViewDados.heading("1", text= "ID")

treeViewDados.column("2", anchor=CENTER)
treeViewDados.heading("2", text= "Nome")

treeViewDados.column("3", anchor=CENTER)
treeViewDados.heading("3", text= "Idade")

treeViewDados.column("4", anchor=CENTER)
treeViewDados.heading("4", text= "Sexo")

treeViewDados.insert("", "end", text="1", values=("1", "Luan", 25, "Masculino"))
treeViewDados.insert("", "end", text="1", values=("2", "Bruna", 24, "Feminino"))
treeViewDados.insert("", "end", text="1", values=("3", "Leonardo", 26, "Masculino"))

treeViewDados.grid(row=3, column=0, columnspan=8, sticky="NSEW")

labelNumeroLinhas = Label(text="Linhas: ", font="Arial 20")
labelNumeroLinhas.grid(row=4, column=0, columnspan=8, sticky="W")

def contarNumeroLinhas(item=""):
    numeroDeLinhas = 0
    linhas = treeViewDados.get_children(item)
    for linha in linhas:
        numeroDeLinhas += 1
    
    labelNumeroLinhas.config(text="Linhas:" + str(numeroDeLinhas))

contarNumeroLinhas()

def deletarItemTreeView():
    itemSelecionado = treeViewDados.selection()
    for item in itemSelecionado:
        treeViewDados.delete(item)
    
    contarNumeroLinhas()

botaoDeletar = Button(text="Deletar",
                        font="Arial 20",
                        command= deletarItemTreeView)

botaoDeletar.grid(row=2, column=2, columnspan=2, sticky="NSEW")

def alterarItemTreeView():
    if str(campoDigitavelID.get()) == "":
        messagebox.showerror("Erro", "Digite algo no campo ID")
        
    elif str(campoDigitavelnome.get()) == "":
        messagebox.showerror("Erro", "Digite algo no campo Nome")
        
    elif str(campoDigitavelidade.get()) == "":
        messagebox.showerror("Erro", "Digite algo no campo Idade")
        
    elif str(campoDigitavelsexo.get()) == "":
        messagebox.showerror("Erro", "Digite algo no campo Sexo")

    else:
        itemSelecionado = treeViewDados.selection()[0]
        treeViewDados.item(itemSelecionado,
                            values=(str(campoDigitavelID.get()),
                                    str(campoDigitavelnome.get()),
                                    str(campoDigitavelidade.get()),
                                    str(campoDigitavelsexo.get())))
        campoDigitavelnome.delete(0, "end")
        campoDigitavelidade.delete(0, "end")
        campoDigitavelsexo.delete(0, "end")
        campoDigitavelID.delete(0, "end")


botaoAlterar = Button(text="Alterar",
                        font="Arial 20",
                        command= alterarItemTreeView)

botaoAlterar.grid(row=2, column= 4, columnspan=2, sticky="NSEW")

def exportarParaExcel():
    workbook = load_workbook(filename="C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\Tratamento_dados.xlsx")
    sheet=workbook["Vendedores"]
    
    for numeroLinhas in treeViewDados.get_children():
        linha = treeViewDados.item(numeroLinhas)['values']
        sheet.append(linha)

    workbook.save(filename="C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\Dados_Exportados.xlsx")
    messagebox.showinfo("Informação", "Dados exportados com sucesso!")
    os.startfile("C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Tkinter Arquivos\\Dados_Exportados.xlsx")

botaoExportar = Button(text="Exportar",
                        font="Arial 20",
                        command= exportarParaExcel)

botaoExportar.grid(row=2, column= 6, columnspan=2, sticky="NSEW")

janela.mainloop()
