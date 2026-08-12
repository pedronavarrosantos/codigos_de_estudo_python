"""
⭐⭐⭐⭐ Exercício 4 — Menu de fila

Crie um programa com:

1 - Adicionar pessoa
2 - Atender pessoa
3 - Mostrar fila
4 - Sair

Regras:

1 adiciona uma pessoa ao final;
2 atende a primeira pessoa;
3 mostra a fila atual;
4 encerra.

Não use pop() nesse exercício. A remoção deve ser feita com pop(0).
"""
clientes = []

while True:
    options = input("== Sistema de pedidos. ==\nEscolha um número:\n"
    " 1 - Adicionar pessoa;\n"
    " 2 - Atender pessoa;\n"
    " 3 - Mostrar fila;\n"
    " 4 - Sair.\n"
    "========================\n")

    if options == "1":
        user = input("Digite o nome da pessoa:\n")

        clientes.append(user)

        print(f"Cliente {user} adicionado.")
    elif options == "2":
        while True:
            if len(clientes) > 0:
                atender = input("Deseja atender o próximo da fila?\nEscolha um número:\n"
                " 1 - Sim;\n"
                " 2 - Não e retornar ao menu principal.\n")
                if atender == "1":
                    print(f"Cliente {clientes[0]} atendido e removido da fila.")
                    clientes.pop(0)
                if atender == "2":
                    print("== Retornando. ==")
                    break
            else:
                print("== Lista Vazia. ==")
                break
    elif options == "3":
        counter = 1
        for pessoa in clientes:
            print(f"{counter}. {pessoa}.")

            counter += 1
        if len(clientes) == 0:
            print("== Fila vazia. ==")
    elif options == "4":
        print("== Encerrando aplicação. ==")
        break
    else:
        print(f"== O comando {options} não é válido.")