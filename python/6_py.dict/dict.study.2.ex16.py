"""
Exercício 15 ⭐⭐⭐⭐⭐

Faça um menu:

1 Adicionar

2 Procurar

3 Alterar idade

4 Remover

5 Mostrar lista

6 Sair
"""
pessoas = []

while True:
    options = input("Escolha um número:\n 1. Adicionar;\n 2. Procurar;\n 3. Alterar idade;\n 4. Remover;\n 5. Mostrar lista;\n 6. Sair.\n")

    if options == "1":
        while True:
            nom = input("Digite o nome da pessoa para adicioná-la ou '0' para retornar ao menu principal.\n")
            
            if nom == "0":
                print("Retornando")
                break
            
            idade = int(input("Digite a idade da pessoa:\n"))

            pessoa = ({
                "nome": nom,
                "idade": idade
            })
            pessoas.append(pessoa)
            print(pessoas)
    elif options == "2":
        while True:
            nomOrAge = input("Deseja procurar alguém pelo nome ou pela idade? Para retornar ao menu principal digite '0'.\n")

            if nomOrAge == "0":
                    print("Retornando")
                    break
            elif nomOrAge == "nome":
                nom = input("Digite o nome da pessoa para procurá-la:\n")

                for pessoa in pessoas:
                    if pessoa["nome"] == nom:
                        print(pessoa)
            if nomOrAge == "idade":
                idade = int(input("Digite a idade:\n"))

                print(f"A(as) pessoa(as) com {idade} anos é(são):")
                for pessoa in pessoas:
                    if pessoa["idade"] == idade:
                        print(pessoa)
                    else:
                        continue
    elif options == "3":
        nom = input("Digite o nome da pessoa que quer alterar a idade:\n")
        found = False

        for pessoa in pessoas:
            if pessoa["nome"] == nom:
                age = int(input("Digite a idade que deseja colocar:\n"))
                pessoa.update({
                    "idade": age
                })
                print(pessoa)
                found = True
                break
        if not found:
            print("Pessoa não encontrada.")  
    elif options == "4":
        while True:
            nom = input("Digite o nome da pessoa para removê-la ou '0' para retornar ao menu principal.\n")
            found = False

            if nom == "0":
                print("Retornando")
                break
            for pessoa in pessoas:
                if pessoa["nome"] == nom:
                    pessoas.remove(pessoa)
                    print("Pessoa removida")
                    print(pessoas)
                    found = True
                    break
                else:
                    continue
            if not found:
                print("Pessoa não encontrada.")      
    elif options == "5":
        for pessoa in pessoas:
            print(f"{pessoa['nome']} - {pessoa['idade']}.")
    elif options == "6":
        print("Encerrando aplicação")
        break
    else:
        print(f"O comando {options} não é válido.")