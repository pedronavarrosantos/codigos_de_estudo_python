"""
Exercícios
Exercício 1 ⭐

Crie:

def quadrado(numero):

Ela deve retornar o quadrado do número.

Teste:

print(quadrado(5))
"""
numero  = 5

def quadrado(numero):
    return numero ** 2

print(quadrado(numero))

"""
Exercício 2 ⭐⭐

Crie:

def maior(a, b):

Ela deve retornar o maior dos dois números.

Teste:

print(maior(8, 15))
"""
a = 8
b = 15

def maior(a, b):
    if a > b:
        return a
    return b

print(maior(a, b))

"""
Exercício 3 ⭐⭐⭐

Crie:

def par(numero):

Ela deve retornar:

True

se o número for par.

Caso contrário:

False

Teste com vários números.
"""
num0 = 19
num1 = 13
num2 = 72
num3 = 6

def par(num0):
    return num0 % 2 == 0
    

print(par(num0))
print(par(num1))
print(par(num2))
print(par(num3))

"""
Exercício 4 ⭐⭐⭐⭐

Crie:

def media(a, b, c):

Ela deve retornar a média dos três números.

Depois faça:

resultado = media(7, 8, 9)

print(resultado)
"""
c = 9

def media(a, b, c):
    return (a + b + c) / 3

print(media(a, b, c))
print(media(num0, num2, num3))

"""
Exercício 5 ⭐⭐⭐⭐⭐

Crie duas funções.

A primeira:

def soma(a, b):

retorna a soma.

A segunda:

def triplo(numero):

retorna o triplo.

Agora faça:

print(triplo(soma(10, 20)))

Sem fazer contas manualmente.
"""
def soma(a, b):
    return a + b

def triplo(numero):
    return numero * 3

print(triplo(numero))
print(soma(a, b))
print(triplo(soma(a, b)))