import tkinter as tk

def cambiar_texto():
    label3.config(text="Has presionado el botón")

root = tk.Tk()
root.title("Ejercicio 1 - Label")
root.geometry("300x200")

label1 = tk.Label(root, text="¡Bienvenido a mi ventana!")
label1.pack(pady=5)

label2 = tk.Label(root, text="Yago Pazos Lema")
label2.pack(pady=5)

label3 = tk.Label(root, text="Texto inicial")
label3.pack(pady=5)

boton = tk.Button(root, text="Cambiar texto", command=cambiar_texto)
boton.pack(pady=10)

root.mainloop()