"""
Exercícios
Exercício 1 ⭐

Crie uma função:

def apresentar(nome):

Ela deve imprimir:

Olá, Pedro!

Chamando:

apresentar("Pedro")
"""
nome = "Pedro"

def apresentar(nome):
    print (f"Olá {nome}!")

apresentar(nome)

"""Exercício 2 ⭐⭐

Crie:

def soma(a, b):

Ela deve imprimir a soma dos dois números.

Teste com:

soma(15, 30)

"""
a = 15
b = 30

def soma(a, b):
    return a + b

print(soma(a, b))

"""
Exercício 3 ⭐⭐⭐

Crie:

def cadastro(nome, idade):

Ela deve imprimir:

Nome: Pedro

Idade: 27
"""
idade = 27

def cadastro(nome, idade):
    print(f"Nome: {nome}\nIdade: {idade}")

cadastro(nome, idade)

"""
Exercício 4 ⭐⭐⭐⭐

Crie:

def saudacao(nome="Visitante"):

Teste:

saudacao()

e

saudacao("Maria")
"""

def saudacao(nome="Visitante"):
    print(f"Olá {nome}!")

saudacao()
saudacao("Maria")

"""
Exercício 5 ⭐⭐⭐⭐⭐

Crie:

def multiplicar(a=1, b=1):

Ela deve imprimir:

a * b

Teste todas estas chamadas:

multiplicar()

multiplicar(5)

multiplicar(5, 10)

Tente prever o resultado de cada uma antes de executar.
"""

def multiplicar(a=1, b=1):
    print(a * b)

multiplicar()

multiplicar(5)

multiplicar(5, 10)