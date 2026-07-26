"""
Exercício 5 ⭐⭐⭐⭐⭐

Crie um programa que peça um nome ao usuário.

Sempre que um nome for digitado, ele deve ser adicionado ao arquivo:

nomes.txt

Quando o usuário digitar:

fim

o programa encerra.
"""
while True:
    nom = input("Digite um nome;\n Ou 'fim' para encerrar a aplicação.\n")

    if nom != "fim":
        with open("addUser.txt", "a") as doc:
            doc.write(f"{nom}\n")
    else:
        print("Encerrando aplicação")
        break

