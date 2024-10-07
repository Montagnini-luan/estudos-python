from tkinter import *
from tkinter import messagebox
import http.client
import json

janela = Tk()

janela.geometry("1200x650")

janela.title('CEP')

instrucao = Label(text='CEP: ', font='Arial 40')
instrucao.grid(row=1, column=0, stick='W')

campo_digitavel_cep = Entry(font='Arial 40')
campo_digitavel_cep.grid(row=1, column=1, stick='W')

def obter_endereco_cep():
    cep = campo_digitavel_cep.get()
    conexao = http.client.HTTPSConnection("viacep.com.br")
    conexao.request("GET", f"/ws/{cep}/json/")
    resposta = conexao.getresponse()
    
    if resposta.status != 200:
        conexao.close()
        messagebox.showerror("Erro", "CEP não encontrado.")
        return
    
    dados = resposta.read()
    endereco = json.loads(dados.decode("utf-8"))

    lblRua.config(text=f"Rua: {endereco.get('logradouro', '-')}")
    lblBairro.config(text=f"Bairro: {endereco.get('bairro', '-')}")
    lblCidade.config(text=f"Cidade: {endereco.get('localidade', '-')}")
    lblCEP.config(text=f"CEP: {endereco.get('cep', '-')}")

    conexao.close()

botao_pesquisar = Button(text='Pesquisar', font='Arial 40', command=obter_endereco_cep)
botao_pesquisar.grid(row=2, column=0, columnspan=2, stick='NSEW')

lblRua = Label(text="\nRua: -", font="Arial 40")
lblRua.grid(row=3, column=0, columnspan=2, stick="NSEW")

lblBairro = Label(text="Bairro: -", font="Arial 40")
lblBairro.grid(row=4, column=0, columnspan=2, stick="NSEW")

lblCidade = Label(text="Cidade: -", font="Arial 40")
lblCidade.grid(row=5, column=0, columnspan=2, stick="NSEW")

lblCEP = Label(text="CEP: -", font="Arial 40")
lblCEP.grid(row=6, column=0, columnspan=2, stick="NSEW")

janela.mainloop()
