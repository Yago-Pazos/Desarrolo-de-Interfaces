import tkinter as tk

def mostrar_fruta():
    seleccion = lista.curselection()
    if seleccion:
        fruta = lista.get(seleccion)
        etiqueta.config(text=f"Fruta seleccionada: {fruta}")

root = tk.Tk()
root.title("Ejercicio 6 - Listbox")
root.geometry("300x200")

lista = tk.Listbox(root)
for fruta in ["Manzana", "Banana", "Naranja"]:
    lista.insert(tk.END, fruta)
lista.pack(pady=10)

tk.Button(root, text="Mostrar fruta", command=mostrar_fruta).pack()
etiqueta = tk.Label(root, text="")
etiqueta.pack(pady=10)

root.mainloop()