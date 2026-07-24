"""
Exercício 1 ⭐

Crie o seguinte dicionário:

livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano": 1899
}

Depois imprima apenas:

título;
autor.
"""
livro = { 
    "titulo": "Dom casmurro",
    "autor": "Machado de Assis",
    "ano": 1899
}

print(livro)

"""
Exercício 2 ⭐⭐

Crie:

filme = {
    "nome": "Interestelar",
    "ano": 2014
}

Depois adicione:

"nota": 8.7

Imprima o dicionário.
"""
filme = {
    "nome": "Interestelar",
    "ano": 2014
}

filme["nota"] = 8.7

print(filme)

"""
Exercício 3 ⭐⭐⭐

Crie:

aluno = {
    "nome": "Pedro",
    "idade": 27,
    "curso": "ADS"
}

Altere a idade para:

28

Depois imprima o dicionário.
"""
aluno = {
    "nome": "Pedro",
    "idade": 27,
    "curso": "ADS"
}

aluno["idade"] = 28

print(aluno)

"""
Exercício 4 ⭐⭐⭐⭐

Crie:

computador = {
    "marca": "Dell",
    "memoria": "16GB",
    "ssd": "512GB"
}

Remova a chave:

ssd

Depois imprima o resultado.
"""
computador = {
    "marca": "Dell",
    "memoria": "16GB",
    "ssd": "512GB"
}

del computador["ssd"]

print(computador)

"""
Exercício 5 ⭐⭐⭐⭐⭐

Crie um dicionário representando você.

Inclua pelo menos:

nome;
idade;
cidade;
curso;
linguagem favorita.

Depois imprima cada informação separadamente usando as chaves.
"""
futuro_dev ={
    "nome": "Pedro Nichollas Navarro dos Santos",
    "idade": 27,
    "cidade": "Águas Claras",
    "curso": "ADS",
    "linguagem favorita": "Python"
}

print(futuro_dev["nome"])
print(futuro_dev["idade"])
print(futuro_dev["cidade"])
print(futuro_dev["curso"])
print(futuro_dev["linguagem favorita"])