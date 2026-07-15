"""Exercício 1 — Fácil

Crie uma função chamada say_hello().

Ela recebe um parâmetro chamado name.

Retorne exatamente a frase:

Olá, Pedro!
"""
name = "Pedro"

def say_hello(name):
    return (f"Olá, {name}!")

print(say_hello(name))

"""
Exercício 2 — Fácil

Crie uma função chamada favorite_language().

Ela recebe um parâmetro chamado language.

Retorne:

Minha linguagem favorita é Python.
"""
l = "Python"
js = "JavaScript"

def favorite_language(js):
    return (f"Minha linguagem favorita é o {js}")

print(favorite_language(l))
print(favorite_language(js))
"""
Exercício 3 — Fácil

Crie uma função chamada full_name().

Ela recebe:

first_name
last_name

Retorne o nome completo separado por um espaço.
"""
m = "Matiuza"
cm = "Cunha-Maia"

def full_name(m, cm):
    completo = m + " " + cm
    return (completo)

print(full_name(m, cm))
"""
Exercício 4 — Fácil

Crie uma função chamada repeat_word().

Ela recebe uma palavra.

Retorne essa palavra repetida duas vezes.
"""
pew = "BANG!!!"

def repeat_word(pew):
    tiroteio = pew + " " + pew
    return (tiroteio)

print(repeat_word(pew))
"""
Exercício 5 — Fácil

Crie uma função chamada count_letters().

Ela recebe uma palavra.

Retorne quantos caracteres essa palavra possui.
"""
def count_letters(pew):
    return (len(pew))

print(count_letters(name))
print(count_letters(l))
print(count_letters(js))
print(count_letters(m))
print(count_letters(cm))
print(count_letters(pew))
"""
Exercício 6 — Fácil

Crie uma função chamada message_size().

Ela recebe uma frase.

Retorne exatamente:

Sua mensagem possui X caracteres.
"""
def message_size(name):
    num_spaces = len(name)
    return (f"Sua mensagem possui {num_spaces} caracteres")

print(message_size(name))
print(message_size(l))
print(message_size(js))
"""
Exercício 7 — Fácil

Crie uma função chamada first_letter().

Ela recebe uma palavra.

Retorne apenas a primeira letra.
"""
def first_letter(l):
    return l[0]

print(first_letter(l))
print(first_letter(name))
print(first_letter(js))
"""
Exercício 8 — Fácil

Crie uma função chamada last_letter().

Ela recebe uma palavra.

Retorne apenas a última letra.
"""
def last_letter(l):
    return l[-1]

print(last_letter(l))
print(last_letter(name))
"""
Exercício 9 — Fácil

Crie uma função chamada first_three_letters().

Ela recebe uma palavra.

Retorne apenas os três primeiros caracteres.
"""
def first_three_letters(l):
    return l[:3]

print(first_three_letters(l))
print(first_three_letters(js))
print(first_three_letters(name))
"""
Exercício 10 — Fácil

Crie uma função chamada remove_last_letter().

Ela recebe uma palavra.

Retorne essa palavra sem o último caractere.
"""
def remove_last_letter(l):
    return l[:-1]

print(remove_last_letter(l))
print(remove_last_letter(name))
print(remove_last_letter(js))
print(remove_last_letter(pew))
print(remove_last_letter(m))
print(remove_last_letter(cm))