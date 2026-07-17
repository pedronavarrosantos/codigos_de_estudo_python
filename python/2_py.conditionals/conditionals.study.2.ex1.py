"""
Exercício 1 ⭐
Número par ou ímpar

Crie:

def par_ou_impar(numero):

Retorne:

"Par"
"Ímpar"

💡 Dica: lembre-se do operador %.
"""
numero = int(input("Digite um número."))

def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} é um número par.")
    else:
        print (f"{numero} não é um número par.")

par_ou_impar(numero)