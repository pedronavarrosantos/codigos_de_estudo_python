"""
Exercício 9 ⭐⭐⭐⭐⭐

Utilizando a lista carregada do arquivo, adicione:

Stephanie,27

Depois imprima toda a lista.
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

pessoas.append({
    "nome": "Stephanie",
    "idade": 27
})

for pessoa in pessoas:
    print(pessoa)