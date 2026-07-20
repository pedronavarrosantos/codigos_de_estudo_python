"""
Exercício 3 ⭐⭐
Apenas pares

Imprima todos os números pares entre 0 e 20 utilizando o terceiro parâmetro do range().

Saída esperada:

0
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

Conceito: range(início, fim, passo).
"""
for num in range(21):
    if num % 2 == 0:
        print(num)