from Genlab import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import screeninfo
from ventanaPA import *

def mostrar_matriz(matriz):
    size = (len(matriz[0])*40, len(matriz)*40)
    imagen = Image.new('RGB', size, color=(0, 0, 0))
    draw = ImageDraw.Draw(imagen)
    font_size = 32
    font = ImageFont.truetype("arial.ttf", font_size)
    cuadro_size = 40
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 'x':
                draw.text((j*cuadro_size, i*cuadro_size), 'x', font=font, fill=(255, 0, 0), stroke_width=1, stroke_fill=(255, 0, 0))
            elif matriz[i][j] == '0':
                draw.text((j*cuadro_size, i*cuadro_size), '0', font=font, fill=(0, 255, 0))
            elif matriz[i][j] == 'F':
                draw.text((j*cuadro_size, i*cuadro_size), 'F', font=font, fill=(0, 0, 255), stroke_width=2, stroke_fill=(0, 0, 255))
            elif matriz[i][j] == 'I':
                draw.text((j*cuadro_size, i*cuadro_size), 'I', font=font, fill=(0, 0, 255), stroke_width=2, stroke_fill=(0, 0, 255))
    # Guarda la imagen 
    imagen.save("temp.png")


matriz = generateMaze()
height = 10
width = 10
printMaze(matriz,height,width)
mostrar_matriz(matriz)

# Crea una ventana con un botón para generar solución
ventana = tk.Tk()
ventana.title("Generar Solución")
screen = screeninfo.get_monitors()[0]
width, height = screen.width, screen.height

# Establecer las dimensiones de la ventana principal
ventana.geometry("%dx%d" % (width, height))
ventana.title("Inteligencia Artificial 1")

# Carga la imagen en un objeto PhotoImage de Tkinter
imagen = ImageTk.PhotoImage(Image.open("temp.png"))

# Crea un widget Label para mostrar la imagen
label_imagen = tk.Label(ventana, image=imagen)
label_imagen.pack(pady=100)

# Define la función que se llamará cuando se presione el botón
def nuevoLaberinto():
    print("Generando nuevo laberinto...")
    # Generar la nueva matriz
    global matriz 
    matriz = generateMaze()
    # Mostrar la nueva matriz en una imagen y guardarla en un archivo temporal
    mostrar_matriz(matriz)
    # Actualizar el objeto PhotoImage con la nueva imagen
    imagen = ImageTk.PhotoImage(Image.open("temp.png"))
    label_imagen.configure(image=imagen)
    label_imagen.image = imagen  # Esto es necesario para evitar errores de garbage collection

def mostrarArbol(alg):
    global matriz
    mostrar_arbol(matriz,alg)

def mostrar_Pasos(alg):
    global matriz
    mostrarPasos(matriz,alg)


def mostrar_Laberinto(algoritmo):
    global matriz, imgLaberinto, imgLaberintoPP
    mostrarLaberintoSolucion(matriz,algoritmo)
    ventanaLaberinto = tk.Toplevel(ventana)
    if (algoritmo == 0): 
        ventanaLaberinto.title("LABERINTO: PRIMERO PROFUNDIDAD")
        imgLaberinto = ImageTk.PhotoImage(Image.open("PA.png"))
        label_imagen = tk.Label(ventanaLaberinto, image=imgLaberinto)
    else: 
        ventanaLaberinto.title("LABERINTO: PRIMERO PROFUNDIDAD")
        imgLaberintoPP = ImageTk.PhotoImage(Image.open("PP.png"))
        label_imagen = tk.Label(ventanaLaberinto, image=imgLaberintoPP)
    
    label_imagen.pack(pady=100)
    ventanaLaberinto.mainloop()

#Botones
boton_generar = tk.Button(ventana, text="Generar nuevo laberinto", command=nuevoLaberinto)
boton_generar.pack()

boton_mostrar = tk.Button(ventana, text="Mostrar árbol PA", command=lambda: mostrarArbol(0))
boton_mostrar.pack(padx=10, pady=10)

boton_mostrarPasos = tk.Button(ventana, text="Mostrar pasos PA", command=lambda: mostrar_Pasos(0))
boton_mostrarPasos.pack(padx=10, pady=10)

boton_mostrar = tk.Button(ventana, text="Mostrar árbol PP", command=lambda: mostrarArbol(1))
boton_mostrar.pack(padx=10, pady=10)

boton_mostrarPasos = tk.Button(ventana, text="Mostrar pasos PP", command=lambda: mostrar_Pasos(1))
boton_mostrarPasos.pack(padx=10, pady=10)

boton_mostrarPasos = tk.Button(ventana, text="Mostrar laberinto PA", command=lambda: mostrar_Laberinto(0))
boton_mostrarPasos.pack(padx=10, pady=10)

boton_mostrarPasos = tk.Button(ventana, text="Mostrar laberinto PP", command=lambda: mostrar_Laberinto(1))
boton_mostrarPasos.pack(padx=10, pady=10)


def eliminar_imagen():
    if os.path.exists("imgPrimeroAmplitud.png"):
        os.remove("imgPrimeroAmplitud.png")
    if os.path.exists("imgPrimeroProfundidad.png"):
        os.remove("imgPrimeroProfundidad.png")
    if os.path.exists("temp.png"):
        os.remove("temp.png")
    if os.path.exists("PA.png"):
        os.remove("PA.png")
    if os.path.exists("PP.png"):
        os.remove("PP.png")
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", eliminar_imagen)

ventana.mainloop()
