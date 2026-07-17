"""
Exercício 6 ⭐⭐⭐
Senha forte

Crie:

def senha_forte(senha):

A senha será considerada forte se:

possuir pelo menos 8 caracteres;
começar com letra.

Caso contrário:

Senha fraca

Atenção: como você ainda não aprendeu loops, não precisa verificar todos os caracteres. Basta analisar o primeiro usando indexação (senha[0]) ou outro método que você conheça.
"""
senha = input("Digite a sua senha.\n")

def senha_forte(senha):
    if len(senha) >= 8 and senha[0].isalpha():
        print("Senha forte.")
    else:
        print("Senha fraca")
 
senha_forte(senha)

# Bug detectado: Ao executar o código, não colocar nada no input e em seguida executar o código novamente sucessivas vezes, o terminal alterna o retorno da senha como senha forte e senha fraca.