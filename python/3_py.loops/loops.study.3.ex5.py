"""
Exercício 5 ⭐⭐⭐
Índices da palavra

Percorra:

palavra = "Python"

Imprima:

Posição 0: P
Posição 1: y
Posição 2: t
Posição 3: h
Posição 4: o
Posição 5: n

Conceitos: range(len()).
"""
palavra = "Python"

for i in range(len(palavra)):
    print(f"Posição {i}: {palavra[i]}")