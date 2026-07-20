"""
Exercício 4 ⭐⭐
Soma dos números

Calcule a soma dos números de 1 até 100 utilizando for e range().

Ao final, imprima:

5050

Conceitos: acumulador + range().
"""
ac = 0

for num in range(1, 101):
    ac += num

    if num == 100:
        print(ac)