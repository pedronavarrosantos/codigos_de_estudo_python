"""
🐍 Exercício 4 ⭐⭐⭐

Crie:

def validar_senha(senha):

Regras:

Primeiro verifique se a senha está vazia.

Se estiver:

Senha vazia

Caso contrário:

Se começar com letra:

Senha válida

Senão:

Senha inválida

Objetivo: evitar acessar senha[0] antes de garantir que ela possui pelo menos um caractere.
"""
senha = input("Digite a sua senha.\n")

def validar_senha(senha):
    if senha.strip() != "":
        if senha[0].isalpha():
            print("Senha válida.")
        else:
            print("Senha inválida.")
    else:
        print("Senha vazia")

validar_senha(senha)