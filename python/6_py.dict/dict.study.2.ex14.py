"""
Exercício 13 ⭐⭐⭐⭐

Adicione um novo aluno utilizando:

append()
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
pessoas.append(
    {"nome": "Lineu", "idade": 74}
    )

pessoas.append(
    {"nome": "Romeu", "idade": 44}
    )

pessoas.append(
    {"nome": "Gertrudes", "idade": 93},
    )
    
print(pessoas)