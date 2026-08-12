"""
⭐⭐⭐ Exercício 3 — Fila de pedidos

Crie uma fila contendo três dicionários.

Cada pedido deve possuir:

id
cliente
produto

Exemplo de estrutura:

{
    "id": 101,
    "cliente": "Pedro",
    "produto": "Cappuccino"
}

Depois processe os pedidos na ordem em que foram adicionados.

Resultado esperado:

Processando pedido 101
Cliente: Pedro
Produto: Cappuccino

Processando pedido 102
...

Processando pedido 103
...
"""

pedidos = []

pedidos.append({
    "id": 101,
    "cliente": "Pedro",
    "produto": "Cappuccino"
})
pedidos.append({
    "id": 102,
    "cliente": "Tephinha",
    "produto": "Milkshake de Morango"
})
pedidos.append({
    "id": 103,
    "cliente": "Monteiro",
    "produto": "Café"
})

while len(pedidos) > 0:
    pedido = pedidos[0]
    
    print(f"Procesando pedido {pedido['id']}\nCliente: {pedido['cliente']}\nProduto: {pedido['produto']}")
        
    pedidos.pop(0)
if len(pedidos) == 0:
    print("Fila vazia.")