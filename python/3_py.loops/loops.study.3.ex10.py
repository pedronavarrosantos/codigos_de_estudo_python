"""
👑 Exercício 10 — Chefe da Lista
Comparador de palavras

Peça duas palavras ao usuário.

Compare letra por letra.

Mostre todas as posições em que elas possuem letras diferentes.

Exemplo:

Entrada:

casa
cama

Saída:

Posição 2:
s != m

Desafio extra: se as palavras tiverem tamanhos diferentes, informe isso antes da comparação.
"""
word1 = input("Digite a primeira palavra.\n")
word2 = input("Digite a segunda palavra.\n")

if len(word1) != len(word2):
    print("As palavras têm tamanhos diferentes.")
else:
     for char in range(len(word1)):
        if word1[char] != word2[char]:
            print(f"posição{char}\n {word1[char]} != {word2[char]}")