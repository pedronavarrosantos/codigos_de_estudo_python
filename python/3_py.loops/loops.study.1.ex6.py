"""
Exercício 6 ⭐⭐⭐
Senha

Peça ao usuário que digite uma senha.

Enquanto a senha for diferente de:

python123

continue pedindo novamente.

Quando acertar, exiba:

Acesso permitido.

Conceitos: while.
"""
senha = input("Digite a sua senha\n")
tentativas = 0

while senha != "python123":
    print("Tente novamente.")
    senha = input("Digite a sua senha\n")
else:
    print("Acesso permitido") 