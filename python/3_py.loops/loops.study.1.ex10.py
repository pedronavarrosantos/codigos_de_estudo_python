"""
Exercício 10 👑 — Chefe da Lista
Sistema de Login

O programa deve pedir o usuário e a senha até que ambos estejam corretos.

Usuário:

admin

Senha:

python123

Se o usuário errar qualquer um dos dois, mostre:

Login inválido.

e peça novamente.

Quando ambos estiverem corretos, exiba:

Login realizado com sucesso!
"""
while True:
    usuario = input("Digite o seu nome de usuário:\n")
    if usuario != "admin":
        print("Login inválido.")
        continue
    senha = input("Digite a sua senha:\n")
    if senha != "python123":
            print("Senha inválida.")
            continue    
    print("Login efetuado.")
    break