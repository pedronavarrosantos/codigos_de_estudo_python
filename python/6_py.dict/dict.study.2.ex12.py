"""
Exercício 11 ⭐⭐⭐⭐

Peça um nome.

Remova-o caso exista.
"""
pessoas = [
    {"nome": "Pedro", "idade": 27},
    {"nome": "Stephanie", "idade": 27},
    {"nome": "Matheus", "idade": 28},
    {"nome": "Vitor", "idade": 66},
    {"nome": "Jean", "idade": 34},
    {"nome": "Carlos", "idade": 17},
    {"nome": "Maria", "idade": 14}
]

nom = input("Digite um nome:\n")
found = False

for pessoa in pessoas:
    if pessoa["nome"] == nom:
        pessoas.remove(pessoa)
        print(pessoas)
        found = True
        break
if not found:
    print("Usuário não encontrado.")