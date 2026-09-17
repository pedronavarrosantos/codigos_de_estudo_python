import tkinter as tk

def cdb():
    print("clicked")

win = tk.Tk()
win.title("Minha primeira janela")
win.geometry("400x300")


botao = tk.Button(
    win,
    text="Esta é a minha primeira janela front-end",
    command=cdb,
    bg="blue",
    fg="white"
)

botao.pack(pady=20)

benjamin = tk.Button(
    win,
    text="Olá Tephinha, te amo",
    bg = "brown",
    fg = "pink"
)

benjamin.pack(pady = 60)

win.mainloop()