"""
Exercício 2 ⭐⭐⭐

Modifique o exercício anterior.

Agora não permita cidades repetidas.

Se a cidade já existir:

Cidade já cadastrada.
"""
cidades = []

while True:
    options = input("Escolha uma opção:\n 1. Digite 'adicionar' para incluir uma cidade;\n 2. Se quiser ver o que está na lista, digite 'listar';\n 3. Para encerrar a aplicação, digite 'fim'.\n")

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
    elif options == "listar":
        print(cidades)
    elif options == "fim":
        print("Encerrando aplicação")
        print(cidades)
        break
    else:
        print(f"O comando {options} não é válido.")