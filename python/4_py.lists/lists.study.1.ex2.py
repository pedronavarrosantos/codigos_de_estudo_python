"""
Exercícios
Exercício 1 ⭐

Crie:

nomes = ["Maria", "João"]

Insira "Pedro" na primeira posição.

Imprima a lista.
"""
nomes = ["Maria", "João"]

nomes.insert(0, "Pedro")

print(nomes)

"""
Exercício 2 ⭐⭐

Crie:

numeros = [10, 30, 40]

Insira 20 entre 10 e 30.

Imprima a lista.
"""
numeros = [10, 30, 40]

numeros.insert(1, 20)

print(numeros)

"""
Exercício 3 ⭐⭐⭐

Crie uma lista vazia.

Permita que o usuário digite palavras.

Se ele digitar:

inicio

o programa deve perguntar:

Qual palavra deseja colocar no início?

e inserir essa palavra na posição 0.

Caso contrário, a palavra digitada deve ser adicionada normalmente ao final da lista com append().

Quando o usuário digitar:

fim

imprima a lista e encerre o programa.
"""
lista = []

while True:
    palavra = input("Escolha uma opção:\n 1. Palavra que vai no início: Digite 'inicio';\n 2. Palavra qualquer que vai em outra posição: Digite a palavra;\n 3. Digite fim para encerrar a aplicação.\n")
    
    if palavra == "fim":
        print("Encerrando aplicação.")
        print(lista)
        break
    elif palavra == "inicio":
        palavra = input("Digite a palavra que vai no início.\n")
        lista.insert(0, palavra)
    else:
        lista.append(palavra)