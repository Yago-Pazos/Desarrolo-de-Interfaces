import tkinter as tk

def dibujar():
    canvas.delete("all")
    try:
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())
        canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=2)
        canvas.create_oval(x1, y1, x2, y2, outline="red", width=2)
    except ValueError:
        pass

root = tk.Tk()
root.title("Ejercicio 7 - Canvas")
root.geometry("400x400")

tk.Label(root, text="x1").pack(); entry_x1 = tk.Entry(root, width=5); entry_x1.pack()
tk.Label(root, text="y1").pack(); entry_y1 = tk.Entry(root, width=5); entry_y1.pack()
tk.Label(root, text="x2").pack(); entry_x2 = tk.Entry(root, width=5); entry_x2.pack()
tk.Label(root, text="y2").pack(); entry_y2 = tk.Entry(root, width=5); entry_y2.pack()

tk.Button(root, text="Dibujar", command=dibujar).pack(pady=5)
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

root.mainloop()