"""
⭐⭐⭐⭐⭐ Exercício 5 — Arquivo

Tente abrir:

cardapio.txt

no modo leitura.

Se o arquivo não existir:

O arquivo do cardápio não foi encontrado.

Se existir, imprima seu conteúdo.

Use FileNotFoundError.
"""
print("Vamos abrir um arquivo.\n")
nome = input("Digite o nome do arquivo:\n")

try:
    with open(f'{nome}.txt', 'r') as doc:
        pass
    print(f"arquivo {nome} já existia e foi aberto para leitura.")
except FileNotFoundError:
    with open(f'{nome}.txt', 'a') as doc:
        pass
    print(f"arquivo {nome} ainda não existia e foi aberto para edição.")