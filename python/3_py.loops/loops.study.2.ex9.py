"""
Exercício 9 ⭐⭐⭐⭐⭐

Quantidade de letras e números

Peça um username.

Exemplo:

Pedro123

Conte separadamente:

letras;
números.

Saída:

Letras: 5
Números: 3

Conceitos: isalpha(), isdigit(), acumuladores.
"""
username = input("Por favor, escolha um nome de usuário:\n")
lc = 0
nc = 0

for car in username:
    if car.isalpha():
        lc += 1
    elif car.isdigit():
        nc += 1

print(f"O nome de usuário poassui {lc} letras e {nc} números.")