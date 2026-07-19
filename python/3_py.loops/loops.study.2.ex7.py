"""
Exercício 7 ⭐⭐⭐⭐

Ignorando espaços

Percorra:

frase = "Aprender Python é divertido"

Imprima todos os caracteres.

Porém, ignore os espaços utilizando continue.

Conceitos: continue dentro do for.
"""
frase = "Aprender Python é divertido"

for caractere in frase:
    if caractere == " ":
        continue
    print(caractere)