"""
Exercícios
Exercício 1 ⭐

Crie:

nomes = ["Pedro", "Maria", "João"]

Inverta a lista.
"""
nomes = ["Pedro", "Maria", "João"]

nomes.reverse()

print(nomes)

"""
Exercício 2 ⭐⭐

Crie:

numeros = [5, 8, 2, 1]

Mostre:

lista original;
lista invertida.
"""
numeros = [5, 8, 2, 1]

print(numeros)

numeros.reverse()

print(numeros)

"""
Exercício 3 ⭐⭐⭐

Utilize:

idades = [18, 42, 21, 35]
Ordene em ordem crescente.
Mostre a lista.
Inverta usando reverse().
Mostre novamente.

O objetivo é perceber a diferença entre:

sort(reverse=True)

e

sort()
reverse()
"""
idades = [18, 42, 21, 35]

idades.sort()

print(idades)

idades.reverse()

print(idades)

"""
Exercício 4 ⭐⭐⭐⭐

Crie um programa que permita ao usuário adicionar palavras em uma lista.

Sempre que ele digitar:

inverter

a lista deverá ser invertida e exibida.

Quando digitar:

fim

o programa termina mostrando a lista final.
"""
lista = []

while True:
    word = input("Escolha uma opção:\n 1. Digite uma palavra; \n 2. Caso queira inverter a lista das palavras, digite 'inverter'.\n 3. Caso queria encerrar a aplicação, digite 'fim'.\n")

    if word == "fim":
        print(lista)
        break
    elif word == "inverter":
        lista.reverse()
        print(lista)
    else:
        lista.append(word)