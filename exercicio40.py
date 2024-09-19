"""
Exercício sobre Operações Básicas com Dicionários

Objetivo: Dado um dicionário que representa informações de 
um aluno, sua tarefa é realizar operações para 
adicionar, atualizar, remover e copiar informações.

Dicionário fornecido:

aluno = {
    "matricula": "A12345",
    "nome": "João Silva",
    "curso": "Engenharia de Computação",
    "semestre": 5,
    "cr": 8.5
}

Instruções:

    1. Adicionando itens:
        - Adicione uma chave "hobbies" com o valor de uma 
        lista contendo: "Leitura", "Corrida", "Xadrez".
        
        - Adicione uma chave "idade" com valor 22.

    2. Atualizando itens:
        - Atualize o valor da chave "semestre" para 6.
        - Atualize o valor da chave "cr" para 8.7.

    3. Removendo itens:
        - Use o método del para remover a chave "idade".
        
        - Use o método pop() para remover a chave "hobbies" 
        e imprima os hobbies removidos.
        
        - Use o método popitem() para remover o último item adicionado 
        ao dicionário e imprima a chave e o valor do item removido.

    4. Copiando dicionários:
        - Crie uma cópia do dicionário aluno chamada copia_1 usando o método copy().
        - Crie outra cópia do dicionário aluno chamada copia_2 usando o método dict().
"""

aluno = {
    "matricula": "A12345",
    "nome": "João Silva",
    "curso": "Engenharia de Computação",
    "semestre": 5,
    "cr": 8.5
}

aluno["hobbies"] = ["Leitura", "Corrida", "Xadrez"]
aluno["idade"] = 22

aluno["semestre"] = 6
aluno["cr"] = 8.7

del aluno["idade"]

itens_removidos = aluno.pop("hobbies")

print(itens_removidos)

ultimo_removido = aluno.popitem()

print(ultimo_removido)

copia1 = aluno.copy()
copia2 = dict(aluno)

print(copia1)
print(copia2)