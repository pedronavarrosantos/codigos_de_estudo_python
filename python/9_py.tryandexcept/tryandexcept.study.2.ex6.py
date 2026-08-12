"""
⭐⭐⭐⭐⭐⭐ Exercício 6 — Vários erros

Faça uma calculadora que:

peça dois números;
converta ambos para float;
divida o primeiro pelo segundo.

Trate separadamente:

ValueError;
ZeroDivisionError.

Cada erro deve apresentar uma mensagem diferente.
"""
print("Vamos dividir dois números.")

while True:
    num_1 = input("Digite o numerador:\n")
    num_2 = input("Digite o denominador:\n")

    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
    except ValueError:
        print("Algum ou os valores inseridos são inválidos, digite um número inteiro ou decimal.")

    try:
        produto = num_1 / num_2
        print(produto)
        break
    except TypeError:
        print("Esse campo não aceita textos, digite apenas números inteiros ou decimais.")
    except ZeroDivisionError:
        print("Não é possível dividir um número por zero.")
    
    
