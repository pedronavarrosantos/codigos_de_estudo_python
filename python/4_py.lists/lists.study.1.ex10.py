"""
Exercício 2 ⭐⭐

Peça ao usuário uma letra.

Verifique se ela existe na palavra:

palavra = "Programacao"

Mostre:

A letra existe.

ou

A letra não existe.
"""
palavra = "Programacao"

letter = input("Escolha uma letra:\n")


if palavra.lower().find(letter) != -1:
    print(f"A letra {letter} está na palavra.")
else:
    print(f"A letra {letter} NÃO está na palavra")