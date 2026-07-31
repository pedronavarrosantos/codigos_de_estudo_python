"""
Exercício 2 ⭐⭐

Utilizando o mesmo arquivo, utilize split(",") para separar as informações.

Imprima:

Pedro
27
Maria
22
Carlos
31
"""
with open("file2.txt", "r") as doc:
    for line in doc:
        nome, idade = line.split(",")
        idade = idade.strip()

        print (nome)
        print (idade)