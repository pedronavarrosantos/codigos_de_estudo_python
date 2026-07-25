"""
Exercício 3 ⭐⭐⭐

Utilize a mesma lista.

Altere a idade de Maria para 23.

Depois imprima todos os alunos.

"""
alunos = [
    {"nome": "Pedro", "idade": 27},
    {"nome": "Maria", "idade": 22},
    {"nome": "Carlos", "idade": 31}
]

for key in alunos:
    if key["nome"] == "Maria":
        key["idade"] = 23
    else:
        continue

for aluno in alunos:
    print(aluno["nome"])

for aluno in alunos:
    print(aluno["idade"])