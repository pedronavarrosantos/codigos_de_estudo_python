"""
Exercício 3 ⭐⭐⭐

Crie:

def dobro(numero):

Dentro da função, crie uma variável chamada:

resultado

Guarde nela o dobro do número.

Depois retorne resultado.

Teste a função.
"""
numero  = 4

def dobro(numero):
    resultado = numero * 2

    return resultado

print(dobro(numero))

"""
Exercício 4 ⭐⭐⭐⭐

Crie:

idade = 27

Depois:

def aniversario():

Dentro da função crie uma variável chamada:

idade = 28

Imprima a idade dentro da função.

Depois da função, imprima novamente a variável global.

Observe a diferença.
"""
idade  = 27

def aniversario():
    idade = 28
    print(idade)

aniversario()
print(idade)

"""
Exercício 5 ⭐⭐⭐⭐⭐

Crie:

def media(a, b):

Dentro dela:

crie uma variável chamada resultado;
guarde a média nela;
retorne resultado.

Depois faça:

media1 = media(10, 20)

media2 = media(8, 14)

print(media1)

print(media2)
"""
def media(a, b):
    
    resultado = (a + b) / 2
    return resultado

media1 = media(10, 20)
media2 = media(8, 14)

print(media1)
print(media2)