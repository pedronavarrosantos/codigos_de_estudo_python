"""
Exercício 9 ⭐⭐⭐⭐⭐
Username

Crie:

def validar_username(username):

Regras:

após usar strip(), o nome não pode estar vazio;
deve começar com @;
deve possuir pelo menos 5 caracteres.

Retorne:

"Username válido"

ou

"Username inválido"

Aqui você reutilizará vários conhecimentos do Módulo 1 (strip(), startswith(), len()) junto com condicionais.
"""
print("Digite o seu username:")

username = input()

def validar_username(username):
    userstrip = username.strip()
    if userstrip[0] == "@" and len(userstrip) >= 5:
        return "Username válido"
    return "Username inválido"

print(validar_username(username))