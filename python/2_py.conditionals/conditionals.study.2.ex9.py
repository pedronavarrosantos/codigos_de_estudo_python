"""
Exercício 9 ⭐⭐⭐⭐⭐
Cadastro de usuário

Crie:

def validar_cadastro(nome, username):

Será válido somente se:

nome não estiver vazio;
username começar com @;
username possuir pelo menos 5 caracteres.

Retorne:

Cadastro válido

ou

Cadastro inválido
"""
nome = input("Qual é o seu nome?\n")
username = input("Escolha um username, ele deve começar com '@'.\n")

def validar_cadastro(nome, username):
    if nome.strip() != "" and len(username) >= 5 and username.startswith("@"):
        print("Cadastro válido.")
    else:
        print("Cadastro inválido.")

validar_cadastro(nome, username)