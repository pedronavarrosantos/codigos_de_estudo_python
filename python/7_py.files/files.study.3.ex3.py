"""
Exercício 3 ⭐⭐⭐

Altere a idade de Maria para 23 na lista.

Depois regrave o arquivo.

Abra novamente o arquivo e confirme que agora aparece:

Maria,23
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
        if pessoa["nome"] == "Maria":
            pessoa.update({
                "idade": 23
            })
            break
        else:
            continue

with open("file3.txt", "w") as doc:
    for pessoa in pessoas:
        doc.write(f"{pessoa['nome']},{pessoa['idade']}\n")

with open("file3.txt", "r") as doc:
    print(doc.read())