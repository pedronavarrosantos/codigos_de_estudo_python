"""
Exercício 4 ⭐⭐⭐⭐

Peça um nome.

Caso exista, remova esse aluno da lista.

Depois imprima a lista atualizada.
"""
alunos = [
    {"nome": "Pedro", "idade": 27},
    {"nome": "Maria", "idade": 22},
    {"nome": "Carlos", "idade": 31}
]

pessoa = input("Digite um nome:\n")

for aluno in alunos:
    if aluno["nome"] == pessoa:
        alunos.remove(aluno)

for aluno in alunos:
    print(aluno)