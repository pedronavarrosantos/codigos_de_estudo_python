"""
Exercício 1 ⭐

Crie:

def calculos(a, b):

Ela deve retornar:

soma
subtração

Depois faça:

soma, subtracao = calculos(20, 5)

print(soma)
print(subtracao)
"""
a = 4
b = 8

def calculos(a, b):
    return a + b, a - b

print(calculos(a, b))

"""
Exercício 2 ⭐⭐

Crie:

def metade(numero)

Depois:

def metade_do_dobro(numero)

Ela deve usar a função metade().
"""
numero = 42

def metade(numero):
    return numero / 2

print(metade(numero))

def metade_do_dobro(numero):
    dobro = numero * 2
    return metade(dobro)

print(metade_do_dobro(numero))

"""
Exercício 3 ⭐⭐⭐

Crie:

def linha():

Ela deve imprimir:

==============================

Depois use essa função pelo menos cinco vezes em um pequeno programa.
"""
def linha():
    print("==============================")

print("Texto ex3")
linha()
print("Texto ex3")
linha()
print("Texto ex3")
linha()
print("Texto ex3")
linha()
print("Texto ex3")
linha()