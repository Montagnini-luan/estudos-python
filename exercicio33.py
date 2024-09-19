"""
Exercício: Gerenciando Vendas de Produtos

Contexto: Você é um gerente de vendas em uma loja de eletrônicos. Cada 
produto vendido é registrado em uma tupla que contém o nome do produto, seu 
preço fixo e uma lista das vendas realizadas durante o mês (quantidades vendidas a cada dia).

Objetivo: Entenda a imutabilidade das tuplas enquanto gerencia o registro de vendas 
diárias de um produto específico.

Instruções:

    1. Registro de Produto:
    
        Crie uma tupla chamada produto com as seguintes 
        
        informações: "Smartphone", 1000.00 (preço em dólares), 
        [2, 3, 4] (vendas nos três primeiros dias do mês).

    2. Tentativa de Alteração de Imutabilidade:
        Tente alterar o preço do "Smartphone" para 1100.00.
        Observe o erro gerado e explique por que ele ocorre.

    3. Atualização de Vendas:
        Um novo lote de "Smartphone" foi vendido e você vendeu mais 
        5 unidades no quarto dia. Adicione esse número à lista de vendas.
        
        Exiba a lista de vendas atualizada para o "Smartphone".

Questões:

a) Ao tentar alterar o preço do "Smartphone", qual erro você encontrou?

b) Qual é o registro de vendas atualizado após adicionar as vendas do quarto dia?

Este exercício visa ensinar sobre a imutabilidade das tuplas em 
um contexto prático de vendas. Ao tentar modificar o preço, enfrentarão um 
erro e, assim, compreenderá a natureza imutável das tuplas. No entanto, ao atualizar 
o registro de vendas, que é uma lista mutável dentro da tupla, aprenderá sobre a 
capacidade de modificar elementos mutáveis mesmo dentro de estruturas imutáveis.
"""

produto = ("Smartphone", 1000.00, [2, 3, 4])

produto[2].append("5")

print(produto[2])