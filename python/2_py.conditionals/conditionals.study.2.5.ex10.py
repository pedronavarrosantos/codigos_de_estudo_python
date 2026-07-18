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

def verificar_dados():
    passagem = input("Você possui passagem?\n").lower()
    
    match passagem:
        case "sim":
            documento = input("Qual é o código do seu documento?\n")
            
            # Usando match para verificar múltiplas condições com uma tupla
            match (documento.startswith("@"), documento.endswith("$")):
                case (True, True):
                    bagagem = float(input("Qual é o peso da sua bagagem?\n"))
                    
                    # Usando "pattern guards" (if dentro do case) para verificar o peso
                    match bagagem:
                        case peso if peso <= 10.0:
                            print("Embarque autorizado.")
                        case _:
                            print("Bagagem acima do permitido.")
                            
                case _: # case _: funciona como o "default" ou "else"
                    print("Documento ausente.")
                    
        case _:
            print("Passagem inválida.")

def embarcar(idade):
    match idade:
        case i if i >= 18:
            verificar_dados()
            
        case _: # Caso seja menor de 18
            acompanhado = input("Você está acompanhado do seu responsável?\n").lower()
            
            match acompanhado:
                case "sim":
                    verificar_dados()
                case _:
                    print("Menor desacompanhado.")

embarcar(idade) 