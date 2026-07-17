"""
Exercício 5 ⭐⭐⭐
Verificador de idade

Crie:

def categoria(idade):

Retorne:

Criança → até 12
Adolescente → 13 até 17
Adulto → 18 até 59
Idoso → 60+
"""
idade = int(input("Qual é a sua idade?\n"))

def categoria(idade):
    if idade >= 60:
        print("Idoso")
    elif idade < 60 and idade >= 18:
        print("Adulto")
    elif idade < 18 and idade >= 13:
        print("Adolescente")
    else:
        print("Criança")

categoria(idade)