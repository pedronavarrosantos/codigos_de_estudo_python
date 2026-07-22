"""
Exercício 3 ⭐⭐⭐

Acrescente um novo comando:

remover

Ele deve perguntar:

Qual cidade deseja remover?

Se existir:

Cidade removida.

Caso contrário:

Cidade não encontrada.
"""
cidades = []

while True:
    options = input("Escolha uma opção:\n 1. Digite 'adicionar' para incluir uma cidade;\n 2. Para tirar uma cidade da lista, digite 'remover';\n 3. Se quiser ver o que está na lista, digite 'listar';\n 4. Para encerrar a aplicação, digite 'fim'.\n")

    if options == "adicionar":
        while True:
            cidade = input("Digite o nome da cidade ou digite 'voltar' para retornar ao menu principal'.\n")

            if cidade != "voltar" and cidade not in cidades:
                cidades.append(cidade)
            elif cidade != "voltar" and cidade in cidades:
                print("A cidade informada já está na lista")
            else:
                print("Retornando ao menu principal.")
                break
    elif options == "remover":
        while True:
            cidade = input("Digite o nome da cidade que quer REMOVER ou digite 'voltar' para retornar ao menu principal'.\n")

            if cidade != "voltar" and cidade in cidades:
                print(f"A cidade {cidade} foi removida da lista.")
                cidades.remove(cidade)
            elif cidade != "voltar" and cidade not in cidades:
                print("Impossível remover cidade por que já não estava na lista")
            else:
                print("Retornando ao menu principal.")
                break
    elif options == "listar":
        print(cidades)
    elif options == "fim":
        print("Encerrando aplicação")
        print(cidades)
        break
    else:
        print(f"O comando {options} não é válido.")