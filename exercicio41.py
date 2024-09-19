filme = {
    "titulo": "Inception",
    "diretor": "Christopher Nolan",
    "ano": 2010,
    "genero": "Ficção Científica"
}

print(list(filme.keys()))
print(list(filme.values()))
print(list(filme.items()))


copiaFilme = filme.copy()
print(copiaFilme)
copiaFilme.clear()
print(copiaFilme)


elenco = filme.setdefault('elenco', ['Leonardo DiCaprio', 'Ellen Page'])
print(elenco)

print(filme)

atualizacoes = {
    "duracao": 148,
    "idioma" :"Inglês"
}

filme.update(atualizacoes)
print(filme)

chaves = ["nome", "idade", "ocupacao"]

novo_filme = dict.fromkeys(chaves, "Desconhecido")
print(novo_filme)