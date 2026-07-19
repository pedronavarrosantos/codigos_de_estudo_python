"""
Exercício 2 ⭐

Contando caracteres

Percorra:

nome = "Pedro"

Conte quantos caracteres existem sem utilizar len().

Ao final, imprima:

O nome possui 5 caracteres.

Conceito: acumulador dentro do for.
"""
nome = "Pedro"
ac = 0

for c in nome:
    ac+= 1

print(f"O nome possui {ac} caracteres.")