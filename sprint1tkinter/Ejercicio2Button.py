import tkinter as tk

def mostrar_mensaje():
    label.config(text="¡Has presionado el botón de mensaje!")

def cerrar_ventana():
    root.quit()

root = tk.Tk()
root.title("Ejercicio 2 - Button")
root.geometry("300x200")

label = tk.Label(root, text="")
label.pack(pady=20)

boton1 = tk.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
boton1.pack(pady=5)

boton2 = tk.Button(root, text="Cerrar ventana", command=cerrar_ventana)
boton2.pack(pady=5)

root.mainloop()