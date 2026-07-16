"""
Exercício 11 — Médio

Crie uma função chamada first_name().

Ela recebe um nome completo.

Retorne apenas o primeiro nome.
"""
full_name = "Pedro Nichollas Navarro dos Santos"

def first_name(full_name):
   names = full_name.split()
   return names[0]

print(first_name(full_name))

"""
Solução alternativa do exercício 11 com menos linhas de código:
"""
def alt_first_name(full_name):
   return full_name.split()[0]

print(alt_first_name(full_name))

"""
Exercício 12 — Médio

Crie uma função chamada last_word().

Ela recebe uma frase.

Retorne apenas a última palavra.
"""
phrase= "My word will be the last"

def last_word(phrase):
    return phrase.split()[-1]

print(last_word(phrase))

"""
Exercício 13 — Médio

Crie uma função chamada join_with_dash().

Ela recebe uma lista de palavras.

Retorne todas elas separadas por hífen (-).
"""
full_name_list = ["Pedro", "Nichollas", "Navarro", "dos", "Santos"]
phrase_list = ["My", "word", "will", "be", "the", "last"]

def join_with_dash(full_name_list):
    return "-".join(full_name_list)

print(join_with_dash(full_name_list))
print(join_with_dash(phrase_list))

"""
Exercício 14 — Médio

Crie uma função chamada csv_line().

Ela recebe uma lista de palavras.

Retorne uma única string separando cada elemento por vírgula seguida de espaço.
"""
def csv_line(full_name_list):
    return ", ".join(full_name_list)

print(csv_line(full_name_list))
print(csv_line(phrase_list))

"""
Exercício 15 — Médio

Crie uma função chamada clean_spaces().

Ela recebe uma string.

Retorne a mesma string sem espaços no começo nem no fim.
"""
exercise15v = "  .come.closer.  "
def clean_spaces(exercise15v):
    return exercise15v.strip()

print(clean_spaces(exercise15v))

"""
Exercício 16 — Médio

Crie uma função chamada remove_dot().

Ela recebe uma palavra que termina com ponto (.).

Retorne a palavra sem o ponto final.
"""
exercise16v = "no dots here."

def remove_dot(exercise16v):
    return exercise16v.rstrip(".")

print(remove_dot(exercise16v))

"""
DESAFIO

Crie uma função chamada the_dot_slayer().

Remova todos os pontos da seguinte string: anti_dot = ".I'm dot.phobic."

Retorne exatamente a seguinte string: "I'm dotphobic".
"""
anti_dot = ".I'm dot.phobic."

def the_dot_slayer(anti_dot):
    first_dot_slay = anti_dot.lstrip(".")
    second_dot_slay = first_dot_slay.rstrip(".")
    final_dot_slay = second_dot_slay[:7] + second_dot_slay[8:]
    return final_dot_slay

print(the_dot_slayer(anti_dot))

"""
Exercício 17 — Médio

Crie uma função chamada starts_with_python().

Ela recebe uma string.

Retorne True se ela começar com "Python".

Caso contrário, retorne False.
"""
python_affirmation = "Python is one of the most used programming languages in the world"
JavaScript_affirmation = "JavaScript is one of the most used programming languages in the world"

def starts_with_python(python_affirmation):
    return python_affirmation.startswith("Python")

print(starts_with_python(python_affirmation))
print(starts_with_python(JavaScript_affirmation))

"""
Exercício 18 — Médio

Crie uma função chamada remove_ing().

Ela recebe uma palavra terminada em "ing".

Retorne essa palavra sem o sufixo.

Exemplo:
"""
sad_day_for_Brazil = "In July 5th of 2026, Brazil was eliminated from the FIFA Soccer World Cup losing to Norway, the match score was Brazil 0 and Norway 2. The two goals were from the player which the last name is Haaland and the first name is Erling"

def remove_ing(sad_day_for_Brazil):
    return sad_day_for_Brazil.removesuffix("ing")

print(remove_ing(sad_day_for_Brazil))
print(remove_ing(JavaScript_affirmation))

"""
Exercício 19 — Fácil

Crie uma função chamada change_color().

Ela recebe uma frase.

Troque todas as ocorrências da palavra "azul" por "verde".
"""
falsos_azuis = "As plantas têm com azul, esmeraldas têm cor azul, jades têm cor azul, os carros estão liberados para avançar o sinal quando a sua cor for azul"

def change_color(falsos_azuis):
    return falsos_azuis.replace("azul", "verde")

print(change_color(falsos_azuis))

"""
DESAFIO 2

Crie uma função chamada the_dot_slayer_reborn().

Remova todos os pontos da seguinte string: anti_dot = ".I'm dot.phobic."

Retorne exatamente a seguinte string: "I'm dotphobic".

Dessa vez faça isso usando replace()
"""

def the_dot_slayer_reborn(anti_dot):
    return anti_dot.replace(".", "")

print(the_dot_slayer_reborn(anti_dot))

"""
Exercício 20 — Médio

Crie uma função chamada snake_case().

Ela recebe uma frase.

Substitua todos os espaços por _.
"""
hideo_k = "Metal Gear Solid Snake"

def snake_case(hideo_k):
    return hideo_k.replace(" ", "_")

print(snake_case(hideo_k))