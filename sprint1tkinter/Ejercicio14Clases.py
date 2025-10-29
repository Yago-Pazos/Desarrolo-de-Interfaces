import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 14 - Registro con Clases")
        self.root.geometry("400x400")


        menu = tk.Menu(self.root)
        archivo = tk.Menu(menu, tearoff=0)
        archivo.add_command(label="Guardar Lista", command=self.guardar_lista)
        archivo.add_command(label="Cargar Lista", command=self.cargar_lista)
        archivo.add_separator()
        archivo.add_command(label="Salir", command=self.salir)
        menu.add_cascade(label="Archivo", menu=archivo)
        self.root.config(menu=menu)


        tk.Label(root, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack(pady=5)

        tk.Label(root, text="Edad:").pack()
        self.scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.scale_edad.pack()

        tk.Label(root, text="Género:").pack()
        self.var_genero = tk.StringVar(value="Otro")
        for texto in ["Masculino", "Femenino", "Otro"]:
            tk.Radiobutton(root, text=texto, variable=self.var_genero, value=texto).pack()

        tk.Button(root, text="Añadir", command=self.añadir_usuario).pack(pady=5)

        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)

        self.scroll = tk.Scrollbar(frame_lista)
        self.scroll.pack(side="right", fill="y")

        self.lista = tk.Listbox(frame_lista, width=40, yscrollcommand=self.scroll.set)
        self.lista.pack()

        self.scroll.config(command=self.lista.yview)

        tk.Button(root, text="Eliminar", command=self.eliminar_usuario).pack(side="left", padx=10, pady=10)
        tk.Button(root, text="Salir", command=self.salir).pack(side="right", padx=10, pady=10)

    def añadir_usuario(self):
        nombre = self.entry_nombre.get()
        edad = self.scale_edad.get()
        genero = self.var_genero.get()
        if nombre:
            self.lista.insert(tk.END, f"{nombre} - {edad} años - {genero}")
            self.entry_nombre.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "Debes ingresar un nombre.")

    def eliminar_usuario(self):
        seleccion = self.lista.curselection()
        if seleccion:
            self.lista.delete(seleccion)
        else:
            messagebox.showinfo("Info", "Selecciona un usuario para eliminar.")

    def guardar_lista(self):
        messagebox.showinfo("Guardar", "Función no implementada.")

    def cargar_lista(self):
        messagebox.showinfo("Cargar", "Función no implementada.")

    def salir(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()