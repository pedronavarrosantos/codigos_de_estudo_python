"""
⭐⭐ Exercício 2 — TypeError

Você possui:

nome = "Pedro"
idade = 27

Tente concatenar os dois valores usando +.

Capture o TypeError e mostre:

Não é possível juntar esses valores dessa forma.
"""
print("Vamos concatenar elementos.")

elemento_1 = input("Digite o primeiro elemento:\n")

while True:
    try:
        elemento_2 = int(input("Digite o segundo elemento:\n"))
        produto = elemento_1 + elemento_2
        break
    except TypeError:
        print("Não é possível juntar esses valores dessa forma.")

print(produto)