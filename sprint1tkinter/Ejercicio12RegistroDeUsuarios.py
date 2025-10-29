import tkinter as tk
from tkinter import messagebox

def añadir_usuario():
    nombre = entry_nombre.get()
    edad = scale_edad.get()
    genero = var_genero.get()
    if nombre:
        lista.insert(tk.END, f"{nombre} - {edad} años - {genero}")
        entry_nombre.delete(0, tk.END)
    else:
        messagebox.showwarning("Atención", "Debes ingresar un nombre.")

def eliminar_usuario():
    seleccion = lista.curselection()
    if seleccion:
        lista.delete(seleccion)
    else:
        messagebox.showinfo("Info", "Selecciona un usuario para eliminar.")

def guardar_lista():
    messagebox.showinfo("Guardar Lista", "Función no implementada, solo demostración.")

def cargar_lista():
    messagebox.showinfo("Cargar Lista", "Función no implementada, solo demostración.")

def salir():
    root.quit()

root = tk.Tk()
root.title("Ejercicio 12 - Registro de Usuarios")
root.geometry("400x400")

# Menú
barra_menu = tk.Menu(root)
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Guardar Lista", command=guardar_lista)
menu_archivo.add_command(label="Cargar Lista", command=cargar_lista)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
root.config(menu=barra_menu)

# Widgets principales
tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack(pady=5)

tk.Label(root, text="Edad:").pack()
scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale_edad.pack()

tk.Label(root, text="Género:").pack()
var_genero = tk.StringVar(value="Otro")
tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Masculino").pack()
tk.Radiobutton(root, text="Femenino", variable=var_genero, value="Femenino").pack()
tk.Radiobutton(root, text="Otro", variable=var_genero, value="Otro").pack()

tk.Button(root, text="Añadir", command=añadir_usuario).pack(pady=5)

# Listbox + Scrollbar
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

scroll = tk.Scrollbar(frame_lista)
scroll.pack(side="right", fill="y")

lista = tk.Listbox(frame_lista, width=40, yscrollcommand=scroll.set)
lista.pack()

scroll.config(command=lista.yview)

# Botones inferiores
tk.Button(root, text="Eliminar", command=eliminar_usuario).pack(side="left", padx=10, pady=10)
tk.Button(root, text="Salir", command=salir).pack(side="right", padx=10, pady=10)

root.mainloop()