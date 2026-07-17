"""
Exercício 4 ⭐⭐
Nome de usuário

Crie:

def usuario_admin(usuario):

Se o nome do usuário for exatamente:

admin

retorne

Administrador

Caso contrário

Usuário comum

Mas aceite:

Admin
ADMIN
AdMiN

💡 Dica: você aprendeu lower().
"""
usuario = input("Digite o seu nome de usuário.\n")

def usuario_admin(usuario):
    ad = "admin"
    
    if usuario.lower() == ad:
        print("Administrador")
    else: 
        print("Usuário comum")

usuario_admin(usuario)
   