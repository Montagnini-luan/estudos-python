"""
Exercício: Análise de Avaliações de Filmes

Contexto: Você é um analista em uma plataforma de streaming e recebeu 
uma lista de avaliações de um filme recém-lançado. As avaliações são dadas como 
estrelas, variando de 1 a 5. Você deve analisar essas avaliações para fornecer 
insights sobre a recepção do filme.

Dados fornecidos: avaliacoes = (5, 4, 4, 3, 5, 2, 4, 3, 5, 5, 1, 4, 3, 5, 2)

Objetivo: Use os métodos de tupla para responder às seguintes perguntas:

    Quantidade de Avaliações de 5 estrelas:
        Quantas vezes o filme foi avaliado com 5 estrelas?
    Primeira Avaliação de 1 estrela:
        Em que posição da sequência aparece a primeira avaliação de 1 estrela?

Instruções:

a) Utilize o método count() para determinar o número de avaliações 
de 5 estrelas na tupla avaliacoes.

b) Utilize o método index() para encontrar a posição da primeira 
avaliação de 1 estrela na tupla avaliacoes.

Questões:

a) Quantas avaliações de 5 estrelas o filme recebeu?

b) Qual é a posição da primeira avaliação de 1 estrela?

Este exercício tem como objetivo familiarizar com os métodos count() 
e index() de tuplas, aplicando-os em um contexto prático de análise de 
dados. 

Ao final, você deve ser capazes de utilizar esses métodos para 
extrair informações relevantes de uma tupla.
"""

avaliacoes = (5, 4, 4, 3, 5, 2, 4, 3, 5, 5, 1, 4, 3, 5, 2)

avaliacoes5estrelas = avaliacoes.count(5)
print(avaliacoes5estrelas)

posicao1estrela = avaliacoes.index(1) + 1
print(posicao1estrela)