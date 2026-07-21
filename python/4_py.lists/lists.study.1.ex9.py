"""
Exercício 1 ⭐

Crie:

animais = ["Cachorro", "Gato", "Peixe"]

Pergunte um animal ao usuário.

Informe se ele está ou não na lista utilizando in.
"""
animais = ["Cachorro", "Gato", "Peixe"]
animal = input("Digite um animal.\n")

if animal in animais:
    print(f"O {animal} está na lista.")
else:
    print("O animal informado não está na lista.")