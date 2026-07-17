"""
Exercício 8 ⭐⭐⭐⭐
Sistema de aprovação

Crie:

def resultado(media, faltas):

O aluno só será aprovado se:

média maior ou igual a 6

E

faltas menores ou iguais a 20.

Caso contrário:

Reprovado
"""
media = float(input("Qual foi a sua média?\n"))
faltas = int(input("Quantas faltas você teve?\n"))

def resultado(media, faltas):
    if media >= 6.0 and faltas <= 20:
        print("Aprovado")
    else:
        print("Reprovado")

resultado(media, faltas)