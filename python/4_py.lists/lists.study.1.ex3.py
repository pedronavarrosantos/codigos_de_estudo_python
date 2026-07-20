"""
Exercícios
Exercício 1 ⭐

Crie:

numeros = [7, 2, 9, 1, 5]

Ordene em ordem crescente.

Imprima a lista.
"""
numeros = [7, 2, 9, 1, 5]

numeros.sort()

print(numeros)

"""
Exercício 2 ⭐⭐

Crie:

nomes = ["Carlos", "Ana", "Pedro", "Bruno"]

Ordene em ordem alfabética.
"""
nomes = ["Carlos", "Ana", "Pedro", "Bruno"]

nomes.sort()

print(nomes)

"""
Exercício 3 ⭐⭐⭐

Utilize:

idades = [21, 35, 18, 42, 27]

Mostre:

Lista original.
Lista em ordem crescente.
Lista em ordem decrescente.
"""
idades = [21, 35, 18, 42, 27]

idades.sort()

print(idades)

idades.sort(reverse=True)

print(idades)

"""
Exercício 4 ⭐⭐⭐⭐

Crie uma lista vazia.

Permita que o usuário digite nomes.

Quando ele digitar:

ordenar

a lista deve ser organizada em ordem alfabética e exibida.

Quando ele digitar:

fim

o programa termina mostrando a lista final.
"""
lista = []

while True:
    nomes_2 = input("Digite um nome de cada vez.\n")

    if nomes_2 == "ordenar":
        lista.sort()
        print(lista)
    elif nomes_2 == "fim":
        print(lista)
        break
    else:
        lista.append(nomes_2)
        