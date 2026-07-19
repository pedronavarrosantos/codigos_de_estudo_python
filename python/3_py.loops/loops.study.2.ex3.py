"""
Exercício 3 ⭐⭐

Contando vogais

Crie um programa que conte quantas vogais existem na palavra.

Exemplo:

palavra = "Programacao"

Saída:

A palavra possui 5 vogais.

Considere apenas:

a
e
i
o
u

Conceito: for + if.
"""
palavra = "Programacao"
vc = 0

for vogal in palavra:
    if vogal == "a" or vogal == "e" or vogal == "i" or vogal == "o" or vogal == "u":
        vc += 1

print (f"A palavra possui {vc} vogais.")