"""
🐍 Exercício 7 ⭐⭐⭐⭐

Crie:

def acessar_sistema(usuario, senha, ativo):

Primeiro verifique:

Usuário.

Depois:

Senha.

Depois:

Se a conta está ativa.

Mensagens possíveis:

Usuário inexistente
Senha incorreta
Conta inativa
Acesso permitido
"""
# Para tentar trazer um contexto melhor ao exercício, vou perguntar ao usuário há quantos meses atrás foi o seu último acesso, se meses > 6, usuário = inativo.
# Além disso, colocarei que os nomes de usuário sempre começam com '@', do contrário será inexistente.
# Por último, estou determinando que as senhas devem ser compostas apenas por números e que tenham apenas 6 caracteres.
# Tenho a opinião de que esse exercício carece de critérios para realização, por isso delimitei melhor.
usuario = input("Qual é o seu nome de usuário?\n")
senha = input("Digite a sua senha.\n")
ativo = int(input("Faz quantos meses que você acessou o sistema pela última vez?\n"))

def acessar_sistema(usuario, senha, ativo):
    if usuario.startswith("@"):
        if senha.isdigit() == True and len(senha) == 6:
            if ativo > 6:
                print("Usuário inativo.")
            else:
                print("Usuário ativo.")
        else:
            print("Senha incorreta.")
    else:
        print("Usuário inexistente")

acessar_sistema(usuario, senha, ativo)