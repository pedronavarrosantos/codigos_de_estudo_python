"""
⭐⭐⭐⭐ Exercício 4 — KeyError

Crie:

prato = {
    "nome": "Cappuccino",
    "preco": 8.50,
    "ingredientes": "café, leite e espuma"
}

Peça ao usuário o nome de uma informação que deseja consultar.

Exemplo:

Digite a informação que deseja consultar: ingredientes

Se a chave existir, mostre seu valor.

Se não existir:

Essa informação não está cadastrada.
"""
prato = {
    "nome": "Cappuccino",
    "preco": 8.50,
    "ingredientes": "café, leite e espuma"
}

while True:
    key = input("Digite o nome da chave que quer acessar\n")

    try:
        print(prato[f'{key}'])
        break
    except KeyError:
        print(f"A chave '{key}' não existe.\n")