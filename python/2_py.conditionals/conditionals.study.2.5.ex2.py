"""
🐍 Exercício 2 ⭐⭐

Crie:

def login(usuario, senha):

Usuário correto:

admin

Senha correta:

python123

Retorne:

Login realizado

ou

Senha incorreta

ou

Usuário inexistente

Use obrigatoriamente um if dentro de outro.
"""
usuario = input()
senha = input()

def login(usuario, senha):
    if usuario == "admin":
        if senha == "python123":
            return "Login realizado."
        return "Senha incorreta."
    return "Usuário inexistente."

print(login(usuario, senha))