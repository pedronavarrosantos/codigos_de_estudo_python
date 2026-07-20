frutas = []

while True:
    fruta = input("Escolha uma opção:\n 1. Digite o nome de uma fruta para removê-la. \n 2. Digite 'fim'para fechar o gerenciador. \n 3. Digite 'adicionar' para aumentar a lista de frutas.\n")
    end = "fim"
    aumentar = "adicionar"

    if fruta == end.lower():
        print("Gerenciador encerrado.")
        break

    if fruta == aumentar.lower():
        while True:
            retroceder = "voltar"
            fruta = input("Escolha uma opção:\n 1. Digite o nome de uma fruta. \n Digite 'voltar' para retornar à aplicação anterior.\n")

            if fruta != retroceder.lower():
                frutas.append(fruta)
                print(frutas)
            else:
                print("Retornando.")
                break

    elif fruta in frutas:
        frutas. remove(fruta)

        print("Fruta removida")
        print(frutas)

        if frutas == []:
            print("Acabaram as frutas")
            break

        continue
    else:
        print("Fruta não encontrada")
        print(frutas)
        continue

