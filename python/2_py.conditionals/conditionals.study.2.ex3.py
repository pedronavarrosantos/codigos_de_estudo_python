"""
Exercício 3 ⭐⭐
Verificador de e-mail

Crie:

def validar_email(email):

Um e-mail será considerado válido se:

possuir "@"
terminar com:
.com

Retorne:

"E-mail válido"

ou

"E-mail inválido"

💡 Dica: lembre-se de endswith() e do operador in.
"""
email = input("Digite o e-mail desejado.")

def validar_email(email):
    arbfind = email.find("@")
    if arbfind != -1 and email.endswith(".com"):
        print(f"{email} é um e-mail válido.")
    else:
        print(f"{email} não é um e-mail válido.")

validar_email(email)