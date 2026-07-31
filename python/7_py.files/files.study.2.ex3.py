"""
Exercício 3 ⭐⭐⭐

Utilizando split() e strip(), imprima:

Pedro tem 27 anos.
Maria tem 22 anos.
Carlos tem 31 anos.
"""
with open("file2.txt", "r") as doc:
    for line in doc:
        nome, idade = line.split(",")
        idade = idade.strip()

        print(f"{nome} tem {idade} anos.")