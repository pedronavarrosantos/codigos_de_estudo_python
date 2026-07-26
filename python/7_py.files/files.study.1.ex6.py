"""
Exercício 1 ⭐⭐

Crie um arquivo chamado:

alunos.txt

Cadastre nele:

Pedro,27
Maria,22
Carlos,31

Depois leia o arquivo e imprima exatamente:

Pedro tem 27 anos.
Maria tem 22 anos.
Carlos tem 31 anos.

Dica: cada linha precisará ser dividida em duas partes.
"""
with open("alunos.txt", "w") as doc:
    doc.write("Pedro,27\n")
    doc.write("Maria,22\n")
    doc.write("Carlos,31\n")

with open("alunos.txt", "r") as doc:
    for aluno in doc:
        nome, idade = aluno.split(",")
        idade = idade.strip()
    print(f"{nome} tem {idade} anos.")
