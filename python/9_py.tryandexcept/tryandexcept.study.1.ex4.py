"""
⭐⭐⭐⭐ Exercício 4

Faça um programa que peça o preço de um produto:

Digite o preço:

O preço deve aceitar números decimais usando float().

Exemplo:

Digite o preço: 12.50
Preço registrado: 12.5

Se for inválido:

Preço inválido.
"""
while True:
    preco = input("Digite o preço do produto (Escreva com as casas decimais, ex.: 12.45):\n")
    try:
        fpreco = float(preco)
        break
    except ValueError:
        print(f"{preco} é um valor inválido, digite apenas números decimais.")

print(f"O preço do produto é {fpreco}.")