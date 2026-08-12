"""
⭐⭐ Exercício 2 — Fila automática

Crie uma fila com:

Ana
Bruno
Carlos
Daniel

Depois utilize um while para retirar todos os elementos automaticamente.

Resultado:

Atendendo Ana
Atendendo Bruno
Atendendo Carlos
Atendendo Daniel
Fila vazia.
"""
fila = []

fila.append("Ana")
fila.append("Bruno")
fila.append("Carlos")
fila.append("Daniel")

while len(fila) > 0:
    print(f"Atendendo {fila[0]}")
    
    fila.pop(0)
if len(fila) == 0:
    print("Fila vazia.")