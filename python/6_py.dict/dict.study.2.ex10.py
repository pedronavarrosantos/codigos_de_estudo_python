"""
Exercício 6 ⭐⭐⭐

Peça uma idade.

Mostre todos que possuem essa idade.
"""
pessoas = [
    {"nome": "Pedro", "idade": 27},
    {"nome": "Stephanie", "idade": 27},
    {"nome": "Matheus", "idade": 28},
    {"nome": "Vitor", "idade": 66},
    {"nome": "Jean", "idade": 34},
]

age = input("Digite uma idade:\n")

for pessoa in pessoas:
    if age == str(pessoa["idade"]):
        print(f"O(a) tem {pessoa["nome"]} tem {pessoa["idade"]} anos")