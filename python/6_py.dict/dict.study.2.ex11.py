"""
Exercício 7 ⭐⭐⭐

Troque:

Pedro

por

Pedrinho
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

for pessoa in pessoas:
    if pessoa["nome"] == "Pedro":
        pessoa.update({
            "nome": "Pedrinho"
        })
        print(pessoa)

"""
Exercício 8 ⭐⭐⭐

Aumente a idade de todos em 1 ano.
"""

for pessoa in pessoas:
    pessoa["idade"] += 1

print(pessoas)

"""
Exercício 9 ⭐⭐⭐⭐

Troque apenas a idade de Carlos para 40.
"""

for pessoa in pessoas:
    if pessoa["nome"] == "Carlos":
        pessoa.update({
            "idade": 40
        })
        print(pessoa)

"""
Exercício 10 ⭐⭐⭐

Remova Maria.
"""

for pessoa in pessoas:
    if pessoa["nome"] == "Maria":
        pessoas.remove(pessoa)

print(pessoas)

