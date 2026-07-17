"""
🐍 Exercício 6 ⭐⭐⭐⭐

Crie:

def calcular_desconto(vip, valor):

Regras:

Se for VIP:

acima de R$100
30%
caso contrário
20%

Se não for VIP:

acima de R$100
10%
caso contrário
Sem desconto
"""
vip = input("Você é vip?\n")
valor = int(input("Qual foi o valor da sua compra?\n"))

def calcular_desconto(vip, valor):
    if vip.lower() == "sim":
        if valor >= 100:
            print("Desconto de 30%.")
        else:
            print("Desconto de 20%.")
    else:
        if valor >= 100:
            print("Desconto de 10%.")
        else:
            print("Sem desconto.")

calcular_desconto(vip, valor)