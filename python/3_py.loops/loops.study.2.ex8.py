"""
Exercício 8 ⭐⭐⭐⭐

Senha inválida

Peça uma senha.

Percorra todos os caracteres.

Se encontrar um espaço " ":

Mostre:

Senha inválida.

e interrompa imediatamente.

Caso termine o laço sem encontrar espaços:

Senha válida.

Conceitos: for, break e else.
"""
senha = input("Digite a sua senha:\n")

for car in senha:
    if car == " ":
            print("Senha inválida.")
            break
else:
    print("Senha válida.")