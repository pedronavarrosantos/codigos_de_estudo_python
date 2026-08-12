"""
⭐⭐ Exercício 2

Peça:

Digite sua idade:

Converta para int.

Se funcionar:

Idade registrada: 27

Se não funcionar:

Digite apenas números inteiros.
"""
while True:
    idade = input("Digite a sua idade:\n")
    try:
        num_idade = int(idade)
        break
    except ValueError:
        print(f"{idade} é um valor inválido, digite apenas números inteiros.")

print(f"A sua idade é {num_idade}.")