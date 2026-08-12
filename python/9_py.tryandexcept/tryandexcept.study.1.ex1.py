"""
⭐ Exercício 1

Peça um número inteiro:

Digite um número inteiro:

Se o usuário digitar algo que não seja inteiro, mostre:

Valor inválido.

Não deixe o programa quebrar.
"""
while True:
    try:
        num = int(input("Digite um número:\n"))
        break
    except ValueError:
        print("O valor inserido é inválido.\n")
print(f"O número escolhido foi o {num}.\n")