"""
Exercício 5 ⭐⭐⭐⭐⭐

Remova Carlos da lista.

Regrave o arquivo.

Ao abrir o arquivo novamente, Carlos não deve mais existir.
"""

pessoas = []

with open("file3.txt", "r") as doc:
    for line in doc:
        nome, idade = line.split(",")
        idade = idade.strip()

        pessoas.append({
            "nome": nome,
            "idade": idade
        })

for pessoa in pessoas:
        if pessoa["nome"] == "Carlos":
            pessoas.remove(pessoa)
            break

with open("file3.txt", "w") as doc: 
    for pessoa in pessoas:
        doc.write(f"{pessoa['nome']},{pessoa['idade']}\n")

with open("file3.txt", "r") as doc:
    print(doc.read())