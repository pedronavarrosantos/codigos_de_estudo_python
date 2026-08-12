"""
⭐⭐⭐⭐⭐⭐⭐ Exercício 7 — Tia Rosa

Crie um dicionário representando um prato:

nome
preço
ingredientes
descrição

Peça ao usuário qual informação deseja visualizar.

Seu programa deve tratar KeyError caso ele peça uma informação que não exista.

Depois faça o programa continuar funcionando para que o usuário possa tentar novamente.

Aqui você já estará combinando dicionário + entrada de dados + while + try/except.
"""
prato = {
    "nome": "Cappuccino",
    "preco": 8.50,
    "ingredientes": "café, leite e espuma",
    "descrição": "cappuccino brabo"
}
while True:
    key = input("Digite qual chave que acessar:\n")

    try:
        print(prato[f'{key}'])
        break
    except KeyError:
        print("Chave não encontrada.")
