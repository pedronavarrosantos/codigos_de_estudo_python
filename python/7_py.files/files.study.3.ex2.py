"""
Exercício 2 ⭐⭐

Leia o arquivo novamente e verifique se ele ficou exatamente igual ao esperado.
"""

with open("file3.txt", "r") as doc:
    for line in doc:
        print(line.strip())