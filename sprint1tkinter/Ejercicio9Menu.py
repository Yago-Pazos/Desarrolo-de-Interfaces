import tkinter as tk
from tkinter import messagebox

def abrir_archivo():
    messagebox.showinfo("Abrir", "Función para abrir archivo (no implementada).")

def salir():
    root.quit()

def acerca_de():
    messagebox.showinfo("Acerca de", "Aplicación creada por Yago.")

root = tk.Tk()
root.title("Ejercicio 9 - Menú")
root.geometry("300x200")

# Crear la barra de menús
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

# Menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

root.mainloop()