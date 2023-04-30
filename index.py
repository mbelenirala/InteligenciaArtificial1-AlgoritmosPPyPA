import tkinter as tk
from tkinter import ttk
import screeninfo
import tkinter.font as tkFont
from Genlab import *


def imprimir():
    label_saludo.configure(text="¡Hola, mundo!")

def generar_laberinto():
    
    # Crear el widget Text y establecer su tamaño
    text_widget = tk.Text(root, width=10, height=10)

    maze = generateMaze()
    height = 10
    width = 10
    printMaze(maze,height,width)
    printMaze2(maze,height,width,text_widget)

    text_widget.configure(state="disabled")

    # Mostrar el widget
    text_widget.pack(padx=10, pady=10)

# Crear la ventana principal
root = tk.Tk()
screen = screeninfo.get_monitors()[0]
width, height = screen.width, screen.height

# Establecer las dimensiones de la ventana principal
root.geometry("%dx%d" % (width, height))
root.title("Inteligencia Artificial 1")

# Crear un label
label = ttk.Label(root, text="Presiona el botón para imprimir", font=("Arial", 16))
label.pack(pady=10)

# Crear un botón
boton = ttk.Button(root, text="Imprimir", command=imprimir)
boton.pack(pady=10)

# Crear un label para el saludo
label_saludo = ttk.Label(root, text="", font=("Arial", 16))
label_saludo.pack(pady=10)

# Crear el botón
generar = tk.Button(root, text="Generar laberinto", command=generar_laberinto)

# Mostrar el botón
generar.pack(pady=10)

# Iniciar el bucle principal
root.mainloop()