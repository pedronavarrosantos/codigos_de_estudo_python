"""
Exercício 5 ⭐⭐⭐⭐⭐

Crie um programa que leia o arquivo frutas.txt e conte quantas frutas existem nele.

Ao final, exiba:

Quantidade de frutas: 4

Esse exercício introduz um padrão muito comum: percorrer um arquivo para contar, filtrar ou processar registros. 
Depois usaremos exatamente essa ideia para ler cadastros completos (como pessoas e cidades) salvos em arquivos.
"""
with open("pyfrutasfilesex5.txt", "w") as doc:
    doc.write("Mamão\n")
    doc.write("Limão\n")
    doc.write("Maça\n")
    doc.write("Banana\n")
    doc.write("Pepino\n")
    doc.write("Pera\n")

with open("pyfrutasfilesex5.txt", "r") as doc:
    counter = 0
    
    for fruta in doc:
        counter += 1

print(f"O documento tem {counter} frutas.")