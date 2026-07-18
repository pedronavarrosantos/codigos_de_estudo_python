"""
Exercício 9 ⭐⭐⭐⭐⭐
Soma apenas dos positivos

Peça números ao usuário continuamente.

Se o usuário digitar:

0

o programa deve terminar.

Some apenas os números positivos.

Ignore os negativos utilizando continue.

No final, exiba:

Soma = ...

Conceitos: acumulador, continue, break (ou condição do while, se preferir).
"""

soma = 0

while True:
    num = int(input("Digite um número."))

    if num == 0:
        break

    if num < 0:
        continue

    soma += num
print (soma)
    
    