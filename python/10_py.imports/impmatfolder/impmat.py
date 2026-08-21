def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def elevar(a, b):
    return a ** b

def use():
    print(f"soma: {somar(12, 4)}.")
    print(f"subtração: {somar(12, 4)}.")
    print(f"numtiplicação: {multiplicar(12, 4)}.")
    print(f"potenciação: {elevar(12, 4)}.")

if __name__ == "__main__":
    use()
    print(__name__)