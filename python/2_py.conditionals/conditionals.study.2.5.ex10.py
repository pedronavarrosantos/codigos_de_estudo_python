"""
👑 Exercício 10 — Chefe do Módulo
Sistema do Aeroporto

Crie:

def embarcar(idade, passagem, documento, bagagem):

Regras:

Primeiro:

Verifique se possui passagem.

Depois:

Verifique se possui documento.

Depois:

Verifique a idade.

Se for menor de 16 anos:

Apenas embarca se estiver acompanhado (use a variável acompanhado e adicione esse parâmetro à função).

Depois:

Verifique a bagagem.

Mensagens possíveis:

Passagem inválida
Documento ausente
Menor desacompanhado
Bagagem acima do permitido
Embarque autorizado

Este exercício reúne praticamente tudo o que você aprendeu sobre condicionais até agora: decisões em etapas, if aninhados, operadores lógicos, not, comparações e organização do código.
"""
idade = int(input("Qual é a sua idade?\n"))

def embarcar(idade):
    if idade >= 18:
        passagem = input("Você possui passagem?\n")
        if passagem.lower() == "sim":
            documento = input("Qual é o código do seu documento?\n")
            if documento.startswith("@") and documento.endswith("$"):
                bagagem = float(input("Qual é o peso da sua bagagem?\n"))
                if bagagem <= 10.0:
                    print("Embarque autorizado.")
                else:
                    print("Bagagem acima do permitido.")
            else:
                print("Documento ausente.")
        else:
            print("Passagem inválida.")
    else:
        acompanhado = input("Você está acompanhado do seu responsável?")
        if acompanhado.lower() == "sim":
            passagem = input("Você possui passagem?\n")
            if passagem.lower() == "sim":
                documento = input("Qual é o código do seu documento?\n")
                if documento.startswith("@") and documento.endswith("$"):
                    bagagem = float(input("Qual é o peso da sua bagagem?\n"))
                    if bagagem <= 10.0:
                        print("Embarque autorizado.")
                    else:
                        print("Bagagem acima do permitido.")
                else:
                    print("Documento ausente.")
            else:
                print("Passagem inválida.")
        else:
            print("Menor desacompanhado.")

embarcar(idade)