"""
Exercício 7 — Livro

Crie uma classe Livro com:

titulo
autor
ano
preco

Crie três livros.

Depois:

Mostre o título de cada livro.
Mostre o preço de cada livro.
Mostre qual livro possui o maior preço.

Dica: você pode comparar:

livro1.preco
livro2.preco
livro3.preco

Não precisa criar métodos ainda.
"""

class Livro:
    def __init__(self, titulo, autor, ano, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.preco = preco

livro1 = Livro("O Hobbit", "J.R.R. Tolkien", 1937, 73.99)
livro2 = Livro("A Cor que Caiu do Céu", "H.P. LoveCraft", 1927, 24.99)
livro3 = Livro("Laranja Mecânica", "Anthony Burgess", 1962, 85.40)

livros = [livro1, livro2, livro3]
precos = []

for livro in livros:
    print(f"Título: {livro.titulo} - Preço {livro.preco}")

    precos.append(livro.preco)

maior = max(precos)

for livro in livros:
    if livro.preco == maior:
        print(f"O livro com maior preço é o {livro.titulo}, que custa, respectivamente, R${livro.preco}.")  