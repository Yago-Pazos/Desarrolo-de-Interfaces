import tkinter as tk

def actualizar():
    seleccionadas = []
    if var_leer.get(): seleccionadas.append("Leer")
    if var_deporte.get(): seleccionadas.append("Deporte")
    if var_musica.get(): seleccionadas.append("Música")
    etiqueta.config(text="Aficiones: " + ", ".join(seleccionadas))

root = tk.Tk()
root.title("Ejercicio 4 - Checkbutton")
root.geometry("300x200")

var_leer = tk.IntVar()
var_deporte = tk.IntVar()
var_musica = tk.IntVar()

tk.Checkbutton(root, text="Leer", variable=var_leer, command=actualizar).pack()
tk.Checkbutton(root, text="Deporte", variable=var_deporte, command=actualizar).pack()
tk.Checkbutton(root, text="Música", variable=var_musica, command=actualizar).pack()

etiqueta = tk.Label(root, text="Aficiones: ")
etiqueta.pack(pady=10)

root.mainloop()