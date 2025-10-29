import tkinter as tk

def dibujar_circulo(event):
    x, y = event.x, event.y
    radio = 15
    canvas.create_oval(x-radio, y-radio, x+radio, y+radio, fill="blue")

def limpiar_canvas(event):
    canvas.delete("all")

root = tk.Tk()
root.title("Ejercicio 13 - Teclado y Raton")
root.geometry("400x300")

canvas = tk.Canvas(root, bg="white", width=400, height=300)
canvas.pack(fill="both", expand=True)

canvas.bind("<Button-1>", dibujar_circulo)
root.bind("c", limpiar_canvas)

root.mainloop()
