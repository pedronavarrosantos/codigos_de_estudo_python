"""
Exercício 8 ⭐⭐⭐⭐
Índices das vogais

Peça uma palavra ao usuário.

Mostre apenas os índices onde existem vogais.

Exemplo:

Digite uma palavra:
Programacao

Saída:

1
3
5
8
10

Conceitos: range(len()) + indexação.
"""
palavra = "Programacao"

for num in range(len(palavra)):
    if palavra[num] == "a" or palavra[num] == "e" or palavra[num] == "i" or palavra[num] == "o" or palavra[num] == "u":
        print(num)