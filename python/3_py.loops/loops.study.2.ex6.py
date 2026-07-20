"""
Exercício 6 ⭐⭐⭐

Encontrando um caractere

Peça ao usuário uma palavra.

Depois percorra a palavra.

Se encontrar a letra:

x

Mostre:

A letra x foi encontrada.

Caso contrário:

A letra x não foi encontrada.

Conceitos: for, if e break.
"""
word = input("Por favor, digite uma palavra.\n")

for letra_x in word:
    if letra_x == "x":
        print("A letra 'x' foi encontrada.")
        break
    else:
        print("A letra 'x' NÃO foi encontrada.")