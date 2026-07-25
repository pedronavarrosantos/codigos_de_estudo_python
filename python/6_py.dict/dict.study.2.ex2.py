"""
Exercício 1 ⭐

Crie a lista:

alunos = [
    {
        "nome": "Pedro",
        "idade": 27
    },
    {
        "nome": "Maria",
        "idade": 22
    }
]

Imprima apenas:

Pedro
Maria
"""
alunos = [
    {
        "nome": "Pedro",
        "idade": 27
    },
    {
        "nome": "Maria",
        "idade": 22
    }
]

for nom in alunos:
    print(nom["nome"])

"""
Exercício 2 ⭐⭐

Utilize a mesma lista.

Imprima:

Pedro tem 27 anos.
Maria tem 22 anos.
"""
for aluno in alunos:
    print(f'{aluno["nome"]} tem {aluno["idade"]} anos.')

"""
Exercício 3 ⭐⭐⭐

Adicione um terceiro aluno utilizando:

append()

Depois percorra a lista imprimindo todos os nomes.
"""
gil = {
    "nome": "Gilberto",
    "idade": 41
}

alunos.append(gil)

for aluno in alunos:
    print(aluno["nome"])

"""
Exercício 4 ⭐⭐⭐⭐

Crie uma lista contendo três produtos.

Cada produto deve possuir:

nome
preço

Depois mostre:

Notebook - R$4500
Mouse - R$120
Teclado - R$250
"""
produtos = [{
    "produto": "Notebook",
    "preço": "R$4500"
    },
    {
    "produto": "Mouse",
    "preço": "R$120" 
    },
    {
    "produto": "Teclado",
    "preço": "R$250" 
    }
]
for produto in produtos:
    print(f"{produto["produto"]} - {produto["preço"]}")

"""
Exercício 5 ⭐⭐⭐⭐⭐

Crie um pequeno cadastro de carros.

Cada carro deve possuir:

marca
modelo
ano

Cadastre pelo menos três carros em uma lista.

Depois percorra essa lista mostrando:

Toyota - Corolla - 2022
Honda - Civic - 2021
Volkswagen - Golf - 2020
"""
carros = [
    {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2022
    }
]

carros.append({
    "marca": "Honda",
    "modelo": "Civic",
    "ano": 2021
}
)
carros.append({
    "marca": "Volkswagen",
    "modelo": "Golf",
    "ano": 2020
}
)

for carro in carros:
    print(f'{carro["marca"]} - {carro["modelo"]} - {carro["ano"]}')