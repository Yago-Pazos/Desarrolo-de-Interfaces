import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 10 - Scrollbar")
root.geometry("400x300")

texto = tk.Text(root, wrap="word", height=10)
texto.pack(side="left", fill="both", expand=True)

scroll = tk.Scrollbar(root, command=texto.yview)
scroll.pack(side="right", fill="y")

texto.config(yscrollcommand=scroll.set)


texto.insert("1.0", ("Hola\n" * 30))

root.mainloop()