"""
Exercícios
Exercício 1 ⭐

Crie:

pessoa = {
    "nome": "Pedro",
    "idade": 27,
    "cidade": "Brasília"
}

Utilize um for para imprimir apenas as chaves.
"""
pessoa = {
    "nome": "Pedro",
    "idade": 27,
    "cidade": "Brasília"
}

for key in pessoa:
    print(key)

"""
Exercício 2 ⭐⭐

Utilize o mesmo dicionário.

Imprima:

nome -> Pedro
idade -> 27
cidade -> Brasília

Utilizando:

pessoa[chave]
"""
for key in pessoa:
    print(key, "->", pessoa[key])

"""
Exercício 3 ⭐⭐⭐

Faça o mesmo exercício anterior.

Mas agora utilizando:

items()
"""
for key, value in pessoa.items():
    print(key, "->", value)

"""
Exercício 4 ⭐⭐⭐⭐

Crie:

produto = {
    "nome": "Notebook",
    "preco": 4500
}

Utilize:

get()

Para tentar acessar:

"marca"

Caso ela não exista, mostre:

Marca não cadastrada.
"""
produto = {
    "nome": "Notebook",
    "preco": 4500
}

print(produto.get("marca", "Marca não cadastrada"))

"""
Exercício 5 ⭐⭐⭐⭐⭐

Crie:

aluno = {
    "nome": "Pedro",
    "idade": 27
}

Depois utilize:

update()

Para:

alterar a idade para 28;
adicionar a chave "curso" com valor "ADS".

Depois imprima o dicionário.
"""
aluno = {
    "nome": "Pedro",
    "idade": 27
}

aluno.update({
    "idade": 28,
    "curso": "ADS"
})

print(aluno)