"""
Exercício 1 ⭐⭐

Crie um programa que permita ao usuário cadastrar cidades.

Comandos:

adicionar
listar
fim

Regras:

adicionar pergunta o nome da cidade e adiciona à lista.
listar mostra todas as cidades cadastradas.
fim encerra o programa.
"""
cidades = []

while True:
    options = input("Escolha uma opção:\n 1. Digite 'adicionar' para incluir uma cidade;\n 2. Se quiser ver o que está na lista, digite 'listar';\n 3. Para encerrar a aplicação, digite 'fim'.\n")

    if options == "adicionar":
        while True:
            cidade = input("Digite o nome da cidade ou digite 'voltar' para retornar ao menu principal'.\n")

            if cidade != "voltar":
                cidades.append(cidade)
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