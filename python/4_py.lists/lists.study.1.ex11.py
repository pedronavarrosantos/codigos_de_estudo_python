"""
Exercício 3 ⭐⭐⭐

Crie uma lista vazia.

Permita que o usuário digite nomes.

Se o nome já existir:

Nome já cadastrado.

Caso contrário:

adicione-o à lista.

Quando digitar:

fim

mostre a lista.
"""
lista = []

while True:
    nome = input("Digite um nome para adicionar à lista:\n")

    if nome != "fim" and nome not in lista:
        lista.append(nome)
    elif nome != "fim" and nome in lista:
        print("Esse nome já está na lista.")
    else:
        print(lista)
        break