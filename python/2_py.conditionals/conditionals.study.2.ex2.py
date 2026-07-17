"""
Exercício 2 ⭐
Ano bissexto simplificado

Crie:

def divisivel_por_4(numero):

Retorne:

"Divisível"
"Não divisível"

se o número for divisível por 4.

Não use ainda as regras completas do ano bissexto.
"""
numero = int(input("Digite um ano."))

def divisivel_por_4(numero):
    if numero % 4 == 0:
        print(f"O ano {numero} é um ano bissexto.")
    else:
        print(f"O ano {numero} não é um ano bissexto.")

divisivel_por_4(numero)