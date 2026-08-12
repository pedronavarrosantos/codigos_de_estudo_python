"""
⭐ Exercício 1 — ZeroDivisionError

Peça dois números inteiros ao usuário e divida o primeiro pelo segundo.

Se o segundo número for 0, mostre:

Não é possível dividir por zero.

Utilize try/except.
"""
print("== Vamos dividir um número pelo outro. Escolha apenas números inteiros. ==")

while True:
    num_1 = input("== Digite o numerador:\n")
    try:
        num_1 = int(num_1)
        break
    except ValueError:
        print(f"O valor {num_1} é inválido, digite um número inteiro")
        
while True:
    num_2 = input("== Digite o denominador:\n")
    try:
        num_2 = int(num_2)
        divisao = num_1 / num_2

        print(f"O resultado da divisão é {divisao}")
        break
    except ValueError:
        print(f"O valor {num_2} é inválido, digite um número inteiro")
    except ZeroDivisionError:
        print("Não é possível dividir um número por zero.")
    