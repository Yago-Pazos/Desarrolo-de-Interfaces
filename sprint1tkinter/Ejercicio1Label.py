import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 1 - Labels y Botón")
ventana.geometry("300x200")  # Tamaño de la ventana

# --- Etiquetas ---
label1 = tk.Label(ventana, text="¡Bienvenido a mi ventana!")
label1.pack(pady=10)

label2 = tk.Label(ventana, text="Yago Pazos Lema")
label2.pack(pady=10)

label3 = tk.Label(ventana, text="Texto inicial")
label3.pack(pady=10)

# --- Función para cambiar el texto de la tercera etiqueta ---
def cambiar_texto():
    label3.config(text="Nuevo texto")

# --- Botón ---
boton = tk.Button(ventana, text="Cambiar texto", command=cambiar_texto)
boton.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
