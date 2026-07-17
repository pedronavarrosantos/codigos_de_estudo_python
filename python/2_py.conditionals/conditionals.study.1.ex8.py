"""
Exercício 8 ⭐⭐⭐⭐
Login

Crie:

def fazer_login(usuario, senha):

O acesso só deve ser permitido quando:

Usuário: admin
Senha: python123

Caso contrário:

"Login inválido"

Agora você precisará comparar duas strings ao mesmo tempo usando and.
"""
print("Digite o seu login")

usuario = input()

print("Digite a sua senha")

senha = input()

def fazer_login(usuario, senha):
    if (usuario == "admin") and (senha == "python123"):
        return "Acesso liberado"
    return "Login inválido"

print(fazer_login(usuario, senha))