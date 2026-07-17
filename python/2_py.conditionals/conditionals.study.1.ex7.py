"""
Exercício 7 ⭐⭐⭐⭐
Desconto

Crie:

def possui_desconto(estudante, idoso):

A pessoa recebe desconto se:

for estudante ou
for idosa.

Retorne:

"Tem desconto"

ou

"Sem desconto"
"""

print("Olá qual é o seu nome?")

nome = input()

print(f"{nome}, você é estudante?")

estudante = input()

print("É idoso?")

idoso = input()

def possui_desconto(estudante, idoso):
    if (estudante or idoso) == "Sim" or (estudante or idoso) == "Sou" or (estudante or idoso) == "sim" or (estudante or idoso) == "sou":
        return "Tem desconto"
    return "Sem desconto"

print(possui_desconto(estudante, idoso))