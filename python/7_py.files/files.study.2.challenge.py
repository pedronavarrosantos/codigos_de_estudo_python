"""
Desafio ⭐⭐⭐⭐⭐⭐

Crie um programa que:

Leia o arquivo alunos.txt;
Transforme-o em uma lista de dicionários;
Exiba um menu:
1 - Procurar aluno
2 - Adicionar aluno
3 - Alterar idade
4 - Remover aluno
5 - Mostrar alunos
6 - Sair

Por enquanto, não grave as alterações no arquivo. 
Todas as modificações podem ficar apenas na memória (na lista). 
Na próxima aula aprenderemos a salvar novamente essa lista no arquivo.
"""
# Lista que receberá em forma de dicionário os dados dentro do arquivo .txt:
alunos = []

# Bloco de código que faz o presente arquivo .py acessar o arquivo .txt:
with open("file2.txt", "r") as doc:
    # for que percorre cada linha do .txt:
    for line in doc:
        # Transformação dos dados em variáveis e filtragem para inserção nos dicionários:
        nome, idade = line.split(",")
        idade = idade.strip()

        # Junção das variáveis no formato dicionário:
        alunos.append({
            "nome": nome,
            "idade": idade
        })

# Bloco de código while que dá ao usuário opções de manipulação da lista de dicionários dos alunos:   
while True:
    
    options = input("Bem-vindo ao sistema de alunos, escolha uma opção:\n 1 - Procurar aluno;\n 2 - Adicionar aluno;\n 3 - Alterar idade;\n 4 - Remover aluno;\n 5 - Mostrar alunos;\n 6 - Sair.\n")
    
    # Procura aluno:
    if options == "1":
            while True:
                alunoNome = input("Digite o nome do aluno ou digite '0' para retornar.\n")
                found = False

                if alunoNome != "0":
                    for aluno in alunos:
                        if aluno["nome"] == alunoNome:
                            print("Aluno encontrado")
                            print(aluno)
                            found = True
                        else:
                            continue
                    if not found:
                        print("Aluno não encontrado.")
                else:
                    print("Retornando ao menu principal")
                    break
    # Adiciona aluno:
    elif options == "2":
        while True:
            alunoNome = input("Digite o nome do aluno ou digite '0' para retornar.\n")

            if alunoNome != "0":
                alunoIdade = int(input("Digite a idade do aluno:\n"))
                
                alunos.append({
                    "nome": alunoNome,
                    "idade": alunoIdade
                })
                print(f"{alunoNome} de idade {alunoIdade} adicionado.")
            else:
                    print("Retornando ao menu principal")
                    break
    # Altera idade de aluno:
    elif options == "3":
        while True:
            alunoNome = input("Digite o nome do aluno que quer mudar a idade ou digite '0' para retornar.\n")
            if alunoNome != "0":
                for aluno in alunos:
                    if aluno["nome"] == alunoNome:
                        updateIdade = int(input("Digite a nova idade:\n"))

                        aluno.update({
                            "idade": updateIdade
                        })
                        print(f"Idade de {aluno["nome"]} alterada para {aluno["idade"]}")
            else:
                    print("Retornando ao menu principal")
                    break
    # Remove aluno            
    elif options == "4":
        while True:
            alunoNome = input("Digite o nome do aluno que deseja remover ou digite '0' para retornar.\n")
                
            if alunoNome != "0":    
                found = False

                for aluno in alunos:
                    if aluno["nome"] == alunoNome:
                        alunos.remove(aluno)
                        print(f"{alunoNome} removido")
                        found = True
                if not found:
                    print(f"{alunoNome} não está listado entre o alunos.")
            else:
                print("Retornando ao menu principal")
                break
    # Imprime os nomes dos alunos (apenas):
    elif options == "5":
        counter = 1
        for aluno in alunos:
            print(f"{counter}. {aluno["nome"]}")

            counter += 1
    # Encerra o aplicativo:
    elif options == "6":
        print("Saindo do aplicativo")
        break
    else:
        print(f"O comando {options} não é válido.")