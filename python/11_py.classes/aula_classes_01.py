class Produto:
    pass

produto1 = Produto()
produto1.nome = "RTX 5090"
produto1.preco = 19999.99

produto2 = Produto()
produto2.nome = "RAM DDR5 Vengance 16gb"
produto2.preco = 1799.90

print(f"{produto1.nome}, valor: R$:{produto1.preco}")
print(f"{produto2.nome}, valor: R$:{produto2.preco}")