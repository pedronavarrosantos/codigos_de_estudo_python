"""
Exercícios
Exercício 1 ⭐

Crie:

numeros = [1, 2, 3, 2, 4, 2]

Mostre quantas vezes o número 2 aparece.
"""
numeros = [1, 2, 3, 2, 4, 2]

print(numeros.count(2))

"""
Exercício 2 ⭐⭐

Crie:

nomes = [
    "Pedro",
    "Maria",
    "Pedro",
    "Ana",
    "Pedro"
]

Mostre quantas vezes "Pedro" aparece.
"""
nomes = [
    "Pedro",
    "Maria",
    "Pedro",
    "Ana",
    "Pedro"
]

print(nomes.count("Pedro"))

"""
Exercício 3 ⭐⭐⭐

Peça cinco nomes ao usuário e armazene-os em uma lista.

Depois pergunte:

Qual nome deseja procurar?

Mostre quantas vezes esse nome aparece utilizando count().
"""
listaNomes = []

for contador in range(5):
    nome2 = input("Digite 5 nomes separadamente.\n")
    listaNomes.append(nome2)
else:
    busca = input("Qual nome deseja procurar?\n")
    print(listaNomes.count(busca))

"""
Exercício 4 ⭐⭐⭐⭐

Crie uma lista vazia.

Permita que o usuário digite palavras.

Quando ele digitar:

contar

o programa deverá perguntar:

Qual palavra deseja contar?

Depois utilize count() para informar quantas vezes ela aparece na lista.

Quando o usuário digitar:

fim

o programa deve terminar mostrando a lista final.
"""
lista = []



while True:
    palavra = input("Escolha uma opção:\n 1. Digite uma palavra;\n 2. Digite 'contar' para verificar quantas vezes ocorre uma palavra;\n 3. Digite 'fim' para encerrar a aplicação.\n")

    if palavra != "contar" and palavra != "fim":
        lista.append(palavra)
    elif palavra == "contar":
        busca = input("Qual palavra deseja contar?\n")
        print(lista.count(busca))
    else:
        print(lista)
        break
