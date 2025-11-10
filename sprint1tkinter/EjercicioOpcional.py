"""
Juego Piedra-Papel-Tijera (versión básica con Tkinter)
Autor: [Tu Nombre Completo]
Descripción:
Juego clásico contra la máquina al mejor de 5 (primero que llega a 3 puntos).
"""

import tkinter as tk
from tkinter import messagebox
import random

#Logica

def jugar(eleccion_jugador):
    if partida_finalizada.get():
        messagebox.showinfo("Fin de partida", "Pulsa 'Nuevo juego' para volver a jugar.")
        return

    eleccion_pc = random.choice(["Piedra", "Papel", "Tijera"])
    var_pc.set(f"Máquina: {eleccion_pc}")

    # Comparar elecciones
    if eleccion_jugador == eleccion_pc:
        var_resultado.set("Empate. No cuenta esta ronda.")
        return

    if (eleccion_jugador == "Piedra" and eleccion_pc == "Tijera") or \
       (eleccion_jugador == "Papel" and eleccion_pc == "Piedra") or \
       (eleccion_jugador == "Tijera" and eleccion_pc == "Papel"):
        puntos_jugador.set(puntos_jugador.get() + 1)
        var_resultado.set("Ganaste esta ronda.")
    else:
        puntos_pc.set(puntos_pc.get() + 1)
        var_resultado.set("Perdiste esta ronda.")

    comprobar_ganador()

def comprobar_ganador():
    if puntos_jugador.get() == 3:
        var_resultado.set("¡Has ganado la partida!")
        partida_finalizada.set(True)
    elif puntos_pc.get() == 3:
        var_resultado.set("Has perdido la partida.")
        partida_finalizada.set(True)

def nuevo_juego():
    puntos_jugador.set(0)
    puntos_pc.set(0)
    var_pc.set("Máquina: ---")
    var_resultado.set("Elige tu jugada para empezar.")
    partida_finalizada.set(False)

def salir():
    root.quit()

#Tkinter

root = tk.Tk()
root.title("Piedra - Papel - Tijera")
root.geometry("300x300")

# Variables
puntos_jugador = tk.IntVar(value=0)
puntos_pc = tk.IntVar(value=0)
var_pc = tk.StringVar(value="Máquina: ---")
var_resultado = tk.StringVar(value="Elige tu jugada para empezar.")
partida_finalizada = tk.BooleanVar(value=False)

# Título
tk.Label(root, text="Piedra - Papel - Tijera", font=("Arial", 14, "bold")).pack(pady=10)

# Marcador
frame_marcador = tk.Frame(root)
frame_marcador.pack()

tk.Label(frame_marcador, text="Jugador").grid(row=0, column=0, padx=20)
tk.Label(frame_marcador, text="Máquina").grid(row=0, column=1, padx=20)

tk.Label(frame_marcador, textvariable=puntos_jugador, font=("Arial", 12)).grid(row=1, column=0)
tk.Label(frame_marcador, textvariable=puntos_pc, font=("Arial", 12)).grid(row=1, column=1)

# Elección del jugador
tk.Label(root, text="Elige tu jugada:", font=("Arial", 10)).pack(pady=10)

frame_botones = tk.Frame(root)
frame_botones.pack()

tk.Button(frame_botones, text="Piedra", width=10, command=lambda: jugar("Piedra")).pack(side="left", padx=5)
tk.Button(frame_botones, text="Papel", width=10, command=lambda: jugar("Papel")).pack(side="left", padx=5)
tk.Button(frame_botones, text="Tijera", width=10, command=lambda: jugar("Tijera")).pack(side="left", padx=5)

# Mostrar elección de la máquina
tk.Label(root, textvariable=var_pc, font=("Arial", 10)).pack(pady=10)

# Resultado de la ronda
tk.Label(root, textvariable=var_resultado, font=("Arial", 11), wraplength=280, justify="center").pack(pady=10)

# Botones de control
frame_control = tk.Frame(root)
frame_control.pack(pady=10)

tk.Button(frame_control, text="Nuevo juego", width=12, command=nuevo_juego).grid(row=0, column=0, padx=5)
tk.Button(frame_control, text="Salir", width=12, command=salir).grid(row=0, column=1, padx=5)

root.mainloop()

