"""
👑 Exercício 10 — Chefe da Lista
Sistema da Biblioteca

Crie:

def emprestar_livro(idade, cadastro, multas):

Uma pessoa pode pegar um livro emprestado apenas se:

tiver cadastro (True);
não possuir multas (False);
possuir pelo menos 16 anos.

Retorne:

Empréstimo autorizado

ou

Empréstimo negado

💡 Dica: este exercício foi criado para que você use, de forma natural, o operador not.
"""
idade = int(input("Qual é a sua idade?\n"))
cadastro = input("Você possui cadastro?\n")
multas = input("Você possui multas?\n")

def emprestar_livro(idade, cadastro, multas):
    if cadastro.lower() == "sim" or cadastro.lower() == "tenho":
        cadastro = True
    else:
        cadastro = False
    if multas.lower() == "não" or multas.lower() == "não tenho":
        multas = False
    else:
        multas = True
    if idade >= 16 and cadastro and not multas:
        print("Empréstimo autorizado")
    else:
        print("Empréstimo negado")

emprestar_livro(idade, cadastro, multas)