"""
Exercício 7 ⭐⭐⭐⭐
Contando letras maiúsculas

Percorra:

texto = "PyThOn É InCrÍvEl"

Conte quantas letras maiúsculas existem.

Ao final, imprima:

Existem X letras maiúsculas.

Conceitos: range(len()) + isupper().
"""
texto = "PyThOn É InCrÍvEl"
contador_maiusculas = 0

for char in range(len(texto)):
    if texto[char].isupper():
        contador_maiusculas += 1
        
print(f"Existem {contador_maiusculas} letras maiúsculas.")