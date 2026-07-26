"""
Exercício 1 ⭐

Crie um arquivo chamado frutas.txt contendo:

Maçã
Banana
Laranja
Uva

Depois utilize read() para imprimir todo o conteúdo.
"""
with open("pyfile4.txt", "w") as doc:
    doc.write("Maçã\n")
    doc.write("Banana\n")
    doc.write("Laranja\n")
    doc.write("Uva\n")

with open("pyfile4.txt", "r") as doc:
    print(doc.read())

"""
Exercício 2 ⭐⭐

Utilizando o mesmo arquivo, imprima apenas a primeira linha usando readline().
"""
with open("pyfile4.txt", "r") as doc:
    print(doc.readline())

"""
Exercício 3 ⭐⭐⭐

Utilize readlines().

Depois percorra a lista retornada imprimindo uma fruta por linha usando strip().
"""
with open("pyfile4.txt", "r") as doc:
    lines = doc.readlines()
    
    for line in lines:
        print(line.strip())

"""
Exercício 4 ⭐⭐⭐⭐

Leia o arquivo utilizando apenas:

for linha in arquivo:

e imprima todas as frutas.
"""
with open("pyfile4.txt", "r") as doc:
    
    for line in doc:
        print(line)