ARQUIVO = "city.list.txt"

# Carrega as cidades salvas anteriormente (se o arquivo existir)
try:
    with open(ARQUIVO, "r") as file:
        cidades = [linha.strip() for linha in file if linha.strip()]
except FileNotFoundError:
    cidades = []
 
 
def salvar():
    """Grava o estado atual da lista no arquivo, uma cidade por linha."""
    with open(ARQUIVO, "w") as file:
        for cidade in cidades:
            file.write(cidade + "\n")

def adicionar():
    """Opção 1: Permite ao usuário colocar itens na lista."""
    while True:
            cidade = input("Digite o nome da cidade ou digite '0' para retornar ao menu principal'.\n")
 
            if cidade != "0" and cidade not in cidades:
                cidades.append(cidade)
                salvar()
            elif cidade != "0" and cidade in cidades:
                print("A cidade informada já está na lista")
            else:
                print("Retornando ao menu principal.")
                break

def remover():
    """Opção 2: Permite ao usuário retirar itens da lista."""
    while True:
            cidade = input("Digite o nome da cidade que quer REMOVER ou digite '0' para retornar ao menu principal'.\n")
 
            if cidade != "0" and cidade in cidades:
                print(f"A cidade {cidade} foi removida da lista.")
                cidades.remove(cidade)
                salvar()
            elif cidade != "0" and cidade not in cidades:
                print("Impossível remover cidade por que já não estava na lista")
            else:
                print("Retornando ao menu principal.")
                break

def listar():
    """Opção 3: Permite ao usuário ver os itens da lista."""
    print(cidades)

def estat():
    """Opção 4: Permite ao usuário verificar detalhes sobre a lista."""
    if len(cidades) == 0:
            print("A lista está vazia.")
    elif len(cidades) == 1:
        print(f"A única cidade na lista é a {cidades[0]}.")
    else:
        print(f"A quantidade de cidades na lista é {len(cidades)};\n A primeira cidade é a {cidades[0]}\n A última cidade é a {cidades[-1]}")

def ordenar():
    """Opção 5: Permite ao usuário colocar os itens da lista em ordem alfabética."""
    cidades.sort()
    salvar()
    print(cidades)

def inversao():
    """Opção 6: Permite ao usuário inverter a ordem dos itens da lista."""
    cidades.reverse()
    salvar()
    print(cidades)

def posicao():
    """Opção 7: Permite ao usuário verificar a posição de um item da lista."""
    cidade = input("Digite o nome da cidade para verificar sua posição ou digite 'voltar' para retornar ao menu principal'.\n")
 
    if cidade in cidades:
        print(f"A Posição da cidade é {cidades.index(cidade)}.")
    else:
        print("Cidade não encontrada.")

def fim():
    """Opção 8: Permite ao usuário fechar o programa."""
    print("Encerrando aplicação")
    print(cidades)
    salvar()

while True:
    # Este while é o coração do documento, ele se aproveita de todas as funções construídas anteriormente.
    options = input("Digite um número de 1 a 8 para escolher uma das seguintes opções:\n 1. Adicionar cidade;\n 2. Remover cidade;\n 3. Exibir lista;\n 4. Ver detalhes da lista;\n 5. Colocar em ordem alfabética;\n 6. Inverter a ordem da lista;\n 7. Verificar a posição de uma cidade;\n 8. Encerrar aplicação.\n")
 
    if options == "1":
        # Insere itens na lista e/ou retorna ao menu principal.
        adicionar()
    elif options == "2":
        # Retira itens na lista e/ou retorna ao menu principal.
        remover()
    elif options == "3":
        # Exibe itens na lista.
        listar()
    elif options == "4":
        # Informa a primeira e última cidade da lista, além disso o número de cidades.
        estat()
    elif options == "5":
        # Coloca os intens em ordem alfabética.
        ordenar()
    elif options == "6":
        # Inverte a ordem da lista.
        inversao()
    elif options == "7":
        # Verifica a posição de uma cidade na lista.
        posicao()
    elif options == "8":
        # Fecha o programa.
        fim()
        break
    else:
        # Else para caso o usuário não digite um comando válido e evitar crash do programa.
        print(f"O comando {options} não é válido.")