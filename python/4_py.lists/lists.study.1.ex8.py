"""
Exercício 4 ⭐⭐⭐⭐

Crie uma lista vazia.

Permita ao usuário adicionar palavras.

Além dos comandos já vistos (fim, por exemplo), implemente um novo comando:

buscar

Quando o usuário digitar:

buscar

o programa deverá perguntar:

Qual palavra deseja localizar?

Se ela existir:

A palavra está na posição X.

Caso contrário:

Palavra não encontrada.

Quando o usuário digitar:

fim

o programa encerra mostrando a lista final.
"""
lista = []
stopper = 0

while stopper == 0:
    veiculo = input("Escolha uma opção:\n 1. Digite um tipo de veículo;\n 2. Para verificar em qual posição da lista está um veículo, digite 'buscar';\n 3. Para encerrar a aplicação digite 'fim'.\n")

    if veiculo != "buscar" and veiculo != "fim":
        lista.append(veiculo)
    elif veiculo == "buscar":
        busca = input("Digite o nome do veículo que quer buscar:\n")
        if busca not in lista:
            print("Veículo não encontrado")
        else:
            posicao = lista.index(busca)
            print(f"A posição do {busca} é {posicao}.")
    else:
        print(lista)
        stopper = 1