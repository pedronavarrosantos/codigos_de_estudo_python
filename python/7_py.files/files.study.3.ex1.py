"""
Exercícios

Exercício 1 ⭐

Utilize a lista:

pessoas = [
    {"nome": "Pedro", "idade": 27},
    {"nome": "Maria", "idade": 22},
    {"nome": "Carlos", "idade": 31}
]

Grave essas informações em um arquivo chamado pessoas.txt no formato:

Pedro,27
Maria,22
Carlos,31
"""
pessoas = [
    {"nome": "Pedro", "idade": 27},
    {"nome": "Maria", "idade": 22},
    {"nome": "Carlos", "idade": 31}
]

with open("file3.txt", "w") as doc:
    for line in pessoas:
        nome = line["nome"]
        idade = line["idade"]
        

        doc.write(f"{nome},{idade}\n")
with open("file3.txt", "r") as doc:
    print(doc.read())