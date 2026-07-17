"""
🐍 Exercício 5 ⭐⭐⭐

Crie:

def categoria(idade):

Mas escreva usando o menor número possível de comparações.

Categorias:

Criança
Adolescente
Adulto
Idoso
"""
idade = int(input("Qual é a sua idade?\n"))

def categoria(idade):
    if idade >= 60:
        print("Idoso")
    elif idade >= 18:
        print("Adulto")
    elif idade >= 13:
        print("Adolescente")
    else:
        print("Criança")

categoria(idade)