import pandas as pd
import pathlib as pt
import win32com.client

from pandas._libs.tslibs import Tick

emails = pd.read_excel(r'E:\\Sites\\Estudos\\estudos python\\Novo Curso\\Projeto1\\Bases de Dados\\Emails.xlsx')
lojas = pd.read_csv(r'E:\\Sites\\Estudos\\estudos python\\Novo Curso\\Projeto1\\Bases de Dados\\Lojas.csv', encoding='latin1', sep=';')
vendas = pd.read_excel(r'E:\\Sites\\Estudos\\estudos python\\Novo Curso\\Projeto1\\Bases de Dados\\Vendas.xlsx')

vendas = vendas.merge(lojas, on='ID Loja')

dicionario_lojas = {}

for loja in lojas['Loja']:
    dicionario_lojas[loja] = vendas.loc[vendas['Loja'] == loja, :]

dia_indicador = vendas['Data'].max()

#Salvar em bakup

#identificar se a pasta ja existe

caminho_backup = pt.Path(r'E:\\Sites\\Estudos\\estudos python\\Novo Curso\\Projeto1\\Backup Arquivos Lojas')
arquivos_pasta_backup = caminho_backup.iterdir()
lista_nomes_beckup = [arquivo.name for arquivo in arquivos_pasta_backup]

for loja in dicionario_lojas:
    if loja not in lista_nomes_beckup:
        nova_pasta = caminho_backup / loja
        nova_pasta.mkdir()

    #salvar dentro da pasta
    nome_arquivo = '{}_{}_{}.xlsx'.format(dia_indicador.month, dia_indicador.day, loja)
    local_arquivo = caminho_backup / loja / nome_arquivo
    
    dicionario_lojas[loja].to_excel(local_arquivo)

#calcular indicadores

#definir meta

meta_faturamento_dia = 1000
meta_faturamento_ano = 1650000
meta_qtde_produtos_dia = 4
meta_qtde_produtos_ano = 120
meta_ticket_medio_dia = 500
meta_ticket_medio_ano = 500

for loja in dicionario_lojas:
    vendas_loja = dicionario_lojas[loja]
    vendas_loja_dia = vendas_loja.loc[vendas_loja['Data'] == dia_indicador, :]

    #faturamento
    faturamento_ano = vendas_loja['Valor Final'].sum()
    #print(faturamento_ano)
    faturamento_dia = vendas_loja_dia['Valor Final'].sum()
    #print(faturamento_dia)

    #deversidade de produtos
    qtde_produtos_ano = len(vendas_loja['Produto'].unique())
    #print(qtde_produtos_dia)

    #ticket médio
    valor_venda = vendas_loja.groupby('Código Venda')
    ticket_medio_ano = valor_venda['Valor Final'].sum().mean()
    #print(ticket_medio_ano)

    valor_venda_dia = vendas_loja_dia.groupby('Código Venda')
    ticket_medio_dia = valor_venda_dia['Valor Final'].sum().mean()
    #print(ticket_medio_dia)

""""
    #enviar email
    outlook = win32com.client.Dispatch("Outlook.Application")

    nome = emails.loc[emails['Loja'] == loja, 'Gerente'].values[0]
    mail = outlook.CreateItem(0)
    mail.To = emails.loc[emails['Loja'] == loja, 'E-mail'].values[0]
    mail.Subject = f'OnePage Dia {dia_indicador.day}/{dia_indicador.month} - Loja {loja}'
    mail.HTMLBody = f'''
    <p>Bom dia, {nome}</p>

    <p>O resultado de ontem <strong>({dia_indicador.day}/{dia_indicador.month})</strong> da <strong>Loja {loja}</strong> foi:</p>

    <table>
        <tr>
            <th>Indicador</th>
            <th>Valor Dia</th>
            <th>Meta Dia</th>
        </tr>
        <tr>
            <td>Faturamento</td>
            <td>R${faturamento_dia:.2f}</td>
            <td>R${meta_faturamento_dia:.2f}</td>
        </tr>
        <tr>
            <td>Diversidade de Produtos</td>
            <td>{qtde_produtos_dia}</td>
            <td>{meta_qtde_produtos_dia}</td>
        </tr>
        <tr>
            <td>Ticket Médio</td>
            <td>R${ticket_medio_dia:.2f}</td>
            <td>R${meta_ticket_medio_dia:.2f}</td>
        </tr>
    </table>
    <br>

    <p>Segue em anexo a planilha com todos os dados para mais detalhes.</p>

    <p>Qualquer dúvida estou a disposição.</p>

    <p>Att.,</p>
    '''

    attachments = pt.Path.cwd() / caminho_backup / loja / f'{dia_indicador.month}_{dia_indicador.day}_{loja}.xlsx'
    mail.Attachments.Add(str(attachments))
    mail.Send()

    print('Email da Loja {} enviado'.format(loja))
"""

faturamento_lojas = vendas.groupby('Loja')[['Loja', 'Valor Final']].sum()
faturamento_lojas = faturamento_lojas.sort_values(by='Valor Final', ascending=False)

print(faturamento_lojas)

vendas_dia = vendas.loc[vendas['Data'] == dia_indicador, :]
faturamento_lojas_dia = vendas_loja_dia.groupby('Loja')[['Loja', 'Valor Final']].sum()
faturamento_lojas_dia = faturamento_lojas_dia.sort_values(by='Valor Final', ascending=False)

print(faturamento_lojas_dia)



