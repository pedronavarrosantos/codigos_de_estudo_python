"""
Exercício 5 ⭐⭐⭐⭐⭐

Crie um cadastro de livros.

Cada livro deve possuir:

título
autor
ano

Cadastre pelo menos 3 livros.

Depois permita ao usuário procurar um título.

Se existir, mostre:

Título
Autor
Ano

Caso contrário:

Livro não encontrado.
"""
livros = [
    {"título": "Majestic Savage", "autor": "Alfred Hartestein", "ano": 1966},
    {"título": "O Manifesto", "autor": "Lineu da Silva", "ano": 1941},
    {"título": "Época Boa", "autor": "Hamilton Lonso", "ano": 1980},
    {"título": "Matheus Solteiro", "autor": "Matheus Yan Monteiro dos Santos Almeida", "ano": 1997},
    {"título": "Porcos Imundos", "autor": "Pedro Navarro", "ano": 1999}
]

livro = input("Digite o nome de um livro:\n")
existe = False

for exemplar in livros:
    if exemplar["título"] == livro:
        print(exemplar)
        existe = True
        break
if not existe:
    print(f"O {livro} não está no acervo.")