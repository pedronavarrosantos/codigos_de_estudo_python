"""
Crie uma classe Conta.

O __init__ deve receber:

titular
saldo

Crie:

conta1 = Conta("Pedro", 1500)

Depois imprima:

Titular: Pedro
Saldo: R$ 1500

Não crie métodos de saque ou depósito ainda.

O objetivo é praticar apenas:

__init__
self
atributos
objetos
"""

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

conta1 = Conta("Pedro N.N.S", 1500.00)

print(f"Titular: {conta1.titular}\nSaldo: {conta1.saldo}.")