"""
Exercício 8 ⭐⭐⭐⭐⭐

Utilizando a lista carregada do arquivo, remova Carlos.

Depois imprima a lista.
"""
pessoas = []

with open("file2.txt", "r") as doc:
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
    else:
        continue
for pessoa in pessoas:
    print(pessoa)