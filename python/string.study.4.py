"""
Exercício 31 — Médio

Crie uma função chamada initials().

Ela recebe um nome completo.

Retorne apenas as iniciais em letras maiúsculas.
"""
namorada = "stephanie sousa ribeiro navarro"
amigo1 = "matheus yan monteiro dos santos almeida"
amigo2 = "arthur guimarães nascimento"
amigo3 = "matheus afonso sousa"

def initials(namorada):
    return namorada.capitalize()

print(initials(namorada))
print(initials(amigo1))
print(initials(amigo2))
print(initials(amigo3))

"""
Exercício 32 — Médio

Crie uma função chamada censor_word().

Ela recebe:

uma frase;
uma palavra proibida.

Substitua todas as ocorrências dessa palavra por "****".
"""

frase_pesada = "Matiuza, você é um bobo"

def censor_word(frase_pesada):
    return frase_pesada.replace("bobo", "****")

print(censor_word(frase_pesada))

"""
Exercício 33 — Médio

Crie uma função chamada count_word().

Ela recebe:

uma frase;
uma palavra.

Retorne quantas vezes essa palavra aparece.
"""
like = "Eu gosto de peixe, eu gosto de churrasco, eu gosto de tacadinha, eu gosto de paçoca"

def count_word(like):
    return like.count("gosto")

print(count_word(like))

"""
Exercício 34 — Difícil

Crie uma função chamada hide_email().

Ela recebe um e-mail.
"""
email1 = "littletephi@gmail.com"
email2 = "pedronichollas@gmail.com"
email3 = "matheusalmeida@gmail.com"

def hide_email(email1):
    arroba = email1.find("@")
    dominio = email1[arroba:]
    usuario = email1[:arroba]
    return "*" * len(usuario) + dominio

print(hide_email(email1))
print(hide_email(email2))
print(hide_email(email3))

"""
Exercício 35 — Difícil

Crie uma função chamada reverse_words().

Ela recebe uma frase.

Inverta cada palavra individualmente, mas mantenha a ordem das palavras.

Exemplo:
"""

def reverse_words(frase_pesada):
   frase_invertida = frase_pesada[::-1]
   frase_list = frase_invertida.split()
   list_reverse = frase_list[::-1]
   final = ' '.join(list_reverse)
   return final

print(reverse_words(frase_pesada))

"""
Exercício 36 — Difícil

Crie uma função chamada remove_duplicate_spaces().

Ela recebe uma frase.

Retorne a frase com apenas um espaço entre cada palavra.
"""
frase_espaçada = "Alanzão  é  gente  boa"

def remove_duplicate_spaces(frase_espaçada):
    return frase_espaçada.replace("  ", " ")

print(remove_duplicate_spaces(frase_espaçada))

"""
Exercício 37 — Difícil

Crie uma função chamada abbreviate_name().

Ela recebe um nome completo.

Exemplo:

Pedro futuro_dev Navarro dos Santos

Retorne:

Pedro N. N. dos Santos

Regras:

mantenha o primeiro nome;
mantenha o último sobrenome;
mantenha partículas como dos, da, de, do, das;
transforme apenas os nomes do meio em iniciais.
"""
futuro_dev = "Pedro Nichollas Navarro dos Santos "

def abbreviate_name(futuro_dev):
    corte = futuro_dev.replace("Nichollas", "N.")
    return corte.replace("Navarro", "N.")

print(abbreviate_name(futuro_dev))

"""
Exercício 38 — Difícil

Crie uma função chamada is_valid_username().

Ela recebe uma string.

Um nome de usuário é válido quando:

possui pelo menos 5 caracteres;
possui apenas letras e números;
começa com uma letra.

Retorne True ou False.
"""
user1 = "Pedrokka4"
user2 = "Vicarious762"
user3 = "osso"

def is_valid_username(user1):
    if len(user1) >= 5:
        if user1.isalnum() == True:
            return True
    return False

print(is_valid_username(user1))
print(is_valid_username(user2))
print(is_valid_username(user3))

"""
Exercício 39 — Muito Difícil

Crie uma função chamada title_case().

Ela recebe uma frase.

Converta para um formato de título.

Mas as seguintes palavras não devem ficar com inicial maiúscula, exceto quando forem a primeira palavra da frase:

de
da
do
das
dos
e

Exemplo:

Entrada:

o senhor dos anéis e o retorno do rei

Saída:

O Senhor dos Anéis e o Retorno do Rei
"""
livro_bom = "o senhor dos anéis e o retorno do rei"
livro_ruim = "o homem macaco que não tem alma e nem coração"
forbidden_capital_words = ["de", "da", "do", "das", "dos", "e", "o"] 

def title_case(livro_bom, forbidden_capital_words):
    txt = livro_bom.split()
    resultado = []
    is_first = True

    for palavra in txt:
        if palavra.lower() not in forbidden_capital_words or is_first:
            resultado.append(palavra.capitalize())
        else:
            resultado.append(palavra.lower())

        if is_first == True:
            is_first = False

    return ' '.join(resultado)

print(title_case(livro_bom, forbidden_capital_words))
print(title_case(livro_ruim, forbidden_capital_words))

#Exercício 39 resolvido dom ajuda de amigos.

"""
Exercício 40 — Muito Difícil

Crie uma função chamada password_strength().

Ela recebe uma senha.

Retorne uma das seguintes strings:

"Fraca"
"Média"
"Forte"

Regras:

Fraca

Menos de 8 caracteres.

Média

Pelo menos 8 caracteres.

E possui:

letras;
números.
Forte

Pelo menos 12 caracteres.

E possui:

letras;
números.

E contém pelo menos:

uma letra maiúscula;
uma letra minúscula.

Observação: resolva utilizando apenas os recursos de strings que você já aprendeu. Não utilize expressões regulares (re) nem bibliotecas externas.
"""
senha1 = "aGharThabLacKoPs3"
senha2 = "senhabunda"
senha3 = "menos8"
senha4 = "senh4media"

def password_strength(senha1):
    if len(senha1) >= 12:
        if senha1.isalnum() == True:
            for batatinha in senha1:
                if batatinha.isupper():
                    return "Forte"
                





