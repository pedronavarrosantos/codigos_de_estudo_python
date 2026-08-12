"""
⭐⭐⭐⭐⭐ Exercício 5 — Fila do Coffee Shop

Crie uma fila de pedidos contendo dicionários:

id
cliente
produto
quantidade

O sistema deve permitir:

1 - Novo pedido
2 - Processar próximo pedido
3 - Mostrar pedidos na fila
4 - Sair

A regra fundamental é:

O pedido que entrar primeiro deve ser sempre o primeiro a ser processado.

Esse é o primeiro exercício em que você estará aplicando uma fila de verdade ao sistema da Tia Rosa.
"""
pedidos = []

while True:
    options = input("== Sistema de pedidos. ==\nEscolha um número:\n"
    " 1 - Novo pedido;\n"
    " 2 - Processar próximo pedido;\n"
    " 3 - Mostrar pedidos na fila;\n"
    " 4 - Sair.\n"
    "========================\n")

    if options == "1":
        if len(pedidos) == 0:
            pedido_counter = 100
        else:
            pedido_counter = pedidos[-1]["id"] + 1
        user = input("Digite o nome do cliente:\n")
        produto = input("Digite o produto:\n")
        try:
            qnt = int(input("Digite a quantidade:\n"))
        except ValueError:
            print("Valor inválido.")
        pedidos.append({
            "id": pedido_counter,
            "cliente": user,
            "produto": produto,
            "quantidade": qnt
        })
        print(pedidos[-1])

    elif options == "2":
        while True:
            if len(pedidos) > 0:
                atender = input("Deseja processar o próximo pedido da fila?\nEscolha um número:\n"
                " 1 - Sim;\n"
                " 2 - Não e retornar ao menu principal.\n")
                if atender == "1":
                    print(f"Pedido {pedidos[0]} processado e removido da fila.")
                    pedidos.pop(0)
                elif atender == "2":
                    print("== Retornando. ==")
                    break
            else:
                print("== Lista Vazia. ==")
                break
    elif options == "3":
        counter = 1
        for pedido in pedidos:
            print(f"Pedido número: {pedido['id']} -> Cliente {pedido['cliente']}.")

            counter += 1
        if len(pedidos) == 0:
            print("== Fila vazia. ==")
    elif options == "4":
        print("== Encerrando aplicação. ==")
        break
    else:
        print(f"== O comando {options} não é válido.")