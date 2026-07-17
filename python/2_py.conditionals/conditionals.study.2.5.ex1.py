"""
🐍 Exercício 1 ⭐

Crie:

def entrar_evento(idade, ingresso):

Regras:

Primeiro verifique a idade.
Se for menor de 18, retorne:
Menor de idade
Caso contrário, verifique se possui ingresso.

Se possuir:

Entrada autorizada

Caso contrário:

Sem ingresso

Objetivo: usar um if dentro de outro.
"""
idade = int(input("Qual é a sua idade?\n"))
ingresso = input("Você possui ingresso? Responda com sim ou não.\n")

def entrar_evento(idade, ingresso):
    if idade > 18:
        if ingresso.lower() == "sim":
            return "Entrada autorizada."
        return "Sem ingresso."
    return "Menor de idade."

print(entrar_evento(idade, ingresso))