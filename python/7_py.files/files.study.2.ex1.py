"""
Exercício 1 ⭐

Crie um arquivo chamado:

alunos.txt

Com o seguinte conteúdo:

Pedro,27
Maria,22
Carlos,31

Depois leia o arquivo e imprima cada linha exatamente como está gravada.
"""

with open("file2.txt", "w") as doc:
    doc.write("Pedro,27\n")
    doc.write("Maria,22\n")
    doc.write("Carlos,31\n")
    doc.write("Jean,33\n")

with open("file2.txt", "r") as doc:
    print(doc.read())