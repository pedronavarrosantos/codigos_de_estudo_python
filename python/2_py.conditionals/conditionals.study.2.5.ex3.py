"""
🐍 Exercício 3 ⭐⭐

Crie:

def desconto(cadastrado, pontos):

Regras:

Primeiro verifique se é cadastrado.

Se não for:

Sem desconto

Se for:

Verifique os pontos.

100 pontos ou mais:
20% de desconto
Caso contrário:
5% de desconto
"""
cadastrado = input("Você é cadastrado?\n")
pontos = int(input("Quantos pontos você tem?\n"))

def desconto(cadastrado, pontos):
    if cadastrado.lower() == "sim":
        if pontos >= 100:\
            print ("Desconto de 20%")
        else:
            print ("Desconto de 5%")
    else:
        print ("Sem desconto.")

desconto(cadastrado, pontos)