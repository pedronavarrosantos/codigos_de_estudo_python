"""
Exercício 7 ⭐⭐⭐⭐
Ignorando múltiplos de 3

Imprima os números de 1 até 20.

Porém, não imprima os múltiplos de 3.

Utilize continue.

Saída esperada:

1
2
4
5
7
8
10
11
13
14
16
17
19
20
"""
num = 1

while num <= 20:
    if num % 3 == 0:
        num += 1
        continue
    print(f"{num}")
    num += 1