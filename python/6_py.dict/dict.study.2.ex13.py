"""
Exercício 12 ⭐⭐⭐⭐

Remova todos que tenham idade menor que 30.
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


for pessoa in pessoas[:]:
    if pessoa["idade"] < 30:
        pessoas.remove(pessoa)
    else:
        print(pessoa)
    


