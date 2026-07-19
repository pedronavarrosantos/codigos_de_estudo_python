"""
Exercício 4 ⭐⭐

Somente maiúsculas

Percorra:

texto = "PyThOn"

Imprima apenas as letras maiúsculas.

Saída:

P
T
O

Dica: lembre-se de isupper().
"""
texto = "PyThOn"

for let_alta in texto:
    if let_alta.isupper():
        print(let_alta)