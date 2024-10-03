import requests

# Constante para a URL base da API
BASE_URL = "https://v6.exchangerate-api.com/v6"

def obter_taxa(moeda_origem, moeda_final, api):
    url = f"{BASE_URL}/{api}/latest/{moeda_origem}"
    request = requests.get(url)
    if request.status_code != 200:
        raise Exception(f"Erro ao acessar a API: {request.status_code}")
    dados = request.json()
    if moeda_final not in dados['conversion_rates']:
        raise Exception(f"Moeda {moeda_final} não disponível.")
    return dados['conversion_rates'][moeda_final]

def converter(valor, cambio):
    return valor * cambio

def main():
    api = "49cb862690c1dff00763f857"  #Chave da api
    moeda_origem = input("Digite a moeda de origem (USD, BRL, AED): ").upper()
    moeda_final = input("Digite a moeda destino (USD, BRL, AED): ").upper()
    valor = float(input("Digite o valor a ser convertido: "))

    try:
        cambio = obter_taxa(moeda_origem, moeda_final, api)
        valor_convertido = converter(valor, cambio)
        print(f"{valor} {moeda_origem} é igual a {valor_convertido:.2f} {moeda_final}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()

