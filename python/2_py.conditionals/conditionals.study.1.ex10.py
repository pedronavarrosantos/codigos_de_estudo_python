"""
Exercício 10 👑 — Chefe da Lista
Sistema de cadastro

Crie:

def cadastrar_usuario(nome, idade, senha):

O cadastro só será aceito se:

o nome não estiver vazio (strip());
a idade for maior ou igual a 18;
a senha possuir pelo menos 8 caracteres.

Se tudo estiver correto:

"Cadastro realizado"

Caso contrário:

"Cadastro inválido"
"""
nome = input("Digite o seu nome:")
idade = int(input("Digite a sua idade:"))
senha = input("Escolha a sua senha:")

def cadastrar_usuario(nome, idade, senha):
    if len(nome.strip()) > 0 and idade >= 18 and len(senha) >= 8:
        return "Cadastro realizado"
    return "Cadastro inválido"

print(cadastrar_usuario(nome, idade, senha))