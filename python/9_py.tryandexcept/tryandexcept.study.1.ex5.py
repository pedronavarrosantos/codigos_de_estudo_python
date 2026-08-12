"""
⭐⭐⭐⭐⭐ Exercício 5 — Tia Rosa

Agora aplique isso ao que você já construiu.

Crie uma entrada para quantidade:

Digite a quantidade do produto:

Ela deve:

aceitar somente números inteiros;
não encerrar o programa caso o usuário digite texto;
continuar pedindo até receber um valor válido;
armazenar o resultado na variável quantidade.

Exemplo:

Digite a quantidade do produto: dois
Quantidade inválida.

Digite a quantidade do produto: 2
Quantidade registrada: 2
"""
while True:
    qnt = input("Digite a quantidade do produto:\n")
    try:
        qnt_inte = int(qnt)
        break
    except ValueError:
        print(f"{qnt} é um valor inválido, digite apenas números inteiros.")

print(f"A quantidade selecionada para o produto foi {qnt_inte}.\n")