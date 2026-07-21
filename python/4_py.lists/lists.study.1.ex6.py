"""
Exercício 1 ⭐

Crie:

frutas = ["Maçã", "Banana", "Uva"]

Mostre a posição de "Banana".
"""
frutas = ["Maçã", "Banana", "Uva"]

print(frutas.index("Banana"))

"""
Exercício 2 ⭐⭐

Crie:

cores = ["Azul", "Verde", "Amarelo", "Vermelho"]

Peça uma cor ao usuário.

Se ela existir, mostre sua posição.
Caso contrário, mostre:
Cor não encontrada.
"""
cores = ["Azul", "Verde", "Amarelo", "Vermelho"]
cor = input("Escolha uma cor:\n")

if cor in cores:
    print(cores.index(cor))
else:
    print("Cor não encontrada")