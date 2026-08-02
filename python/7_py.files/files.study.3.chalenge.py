"""
Desafio ⭐⭐⭐⭐⭐⭐

Modifique o sistema de alunos que você criou para que todas as operações (adicionar, alterar e remover) 
sejam salvas automaticamente no arquivo .txt. Assim, quando você fechar e abrir o programa novamente,
as alterações continuarão lá.

Esse desafio é um excelente fechamento do módulo de arquivos e muito próximo de como pequenos sistemas funcionam antes de introduzirmos bancos de dados.
"""

# A maior parte das linhas de código abaixo foram importadas do documento D:\VSCODE.pastas\codigos_de_estudo\python\7_py.files\files.study.2.challenge.py
# Um novo txt chamado 'challenge.txt' é criado neste documento.

# Função 'savedoc() salva o arquivo sempre que uma alteração é feita:
def savedoc():
    with open("challenge.txt", "w") as doc:
        for aluno in alunos:
             doc.write(f"{aluno['nome']},{aluno['idade']}\n")

# 'alunos = []' é a lista que receberá em forma de dicionário os dados dentro do arquivo challenge.txt:
alunos = []

# Bloco de código que faz o presente arquivo .py acessar o arquivo .txt:
with open("challenge.txt", "r") as doc:
    # for que percorre cada linha do .txt:
    for line in doc:
        # Transformação dos dados em variáveis e filtragem para inserção nos dicionários:
        nome, idade = line.split(",")
        idade = idade.strip()

        # Junção das variáveis no formato de dicionário:
        alunos.append({
            "nome": nome,
            "idade": idade
        })

# Bloco de código while que dá ao usuário opções de manipulação da lista de dicionários dos alunos:   
while True:
    # A variavel 'options' permite que o usuário acesse os recursos do aplicativo:
    options = input("Bem-vindo ao sistema de alunos, escolha uma opção de 1 a 6:\n 1 - Procurar aluno;\n 2 - Adicionar aluno;\n 3 - Alterar idade;\n 4 - Remover aluno;\n 5 - Mostrar alunos;\n 6 - Sair.\n")
    
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
                savedoc()
            else:
                    print("Retornando ao menu principal")
                    break
    # Altera idade de aluno:
    elif options == "3":
        while True:
            alunoNome = input("Digite o nome do aluno que quer mudar a idade ou digite '0' para retornar.\n")
            found = False
            
            if alunoNome != "0":
                for aluno in alunos:
                    if aluno["nome"] == alunoNome:
                        updateIdade = int(input("Digite a nova idade:\n"))
                        found = True

                        aluno.update({
                            "idade": updateIdade
                        })
                        print(f"Idade de {aluno['nome']} alterada para {aluno['idade']}")
                        savedoc()
                if not found:
                    print(f"{alunoNome} não está listado entre o alunos.")
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

                        found = True

                        print(f"{alunoNome} removido")
                        savedoc()
                        break
                if not found:
                    print(f"{alunoNome} não está listado entre o alunos.")
            else:
                print("Retornando ao menu principal")
                break
    # Imprime os nomes dos alunos (apenas):
    elif options == "5":
        counter = 1
        for aluno in alunos:
            print(f"{counter}. {aluno['nome']}")

            counter += 1
    # Encerra o aplicativo:
    elif options == "6":
        print("Saindo do aplicativo")
        break
    # Else para caso o usuário escreva um comando invalido:
    else:
        print(f"O comando {options} não é válido.")