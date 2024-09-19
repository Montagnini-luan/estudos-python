"""
Exercício sobre Acessando Itens do Dicionário

Objetivo: Dado um dicionário que representa informações sobre um artista 
musical, sua tarefa é acessar certas informações usando diferentes métodos.

Dicionário fornecido:

artista = {
    "nome": "Ludwig van Beethoven",
    "nascimento": 1770,
    "falecimento": 1827,
    "nacionalidade": "Alemã",
    "estilo": "Clássico"
}

Instruções:

    1. Acessando valores usando chaves:
        - Imprima o nome do artista diretamente usando a chave apropriada.
        - Tente acessar a "profissão" do artista diretamente usando a 
        chave (cuidado, essa chave não existe no dicionário!).

    2. Método get():
        - Use o método get() para obter a "nacionalidade" do artista.
        - Use o método get() para tentar acessar a "profissão" do 
        artista. Se a chave não existir, deve retornar "Informação não disponível".

    3. Verificando a existência de uma chave:
        - Verifique se o "estilo" musical do artista está presente 
        no dicionário. Se estiver, imprima-o.
        - Verifique se "instrumento principal" está presente no 
        dicionário. Se não estiver, imprima "Instrumento principal não especificado".
        
"""

artista = {
    "nome": "Ludwig van Beethoven",
    "nascimento": 1770,
    "falecimento": 1827,
    "nacionalidade": "Alemã",
    "estilo": "Clássico"
}

print(artista["nome"])

print(artista.get("nacionalidade"))

print(artista.get("profissão", "dado não informado"))

if "estilo" in artista:
    print(artista["estilo"])
else:
    print("")

if "instrumento principal" in artista:
    print(artista["instrumento principal"])
else:
    print("Instrumento principal não especificado")