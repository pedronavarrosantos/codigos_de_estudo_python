"""
Exercício 8 — Estoque

Crie uma classe Produto com:

nome
preco
quantidade

Crie três produtos.

Exemplo:

Arroz → R$ 25 → 10 unidades
Feijão → R$ 8 → 20 unidades
Macarrão → R$ 6 → 15 unidades

Depois calcule o valor total em estoque de cada produto:

preço x quantidade

Por exemplo:

Arroz:
25 x 10 = R$ 250

Você deve acessar os atributos através dos objetos.
"""
class Produto:

    def __init__(self,nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade



prod1 = Produto("Arroz", 25, 10)
prod2 = Produto("Feijão", 8, 20)
prod3 = Produto("Macarrão", 6, 15)


produtos = [prod1, prod2, prod3]

vTotal = 0
for i in produtos:
    produtoVTotal = i.preco * i.quantidade

    vTotal += produtoVTotal

    print(f"O valor total do produto {i.nome} é {produtoVTotal}.")

print(f"O Valor total do estoque é R$: {vTotal}.")