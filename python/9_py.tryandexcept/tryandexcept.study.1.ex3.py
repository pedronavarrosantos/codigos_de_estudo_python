"""
⭐⭐⭐ Exercício 3

Faça um programa que continue pedindo uma idade até o usuário fornecer um número válido.

Exemplo:

Digite sua idade: abc
Digite apenas números inteiros.

Digite sua idade: Pedro
Digite apenas números inteiros.

Digite sua idade: 27

Idade registrada: 27

Obrigatório: use while, try, except e break.
"""
while True:
    idade = input("Digite a sua idade:\n")
    try:
        num_idade = int(idade)
        break
    except ValueError:
        print(f"{idade} é um valor inválido, digite apenas números inteiros.")

print(f"A sua idade é {num_idade}.")