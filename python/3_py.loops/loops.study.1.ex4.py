"""
Exercício 4 ⭐⭐
Apenas pares

Imprima todos os números pares entre 1 e 20 utilizando while.

Saída esperada:

2
4
6
8
10
12
14
16
18
20

Dica: utilize o operador %.
"""
x = 1

while x <= 20:
    if x % 2 == 0:
        print(x)
    x += 1