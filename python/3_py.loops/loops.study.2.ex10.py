"""
👑 Exercício 10 — Chefe da Lista

Validador de senha

Peça uma senha.

Ela será considerada válida somente se:

possuir pelo menos 8 caracteres;
possuir pelo menos uma letra;
possuir pelo menos um número;
não possuir espaços.

Retorne:

Senha válida.

ou

Senha inválida.
💡 Dicas

Você ainda não aprendeu listas nem expressões regulares, então resolva apenas com os conhecimentos que possui:

for
if
break
continue
isalpha()
isdigit()
len()
"""
print("A sua senha deve conter pelo menos 8 caracteres, pelo menos uma letra, pelo menos um número e não pode ter espaços vazios.")

senha = input("Por favor, escolha a sua senha:\n")



def validador_passwords(senha):
    has_digit = False
    has_letter = False
    dont_space = False

    for car in senha:
        if car.isdigit():
            has_digit = True
        if car.isalpha():
            has_letter = True
        if car == " ":
            dont_space = True
    
    if has_digit and has_letter and not dont_space and len(senha) >= 8:
        print("Senha válida.")
    else:
        print("Senha inválida.")

        if not has_digit:
            print("Deve conter pelo menos um número.")
        if not has_letter:
            print("Deve conter pelo menos uma letra.")
        if dont_space:
            print("Não pode conter espaços vazios.")
        if len(senha) < 8:
            print("Deve conter pelo menos 8 caracteres.")

validador_passwords(senha)