"""
Exercício 1 ⭐

Crie um arquivo chamado:

teste.txt

Escreva nele:

Olá mundo!
"""
with open("filesteste.txt", "w") as file:
    file.write("Olá mundo!\n")

"""
Exercício 2 ⭐⭐

Escreva três linhas:

Pedro
Maria
Carlos
"""
with open("filesteste.txt", "a") as file:
    file.write("Pedro\n")
    file.write("Maria\n")
    file.write("Carlos\n")

"""
Exercício 3 ⭐⭐⭐

Acrescente mais duas linhas ao arquivo:

Stephanie
Matheus
"""
with open("filesteste.txt", "a") as file:
    file.write("Stephanie\n")
    file.write("Matheus\n")

"""
Exercício 4 ⭐⭐⭐⭐

Leia o arquivo inteiro usando:

read()

e imprima seu conteúdo.
"""

with open("filesteste.txt", "r") as file:
    print(file.read())