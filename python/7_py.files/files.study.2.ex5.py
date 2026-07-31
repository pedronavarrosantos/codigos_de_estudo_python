"""
Exercício 5 ⭐⭐⭐⭐

Após criar a lista de dicionários, percorra-a imprimindo:

Nome: Pedro
Idade: 27

Nome: Maria
Idade: 22

Nome: Carlos
Idade: 31
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
        print(f"Nome: {pessoa['nome']}")
        print(f"Idade: {pessoa['idade']}")