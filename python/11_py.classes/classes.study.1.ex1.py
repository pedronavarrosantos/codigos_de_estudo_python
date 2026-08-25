"""
Exercício 1 — Pessoa

Crie uma classe chamada Pessoa.

Ela deve receber no __init__:

nome
idade

Crie uma pessoa:

pessoa1 = Pessoa("Pedro", 27)

Depois imprima:

Nome: Pedro
Idade: 27
"""
class Pessoa:
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

pessoa1 = Pessoa("Pedro", 27)

print(f"Nome: {pessoa1.Nome}")
print(f"Idade: {pessoa1.Idade}")