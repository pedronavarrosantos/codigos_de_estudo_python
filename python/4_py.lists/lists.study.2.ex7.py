"""
Exercício 7 ⭐⭐⭐⭐⭐ (Desafio Final)

Transforme tudo em um pequeno sistema.

Menu:

1 - Adicionar cidade
2 - Remover cidade
3 - Buscar cidade
4 - Ordenar cidades
5 - Inverter lista
6 - Listar cidades
7 - Estatísticas
8 - Encerrar

Regras:

Não permitir duplicatas.
Nunca gerar erro caso a lista esteja vazia.
Sempre mostrar mensagens amigáveis ao usuário.
O programa só termina quando o usuário escolher 8.
"""
cidades = []

while True:
    options = input("Digite um número de 1 a 8 para escolher uma das seguintes opções:\n 1. Adicionar cidade;\n 2. Remover cidade;\n 3. Exibir lista;\n 4. Ver detalhes da lista;\n 5. Colocar em ordem alfabética;\n 6. Inverter a ordem da lista;\n 7. Verificar a posição de uma cidade;\n 8. Encerrar aplicação.\n")

    if options == "1":
        while True:
            cidade = input("Digite o nome da cidade ou digite '0' para retornar ao menu principal'.\n")

            if cidade != "0" and cidade not in cidades:
                cidades.append(cidade)
            elif cidade != "0" and cidade in cidades:
                print("A cidade informada já está na lista")
            else:
                print("Retornando ao menu principal.")
                break
    elif options == "2":
        while True:
            cidade = input("Digite o nome da cidade que quer REMOVER ou digite '0' para retornar ao menu principal'.\n")

            if cidade != "0" and cidade in cidades:
                print(f"A cidade {cidade} foi removida da lista.")
                cidades.remove(cidade)
            elif cidade != "0" and cidade not in cidades:
                print("Impossível remover cidade por que já não estava na lista")
            else:
                print("Retornando ao menu principal.")
                break
    elif options == "3":
        print(cidades)
    elif options == "8":
        print("Encerrando aplicação")
        print(cidades)
        break
    elif options == "6":
        cidades.reverse()
        print(cidades)
    elif options == "5":
        cidades.sort()
        print(cidades)
    elif options == "7":
        cidade = input("Digite o nome da cidade para verificar sua posição ou digite 'voltar' para retornar ao menu principal'.\n")

        if cidade in cidades:
            print(f"A Posição da cidade é {cidades.index(cidade)}.")
        else:
            print("Cidade não encontrada.")
    elif options == "4":
        if cidades == []:
            print("A lista está vazia.")
        elif len(cidades) == 1:
            print(f"A única cidade na lista é a {cidades}.")
        else:
            print(f"A quantidade de cidades na lista é {len(cidades)};\n A primeira cidade é a {cidades[0]}\n A última cidade é a {cidades[-1]}")
    else:
        print(f"O comando {options} não é válido.")