"""
Exercício 2 — Produto

Crie uma classe Produto.

Ela deve receber:

nome
preco

Crie dois produtos diferentes.

Exemplo:

Produto: RTX 5090
Preço: R$ 19999.99

Produto: RAM DDR5
Preço: R$ 1799.90

Depois imprima os atributos de cada objeto.
"""
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto1 = Produto("RTX 5090", 19999.99)
produto2 = Produto("RAM DDR5", 1799.90)

print(f"Produto: {produto1.nome}\nPreço: {produto1.preco}\n")
print(f"Produto: {produto2.nome}\nPreço: {produto2.preco}")