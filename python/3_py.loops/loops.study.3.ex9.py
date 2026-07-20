"""
Exercício 9 ⭐⭐⭐⭐⭐
Invertendo uma palavra

Peça uma palavra ao usuário.

Utilizando range() com passo negativo, imprima a palavra invertida.

Exemplo:

Entrada:

Python

Saída:

nohtyP

Dica: não utilize [::-1]. O objetivo é praticar range().

Conceitos: passo negativo + indexação.
"""
word = input("Digite uma palavra\n")

for letter in range(len(word) -1, -1, -1):
    print(word[letter])