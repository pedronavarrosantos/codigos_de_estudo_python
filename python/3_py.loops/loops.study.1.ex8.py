"""
Exercício 8 ⭐⭐⭐⭐
Encontrando um número

Peça ao usuário que digite números.

Se ele digitar o número 7, encerre imediatamente o programa utilizando break.

Antes disso, continue perguntando.

Exemplo:

Digite um número:
2

Digite um número:
15

Digite um número:
7

Número encontrado!
"""
num = int(input("Digite um número de 0 a 100 até adivinhar o certo.\n"))

if num == 101:
        print("Meu caro usuário, eu falei para você digitar 'UM NÚMERO ENTRE 0 E 100'... Desculpe ter me exaltado.")
        num = int(input("Digite outro número:"))
while num != 101:
    if num > 100:
        print("Meu caro usuário, eu falei para você digitar 'UM NÚMERO ENTRE 0 E 100'... Desculpe ter me exaltado.")
        num = int(input("Digite outro número:"))
    elif num > 7:
        print("Esse não é o número certo, tente um menor.")
        num = int(input("Digite outro número:"))
    elif num < 7:
        print("Esse não é o número certo, tente um maior.")
        num = int(input("Digite outro número:"))
    else:
        print("Parabéns, você acertou o número!!!")
        break