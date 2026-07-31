"""
Exercício 4 ⭐⭐⭐⭐

Leia o arquivo.

Converta cada linha em um dicionário.

Ao final, imprima:

[
    {"nome": "Pedro", "idade": 27},
    {"nome": "Maria", "idade": 22},
    {"nome": "Carlos", "idade": 31}
]
"""
with open("file2.txt", "r") as doc:
    pessoas = []

    for line in doc:
        nome, idade = line.split(",")
        idade = idade.strip()

        pessoas.append({
            "nome": nome,
            "idade": idade
        })
    for pessoa in pessoas:
        print(pessoa)