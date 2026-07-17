"""
Exercício 7 ⭐⭐⭐⭐
Entrada VIP

Crie:

def entrar_vip(idade, vip):

Uma pessoa pode entrar se:

for VIP

OU

possuir pelo menos 18 anos.

Retorne:

Entrada permitida

ou

Entrada negada
"""
idade = int(input("Qual é a sua idade?\n"))
vip = input("Você é vip?\n")


def entrar_vip(idade, vip):
    yess = "sim"
    iam = "sou"

    if vip.lower() == yess or vip.lower() == iam or idade >= 18:
        print ("Entrada permitida")
    else:
        print("Entrada negada")

entrar_vip(idade, vip)