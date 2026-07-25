"""
Exercício 2 ⭐⭐

Utilize a mesma lista.

Peça um nome.

Caso exista:

Pedro encontrado!

Caso contrário:

Pedro não encontrado.

(utilize uma variável encontrou)
"""
alunos = [
    {"nome": "Pedro", "idade": 27},
    {"nome": "Maria", "idade": 22},
    {"nome": "Carlos", "idade": 31}
]

aluno = input("Digite o nome de um aluno para saber a idade dele.\n")

found = False

for key in alunos:
    if aluno == key["nome"]:
        print(f"{key["nome"]} encontrado.")
        found = True
        break
if not found:
    print(f"{aluno} não encontrado(a).")
