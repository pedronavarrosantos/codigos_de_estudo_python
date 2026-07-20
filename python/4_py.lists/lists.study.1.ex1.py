"""
Exercícios
Exercício 1 ⭐

Crie:

numeros = [10, 20, 30, 40]

Remova o número 40 utilizando pop().

Imprima a lista.
"""
numeros = [10, 20, 30, 40]

numeros.pop(3)

print(numeros)

"""
Exercício 2 ⭐⭐

Crie:

nomes = ["Pedro", "Maria", "João"]

Remova o primeiro elemento usando pop().

Imprima:

Elemento removido: Pedro

Depois imprima a lista restante.
"""
nomes = ["Pedro", "Maria", "João"]

nomes.pop(0)

print(nomes)
"""
Exercício 3 ⭐⭐⭐

Crie uma lista vazia.

Permita ao usuário adicionar palavras.

Quando ele digitar:

desfazer

o último item adicionado deve ser removido usando pop().

Quando digitar:

fim

o programa termina mostrando a lista final.

Esse exercício simula uma funcionalidade de desfazer (undo), muito comum em editores de texto, aplicativos de desenho e diversos softwares.
"""
lista = []

while True:
    palavra = input("Digite uma palavra.\n")
    end = "fim"
    undo = "desfazer"

    if palavra == end.lower():
        print(lista)
        break
    if palavra == undo.lower():
        if len(lista) > 0:
            lista.pop(-1)
        else:
            print("Lista vazia")
    if palavra != end.lower() and palavra != undo.lower():
        lista.append(palavra)
    