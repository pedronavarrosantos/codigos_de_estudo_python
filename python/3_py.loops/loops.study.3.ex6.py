"""
Exercício 6 ⭐⭐⭐
Letras nas posições pares

Percorra:

palavra = "Programacao"

Imprima apenas as letras que estão em índices pares.

Saída esperada:

P
o
r
m
c
o

Conceitos: índice + operador %.
"""
palavra = "Programacao"

for even in range(len(palavra)):
    if even %  2 == 0:
        print(f"{palavra[even]}")