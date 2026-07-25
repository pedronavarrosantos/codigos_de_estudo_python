"""
Exercício 1 ⭐

Crie:

pessoas = [
    {"nome": "Pedro", "idade": 27},
    {"nome": "Maria", "idade": 22},
    {"nome": "Carlos", "idade": 31}
]

Imprima:

Pedro
Maria
Carlos
"""
pessoas = [
    {"nome": "Pedro", "idade": 27},
    {"nome": "Stephanie", "idade": 27},
    {"nome": "Matheus", "idade": 28},
    {"nome": "Vitor", "idade": 66},
    {"nome": "Jean", "idade": 34},
]

for pessoa in pessoas:
    print(pessoa["nome"])

"""
Exercício 2 ⭐

Utilizando a mesma lista.

Imprima a idade
"""
for pessoa in pessoas:
    print(pessoa["idade"])

"""
Exercício 3 ⭐⭐

Imprima:

Pedro - 27
Maria - 22
Carlos - 31
"""

for pessoa in pessoas:
    print(f"{pessoa["nome"]} - {pessoa["idade"]}")

"""
Bloco 2 — Busca
Exercício 4 ⭐⭐

Peça um nome.

Mostre somente a idade.
"""
nom = input("Digite um nome:\n")
found = False

for pessoa in pessoas:
    if nom == pessoa["nome"]:
        print(pessoa["idade"])
        found = True
        break
if not found:
    print("Nome não encontrado")
