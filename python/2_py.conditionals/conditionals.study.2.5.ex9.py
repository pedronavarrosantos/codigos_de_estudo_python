"""
🐍 Exercício 9 ⭐⭐⭐⭐⭐

Sistema bancário

Crie:

def sacar(logado, saldo, valor):

Regras:

Primeiro:

Verifique se está logado.

Depois:

Verifique se há saldo suficiente.

Depois:

Verifique se o valor solicitado é maior que zero.

Mensagens:

Usuário não autenticado
Saldo insuficiente
Valor inválido
Saque realizado
"""
logado = input("O usuário está logaddo?\n")
saldo = float(input("Qual é o saldo da conta?\n"))
valor = float(input("Quanto deseja sacar?\n"))

def sacar(logado, saldo, valor):
    restante = saldo - valor
    if logado.lower() == "sim":
        if saldo > 0:
            if valor <= saldo:
                print(f"Saque de R$:{valor} realizado.")
                if restante > 0:
                    print(f"O seu saldo restante é R$:{restante}.")
                else:
                    print("E o seu saldo agora está zerado.")
            else:
                print(f"Impossível realizar saque, o valor de R$:{valor} é maior do que o seu saldo de R$:{saldo}.")
        else:
            print ("Saldo zerado.")
    else:
        print("Usuário não autenticado.")

sacar(logado, saldo, valor)
