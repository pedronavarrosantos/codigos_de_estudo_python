"""
⭐⭐⭐ Exercício 3 — IndexError

Crie:

alunos = ["Pedro", "Maria", "Carlos"]

Peça ao usuário um índice e mostre o aluno correspondente.

Se o índice não existir:

Aluno não encontrado nessa posição.

Use try/except.
"""
alunos = ["Pedro", "Maria", "Carlos"]

while True:
    position = input("Digite a posição para sera acessada dentro da lista:\n")

    try:
        print(alunos[int(position)])
    except ValueError:
        print(f"O valor {position} é inválido, digite um número inteiro")
    except IndexError:
        print("Aluno não encontrado nessa posição.")
    