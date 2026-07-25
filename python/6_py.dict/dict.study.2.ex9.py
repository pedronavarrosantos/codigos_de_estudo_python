"""
Exercício 5 ⭐⭐⭐

Peça um nome.

Mostre o dicionário inteiro.

Exemplo:

{
    "nome":"Pedro",
    "idade":27
}
"""
pessoas = [
    {"nome": "Pedro", "idade": 27},
    {"nome": "Stephanie", "idade": 27},
    {"nome": "Matheus", "idade": 28},
    {"nome": "Vitor", "idade": 66},
    {"nome": "Jean", "idade": 34},
]

nom = input("Digite um nome:\n")
found = False

for pessoa in pessoas:
    if nom == pessoa["nome"]:
        print(pessoa)
        found = True
        break
if not found:
    print("Nome não encontrado.")

