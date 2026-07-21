"""
Exercício 3 ⭐⭐⭐

Crie:

nomes = [
    "Pedro",
    "Maria",
    "Ana",
    "Carlos",
    "João"
]

Peça um nome ao usuário.

Informe:

se ele existe;
qual sua posição.
"""
nomes = [
    "Pedro",
    "Maria",
    "Ana",
    "Carlos",
    "João"
]

nome = input("Digite um nome:\n")

if nome in nomes:
    print(nomes.index(nome))
else:
    print("Nome não encontrado.")