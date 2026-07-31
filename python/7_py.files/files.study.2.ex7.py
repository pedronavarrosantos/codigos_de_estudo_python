"""
Exercício 7 ⭐⭐⭐⭐⭐

Utilizando a lista carregada do arquivo, altere a idade de Maria para 23.

Depois imprima a lista atualizada.
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
    if pessoa["nome"] == "Maria":
        pessoa.update({
            "idade": 23
        })
        break
    else:
        continue
for pessoa in pessoas:
    print(pessoa)