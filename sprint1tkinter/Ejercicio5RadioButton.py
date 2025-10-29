import tkinter as tk

def cambiar_color():
    root.config(bg=var_color.get())

root = tk.Tk()
root.title("Ejercicio 5 - Radiobutton")
root.geometry("300x200")

var_color = tk.StringVar(value="white")

tk.Radiobutton(root, text="Rojo", variable=var_color, value="red", command=cambiar_color).pack()
tk.Radiobutton(root, text="Verde", variable=var_color, value="green", command=cambiar_color).pack()
tk.Radiobutton(root, text="Azul", variable=var_color, value="blue", command=cambiar_color).pack()

root.mainloop()