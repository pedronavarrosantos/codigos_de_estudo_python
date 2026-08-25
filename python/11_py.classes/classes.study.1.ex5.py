"""
Exercício 5 — Funcionário

Crie uma classe Funcionario.

A classe deve receber:

nome
cargo
salario

Crie três funcionários diferentes.

Depois imprima os dados de cada um.

Exemplo:

Nome: Ana
Cargo: Desenvolvedora
Salário: R$ 5000
"""
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

func1 = Funcionario("Monteiro", "Tech Lead", 21980.66)
func2 = Funcionario("Pedro", "Estaigário de TI", 1989.73)
func3 = Funcionario("Stephanie", "Cientista de Dados", 16540.21)

print(f"Nome: {func1.nome}\nCargo: {func1.cargo}\nSalário: {func1.salario};\n")
print(f"Nome: {func2.nome}\nCargo: {func2.cargo}\nSalário: {func2.salario};\n")
print(f"Nome: {func3.nome}\nCargo: {func3.cargo}\nSalário: {func3.salario};\n")