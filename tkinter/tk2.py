import tkinter as tk
import os

def nwin(x):
    # Cria a nova janela secundária
    nova_janela = tk.Toplevel(janela)
    nova_janela.title(f"{x}")
    nova_janela.geometry("300x200")

janela = tk.Tk()
janela.title("Café Tia Rosa.")
janela.geometry("700x500")
janela.configure(bg = "#7b5e4a")

logo = tk.PhotoImage(file = "tia_rosa_logo.png")
logo = logo.subsample(8, 8)

logo_label = tk.Label(janela, image = logo, bg="#7b5e4a")
logo_label.pack()



cardapio_bt = tk.Button(
    janela,
    text = "Cardápio",
    command = lambda: nwin("Sistema de Cardápio"),
    bg = "#3B2A22",
    fg = "light coral"
)

cardapio_bt.pack(pady = 4)

estoque_bt = tk.Button(
    janela,
    text = "Estoque",
    bg = "#3B2A22",
    fg = "light coral"
)

estoque_bt.pack(pady = 4)

clientes_bt = tk.Button(
    janela,
    text = "Clientes",
    bg = "#3B2A22",
    fg = "light coral"
)

clientes_bt.pack(pady = 4)

pedidos_bt = tk.Button(
    janela,
    text = "Pedidos",
    bg = "#3B2A22",
    fg = "light coral"
)

pedidos_bt.pack(pady = 4)

janela.mainloop()