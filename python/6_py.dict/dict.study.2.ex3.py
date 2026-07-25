"""
Exercício 1 ⭐

Crie:

alunos = [
    {"nome": "Pedro", "idade": 27},
    {"nome": "Maria", "idade": 22},
    {"nome": "Carlos", "idade": 31}
]

Peça um nome ao usuário.

Se existir, mostre apenas a idade.

Caso contrário:

Aluno não encontrado.
"""
alunos = [
    {"nome": "Pedro", "idade": 27},
    {"nome": "Maria", "idade": 22},
    {"nome": "Carlos", "idade": 31}
]

aluno = input("Digite o nome de um aluno para saber a idade dele.\n")

for key in alunos:
    if key["nome"] == aluno:
        print(f"O(a) {key['nome']} tem {key['idade']} anos.")
        break
    else:
        print("Nome não encontrado")
        break