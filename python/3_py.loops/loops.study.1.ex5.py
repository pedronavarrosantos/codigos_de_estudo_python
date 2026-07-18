"""
Exercício 5 ⭐⭐⭐
Contador de letras

Peça ao usuário uma palavra.

Utilizando while, conte quantas letras ela possui.

Exemplo:

Digite uma palavra:
Python

Saída:

A palavra possui 6 letras.

Dica: lembre-se da indexação (palavra[indice]).
"""
palavra = "Python"
x = 0

while x < len(palavra):
    print(palavra[x])
    x += 1