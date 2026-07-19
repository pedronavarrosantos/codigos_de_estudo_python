"""
Exercício 5 ⭐⭐⭐

Contando números

Percorra:

texto = "abc123xyz45"

Conte quantos números existem.

Saída:

Existem 5 números.

Dica: isdigit().
"""
texto = "abc123xyz45"
nc = 0

for digit in texto:
    if digit.isdigit():
        nc += 1

print(f"O texto tem {nc} números.")
