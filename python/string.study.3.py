"""
Exercício 21 — Fácil

Crie uma função chamada shout().

Ela recebe uma frase.

Retorne a frase completamente em letras maiúsculas.
"""
fala_baixo = "eu vou falar alto, não quero saber!"

def shout(fala_baixo):
    return fala_baixo.upper()

print(shout(fala_baixo))

"""
Exercício 22 — Fácil

Crie uma função chamada book_title().

Ela recebe um título escrito totalmente em minúsculas.

Retorne esse título utilizando a convenção de títulos (title()).
"""
book = "matiuza, solteiro, lonso e chibanga contra o lich das maldivas."

def book_title(book):
    return book.title()

print(book_title(book))

"""
Exercício 23 — Médio

Crie uma função chamada contains_python().

Ela recebe uma frase.

Retorne True se a palavra "Python" aparecer na frase.

Caso contrário, retorne False.

Utilize find().
"""
python_facts = "Python: linguagem de tipagem dinâmica, criada por Guido van Rossum em 1991, é ótima para IA, web e automação. 🐍 Python usa indentação em vez de chaves '{}', tem tipagem duck typing e o (import this) resume sua filosofia. 🐍 Python é interpretado (não compilado) e possui um vasto ecossistema de bibliotecas via PyPI, com mais de 500 mil pacotes. 🐍"

def contains_python(python_facts):
    if python_facts.find("Python") != -1:
        return True
    return False

print(contains_python(python_facts))
print(contains_python(book))
print(contains_python(fala_baixo))

"""
Exercício 24 — Médio

Crie uma função chamada count_spaces().

Ela recebe uma frase.

Retorne quantos espaços existem nela.
"""
def count_spaces(book):
    return book.count(" ")

print(count_spaces(book))
print(count_spaces(fala_baixo))

"""
Exercício 25 — Médio

Crie uma função chamada only_letters().

Ela recebe uma string.

Retorne True se ela possuir apenas letras.
"""
letras = "palavra"
letras_espaço = "p a l a v r a"

def only_letters(book):
    return book.isalpha()

print(only_letters(book))
print(only_letters(letras))
print(only_letters(letras_espaço))

"""
Crie uma função chamada is_number().

Ela recebe uma string.

Retorne True caso ela represente apenas números.
"""
num = "123456"
num_espaço = "1 2 3 4 5 6"

def is_number(num):
    return num.isdigit()

print(is_number(num))
print(is_number(num_espaço))

"""
Exercício 27 — Médio

Crie uma função chamada reverse_word().

Ela recebe uma palavra.

Retorne a palavra invertida.
"""
def reverse_word(num):
    return num[::-1]

print(reverse_word(num))
print(reverse_word(book))

"""
Exercício 28 — Médio

Crie uma função chamada is_palindrome().

Ela recebe uma palavra.

Retorne True caso ela seja um palíndromo.

Um palíndromo é uma palavra que pode ser lida normalmente ou de trás para frente.
"""
palindrome = "osso"
reverse_word(palindrome)


def is_palindrome(palindrome):
    if palindrome == reverse_word(palindrome):
        return True
    return False

print(is_palindrome(palindrome))

"""
Exercício 29 — Difícil

Crie uma função chamada normalize_name().

Ela recebe uma string.

Que deve pode conter:

espaços no começo;
espaços no fim;
letras maiúsculas;
letras minúsculas.

Retorne a string:

sem espaços extras;
totalmente em minúsculas.
"""
namorada = "  STEPHANIE Sousa riBeIro navarro  "

def normalize_name(namorada):
    noiva = namorada.strip()
    return noiva.lower()

print(normalize_name(namorada))

"""
Exercício 30 — Difícil

Crie uma função chamada create_username().

Ela recebe um nome completo.

Exemplo:

Pedro Nichollas Santos

A função deve retornar:

pedro_nichollas_santos

Regras:

remover espaços do início e do fim;
transformar tudo em minúsculas;
trocar espaços por _.
"""
def create_username(namorada):
    noiva = namorada.strip()
    esposa = noiva.lower()
    return esposa.replace(" ", "_")

print(create_username(namorada))