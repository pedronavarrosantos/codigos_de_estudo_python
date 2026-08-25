"""
Exercício 3 — Carro

Crie uma classe Carro com:

marca
modelo
ano

Crie dois carros diferentes.

Depois imprima as informações de cada um.
"""

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro("Citroên", "C4 Cactus", 2022)
carro2 = Carro("Jaecoo", "Jaecoo 7", 2026)

print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano};\n")
print(f"Marca: {carro2.marca}\nModelo: {carro2.modelo}\nAno: {carro2.ano}.")