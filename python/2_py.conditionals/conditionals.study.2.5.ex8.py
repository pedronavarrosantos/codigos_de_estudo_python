"""
🐍 Exercício 8 ⭐⭐⭐⭐⭐

Sistema de matrícula

Crie:

def matricular(idade, documentos, vagas):

Regras:

Primeiro:

Verifique a idade.

Depois:

Verifique os documentos.

Depois:

Verifique se ainda existem vagas.

Mensagens possíveis:

Menor de idade
Documentação incompleta
Sem vagas
Matrícula realizada
"""
# Novamente o exercício sofre com falta de critérios. Vou delimitar que a turma tem apenas 150 vagas, caso o número de matrícula > 150 direi que não existem mais vagas.

idade = int(input("Qual é a sua idade?\n"))
documentos = input("Você já entregou todos os documento?\n")
vagas = int(input("Qual é o seu número de matrícula?\n"))

def matricular(idade, documentos, vagas):
    if idade >= 18:
        if documentos.lower() == "sim":
            if vagas <= 150:
                print ("Matrícula realizada.")
            else:
                print("Sem vagas")
        else:
            print("Documentação incompleta")
    else:
        print("Menor de idade.")

matricular(idade, documentos, vagas)
