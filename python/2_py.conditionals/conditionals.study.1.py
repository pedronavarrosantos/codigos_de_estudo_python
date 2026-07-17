"""
Exercício 1 — Maioridade

Crie um programa que:

Receba uma idade
Verifique se a pessoa é maior de idade
Mostre:
Maior de idade

ou

Menor de idade
"""

maior1 = 19
maior2 = 73
menor1 = 4
menor2 = 16

def is_maior(maior1):
    if maior1 >= 18:
        return "Maior de idade"
    return "Menor de idade"

print(is_maior(maior1))
print(is_maior(maior2))
print(is_maior(menor1))
print(is_maior(menor2))

"""
🐍 Missão 2 — Classificador de nota

Crie uma função:

def verificar_nota(nota):

Ela deve:

retornar "Aprovado" se a nota for maior ou igual a 6
retornar "Reprovado" caso contrário
"""
nota1 = 9
nota2 = 5.7
nota3 = 6.1
nota4 = 8

def verificar_nota(nota1):
    if nota1 >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

print(verificar_nota(nota1))

"""
🔥 Missão 3 — Sistema de classificação

Você vai conhecer o próximo conceito:

elif

Imagine um sistema de notas:

Nota 9 ou maior → "Excelente"
Nota entre 7 e 8.9 → "Bom"
Nota entre 6 e 6.9 → "Regular"
Menor que 6 → "Reprovado"
"""

def rotulo_nota(nota1):
    if nota1 >= 9:
        return "Excelente"
    elif nota1 >= 7:
        return "Bom"
    elif nota1 >= 6:
        return "Regular"
    else:
        return "Reprovado"

print(rotulo_nota(nota1))
print(rotulo_nota(nota2))
print(rotulo_nota(nota3))
print(rotulo_nota(nota4))

"""
Exercício 1 ⭐

Crie uma função chamada:

def numero_positivo(numero):

Ela deve retornar:

"Positivo" se o número for maior que zero.
"Zero" se o número for igual a zero.
"Negativo" se o número for menor que zero.
"""
un_num = -3
zero = 0
def numero_positivo(un_num):
    if un_num > 0:
        return "Positivo"
    elif un_num < 0:
        return "Negativo"
    else:
        return "Zero"

print(numero_positivo(un_num))
print(numero_positivo(zero))
print(numero_positivo(nota1))

"""
Exercício 2 ⭐
Maioridade

Crie:

def verificar_idade(idade):

Retorne:

"Maior de idade"
"Menor de idade"
"""

def verificar_idade(maior1):
    if maior1 >= 18:
        return "Maior de idade"
    return "Menor de idade"

print(verificar_idade(maior1))
print(verificar_idade(menor1))

"""
Exercício 3 ⭐⭐
Senha

Crie:

def verificar_senha(senha):

Se a senha for exatamente:

python123

retorne:

"Acesso permitido"

Caso contrário:

"Acesso negado"
"""
senha_ex3 = "python123"
senha_ex3_2 = "JaVaScRiPt"

def verificar_senha(senha_ex3):
    if senha_ex3 == "python123":
        return "Acesso permitido"
    else:
        return "Acesso negado"

print (verificar_senha(senha_ex3))
print (verificar_senha(senha_ex3_2))

"""
Exercício 4 ⭐⭐
Nome vazio

Crie:

def validar_nome(nome):

Se, após remover os espaços das extremidades (strip()), o nome estiver vazio, retorne:

"Nome inválido"

Caso contrário:

"Nome válido"

Primeiro exercício misturando Strings + Condicionais.
"""

nome1 = "  "
nome2 = "  Pedro Nichollas  "
nome3 = "  Stephanie Navarro  "
nome4 = " Matheus Solteiro "

def validar_nome(nome1):
    if len(nome1.strip()) == 0:
        return "Nome inválido"
    else: 
        return "Nome Válido"

print(validar_nome(nome1))
print(validar_nome(nome2))
print(validar_nome(nome3))
print(validar_nome(nome4))

"""
Exercício 5 ⭐⭐⭐
Classificação de notas

Crie:

def classificar_nota(nota):

Retorne:

"Excelente" (9 ou mais)
"Bom" (7 até 8.9)
"Regular" (6 até 6.9)
"Reprovado" (abaixo de 6)
"""
def classificar_nota(nota1):
    if nota1 >= 9:
        return "Excelente"
    elif nota1 >= 7:
        return "Bom"
    elif nota1 >= 6:
        return "Regular"
    else:
        return "Reprovado"

print(rotulo_nota(nota1))
print(rotulo_nota(nota2))
print(rotulo_nota(nota3))
print(rotulo_nota(nota4))

"""
Exercício 6 ⭐⭐⭐
Sistema de acesso

Crie:

def entrar(idade, ingresso):

A pessoa entra somente se:

possuir ingresso;
tiver pelo menos 18 anos.

Retorne:

"Entrada liberada"

ou

"Entrada negada"
"""

idade1 = 12
ingresso1 = True
idade2 = 16
ingresso2 = False
idade3 = 22
ingresso3 = False
idade4 = 23
ingresso4 = True

def entrar(idade1, ingresso1):
    if idade1 >= 18 and ingresso1 == True:
        return "Entrada liberada"
    return "Entrada negada"

print(entrar(idade1, ingresso1))
print(entrar(idade2, ingresso2))
print(entrar(idade3, ingresso3))
print(entrar(idade4, ingresso4))