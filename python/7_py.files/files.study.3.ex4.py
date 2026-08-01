"""
Exercício 4 ⭐⭐⭐⭐

Adicione:

Jean,33

na lista.

Depois regrave o arquivo.
"""


pessoas =[]

with open("file3.txt", "r") as doc:
    for line in doc:
        nome, idade = line.split(",")
        idade = idade.strip()

        pessoas.append({
            "nome": nome,
            "idade": idade
        })
    pessoas.append({
            "nome": "Jean",
            "idade": 33
        })
    
with open("file3.txt", "w") as doc:
    for pessoa in pessoas:
        doc.write(f"{pessoa['nome']},{pessoa['idade']}\n")

print(pessoas)
