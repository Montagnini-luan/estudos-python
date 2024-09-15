"""
Exercício:

Adivinhe o Número Secreto

Você foi desafiado a adivinhar um número secreto entre 1 e 10!

    Execute o programa.
    Insira um número inteiro entre 1 e 10 quando solicitado.
    O programa irá informar se você adivinhou corretamente o número secreto ou não.

Seu objetivo é descobrir qual é o número secreto. Você pode executar o programa 
quantas vezes quiser até adivinhar corretamente.

Nota: Para fins deste exercício, o número secreto é fixo e é igual a 7. Em uma 
versão mais avançada do exercício, você poderia modificar o programa para escolher um número 
secreto aleatório cada vez que é executado.
"""

numero_secreto = 7

numero_digitado = int((input("Adivinhe o número secreto entre 1 e 10: ")))

if numero_digitado == numero_secreto:
    print("Você acertou! Parabéns")

else:
    print("Você errou, tente novamente!")