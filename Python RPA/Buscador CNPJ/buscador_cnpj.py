import http.client
import json
import pandas as pd

def limpar_cnpj(cnpj):
    return ''.join(filter(str.isdigit, cnpj))

def obter_dados_cnpj(cnpj):

    cnpj = limpar_cnpj(cnpj)

    conexao = http.client.HTTPSConnection("www.receitaws.com.br")

    conexao.request("GET", f"/v1/cnpj/{cnpj}")

    resposta = conexao.getresponse()

    print(f"Status da resposta HTTP: {resposta.status}")

    if resposta.status != 200:
        return {"status": "ERROR", "message": f"resposta HTTp com status {resposta.status}"}

    dados = resposta.read()

    conexao.close()

    try:

        empresa = json.loads(dados.decode("utf-8"))

        print(f"Empresa decodificada: {empresa}")

        return empresa
    
    except json.JSONDecodeError as e:

        print(f"Erro na decodificacao do JSON: {str(e)}")

def formatar_dados(empresa):
    
    campos_interesse = ['cnpj', 'nome', 'telefone', 'email', 'logradouro', 'bairro', 'municipio', 'uf', 'cep', 'atividade_principal']
    
    dados_formatados = {campo: empresa.get(campo, '') for campo in campos_interesse}
    
    if 'atividade_principal' in empresa and empresa['atividade_principal']:
        dados_formatados['atividade_principal'] = empresa['atividade_principal'][0].get('text', '')
    
    return dados_formatados

def salvar_dados_empresa_excel(resultados, nome_arquivo, nome_aba="Dados"): 

    with pd.ExcelWriter(nome_arquivo, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        
        try:

            worksheet = writer.book[nome_aba]

            start_row = worksheet.max_row
            
            resultados.to_excel(writer, sheet_name=nome_aba, index=False, header=False, startrow=start_row)
            
        except KeyError:

            resultados.to_excel(writer, sheet_name=nome_aba, index=False, header=True)
            
caminho_planilha = "C:\\Users\\luanm\\OneDrive\\Desktop\\Sites\\Estudos\\estudos python\\Python RPA\\Buscador CNPJ\\CNPJ.xlsx"

planilha_cnpjs = pd.read_excel(caminho_planilha, sheet_name='CNPJ', dtype={'CNPJ': str})

resultados = []

for cnpj in planilha_cnpjs['CNPJ'].dropna():
    
    print(f"Lendo CNPJ: {cnpj}")
    

    dados_empresa = obter_dados_cnpj(str(cnpj))
    

    if dados_empresa:
        

        dados_formatados = formatar_dados(dados_empresa)
        

        resultados.append(dados_formatados)

if resultados:
    
    resultados_df = pd.DataFrame(resultados)
    
    salvar_dados_empresa_excel(resultados_df, caminho_planilha)

print("Dados das empresas foram salvos na planilha na aba 'Dados'.")