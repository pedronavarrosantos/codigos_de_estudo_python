"""
O objetivo deste arquivo é melhorar o dict.study2.ex16

Para tal:
1. Transformar opções em funções;
2. Acrescentar docstrings descrevendo o que cada bloco de código faz.

O arquivo dict.study2.ex16 é um sistema de cadastro de dicionários de informações de pessoas.
"""

# Função adicionar() insere dicionários de pessoas na lista.
def adicionar():
    while True:
        nom = input("Digite o nome da pessoa para adicioná-la ou '0' para retornar ao menu principal.\n")
            
        if nom == "0":
            print("Retornando")
            break

        found = False

        for pessoa in pessoas:
            if pessoa["nome"] == nom:
                found = True
                break
        if found:
            print("Pessoa já cadastrada.")
            continue
            
        idade = int(input("Digite a idade da pessoa:\n"))

        pessoa = ({
            "nome": nom,
            "idade": idade
        })
        pessoas.append(pessoa)
        print(pessoas)

# Função procurar() verifica e retorna informações do dicionário de uma pessoa se a pessoa existir na lista.
def procurar():
    while True:
            if len(pessoas) == 0:
                print("A lista está vazia\n")
                break

            nomOrAge = input("Deseja procurar alguém pelo nome ou pela idade? Para retornar ao menu principal digite '0'.\n")

            if nomOrAge == "0":
                    print("Retornando")
                    break
            elif nomOrAge == "nome":
                nom = input("Digite o nome da pessoa para procurá-la:\n")

                for pessoa in pessoas:
                    if pessoa["nome"] == nom:
                        print(pessoa)
            if nomOrAge == "idade":
                idade = int(input("Digite a idade:\n"))

                print(f"A(as) pessoa(as) com {idade} anos é(são):")
                for pessoa in pessoas:
                    if pessoa["idade"] == idade:
                        print(pessoa)
                    else:
                        continue

# Função alterarIdade() localiza uma pessoa entre os dicionários e altera a sua idade.
def alterarIdade():
    nom = input("Digite o nome da pessoa que quer alterar a idade:\n")
    found = False

    for pessoa in pessoas:
        if pessoa["nome"] == nom:
            age = int(input("Digite a idade que deseja colocar:\n"))
            pessoa.update({
                "idade": age
            })
            print(pessoa)
            found = True
            break
    if not found:
        print("Pessoa não encontrada.")

# Função remover() recebe como input um nome, se o nome existir em algum dicionário lista, o dicionário é removido.
def remover():
    while True:
            nom = input("Digite o nome da pessoa para removê-la ou '0' para retornar ao menu principal.\n")
            found = False

            if nom == "0":
                print("Retornando")
                break
            for pessoa in pessoas:
                if pessoa["nome"] == nom:
                    pessoas.remove(pessoa)
                    print("Pessoa removida")
                    print(pessoas)
                    found = True
                    break
                else:
                    continue
            if not found:
                print("Pessoa não encontrada.")

# Função showList() exibe o conteúdo de cada dicionário dentro da lista.
def showList():
    for pessoa in pessoas:
            print(f"{pessoa['nome']} - {pessoa['idade']}.\n")

# Função end() encerra o funcionamento de toda a aplicação.
def end():
    print("Encerrando aplicação")

# A seguir está a estrutura do programa que se aproveita das funções construídas anteriormente:

# pessoas = [] será a lista que recebe todo o produto do programa
pessoas = []

while True:
    # A variável 'options' recebe números de 1 a 6 em forma de string, um número para cada função construída. Caso receba um valor diferente, o programa acusa ser um comando inválido
    options = input("Escolha um número:\n 1. Adicionar;\n 2. Procurar;\n 3. Alterar idade;\n 4. Remover;\n 5. Mostrar lista;\n 6. Sair.\n")

    if options == "1":
        adicionar()
    elif options == "2":
        procurar()
    elif options == "3":
        alterarIdade()
    elif options == "4":
        remover()
    elif options == "5":
        showList()
    elif options == "6":
        end()
        break
    # 'else' acusa comando inválido.
    else:
        print(f"O comando {options} não é válido.\n")