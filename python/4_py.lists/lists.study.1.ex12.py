"""
Exercício 4 ⭐⭐⭐⭐

Crie uma lista de produtos.

produtos = []

Menu:

1 - adicionar
2 - remover
3 - listar
4 - fim

Regras:

Ao adicionar, não permita produtos duplicados.
Ao remover, informe caso o produto não exista.
Ao listar, mostre todos os produtos.
Ao digitar "fim", encerre o programa.
"""
produtos = []

while True:
    options = input("Escolha uma opção:\n 1. Digite 'adicionar' para adicioná-lo à lista;\n 2. Digite 'remover' para tirá-lo da lista;\n 3. Se quiser ver o que está na lista, digite 'listar';\n 4. Para encerrar a aplicação, digite 'fim'.\n")

    if options == "adicionar":
        while True:
            productId = input("Digite o nome do produto.\n Para voltar, digite 'retornar'.\n")

            if productId != "retornar" and productId not in produtos:
                produtos.insert(0, productId)
            elif productId == "retornar":
                break
            else:
                print("Esse produto já está na lista.")
    elif options == "remover":
        while True:
            removeId = input("Digite o nome do produto.\n Para voltar, digite 'retornar'.\n")

            if removeId != "retornar" and removeId in produtos:
                produtos.remove(removeId)
                print(produtos)
            elif removeId == "retornar":
                break
            else:
                print("Esse produto já não estava na lista.")
    elif options == "listar":
        print(produtos)
    elif options == "fim":
        print("Encerrando aplicação e divulgando lista:")
        print(produtos)
        break
    else:
        print(f"O comando {options} não é válido")