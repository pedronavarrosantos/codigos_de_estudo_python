"""
Exercício 6 — Aluno

Crie uma classe Aluno.

O objeto deve possuir:

nome
idade
curso
nota

Crie dois alunos.

Depois mostre todas as informações.

Desafio adicional: crie um terceiro aluno sem copiar exatamente as linhas dos outros dois; apenas altere os argumentos utilizados na criação.
"""

class Aluno:
    def __init__(self, nome, idade, curso, nota):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

aluno1 = Aluno("Matheus Yan Monteiro dos Santos Almeida", 29, "Engenharia de Software", 7.7)
aluno2 = Aluno("Stephanie Sousa Ribeiro Navarro", 28, "Análise e Densevolvimento de Sistemas", 9.6)
aluno3 = Aluno("Pedro Nichollas Navarro dos Santos", 27, "Análise e Desenvolvimento de Sistemas", 7.1)

print(f"Aluno: {aluno1.nome}\nCurso: {aluno1.curso}\nIdade: {aluno1.idade} - Nota:{aluno1.nota}\n")
print(f"Aluno: {aluno2.nome}\nCurso: {aluno2.curso}\nIdade: {aluno2.idade} - Nota:{aluno2.nota}\n")
print(f"Aluno: {aluno3.nome}\nCurso: {aluno3.curso}\nIdade: {aluno3.idade} - Nota:{aluno3.nota}")