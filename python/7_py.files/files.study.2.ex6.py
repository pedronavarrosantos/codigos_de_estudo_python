"""
Exercício 6 ⭐⭐⭐⭐⭐

Depois de carregar o arquivo para uma lista de dicionários, peça um nome.

Caso exista, mostre:

Pedro encontrado.
Idade: 27

Caso contrário:

Aluno não encontrado.
"""
pessoas = []

with open("file2.txt", "r") as doc:

    for line in doc:
        nome, idade = line.split(",")
        idade = idade.strip()

        pessoas.append({
            "Nome": nome,
            "Idade": idade
        })

encontrarPessoa = input("Digite o nome da pessoa que deseja encontrar:\n")
found = False

for pessoa in pessoas:
    if pessoa["Nome"] == encontrarPessoa:
        print(f"{pessoa["Nome"]} foi encontrado(a).")
        found = True
        break
    else:
        continue
if not found:
    print(f"{encontrarPessoa} não foi encontrado(a).")