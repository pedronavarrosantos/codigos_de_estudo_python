"""
Exercício 14 ⭐⭐⭐⭐⭐

Permita cadastrar alunos infinitamente.

Digite:

fim

para parar.
"""
pessoas = []

while True:
    nome = input("Digite o nome ou digite 'fim' para encerrar a aplicação.\n")

    if nome == "fim":
        for key in pessoas:
            print(f"{key["nome"]} - {key["idade"]}.")
        break

    idade = int(input("Digite a idade\n"))

    pessoa = {
        "nome": nome, 
        "idade": idade
        }
    pessoas.append(pessoa)
    print(pessoas)  
    continue