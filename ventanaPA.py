import tkinter as tk
from PrimeroAmplitud import *
from PIL import ImageTk
from networkx.drawing.nx_agraph import graphviz_layout
import screeninfo
import os

# Define la función para generar el laberinto y el árbol
def generar_laberinto_y_arbol():
   matriz = generateMaze()
   height = 10
   width = 10
   printMaze(matriz,height,width)
   arbolBusqueda = PrimeroAmplitud(matriz)
   return arbolBusqueda 

def generarArbol(arbolBusqueda):
	g = Graph(engine='sfdp')
	g = graphviz.Digraph(format='png')
	for n in arbolBusqueda:
		nodo_padre = (n.padre.fila,n.padre.columna)
		nodo_hijo = (n.hijo.fila,n.hijo.columna)
		g.edge(str(nodo_padre), str(nodo_hijo))
	g.render('imgPrimeroAmplitud')


def mostrar_arbol():
     arbolBusqueda = generar_laberinto_y_arbol()
     generarArbol(arbolBusqueda)
     nombre_archivo = 'imgPrimeroAmplitud.png'

     img = Image.open(nombre_archivo)
     img = img.resize((700, 700), Image.LANCZOS)
     img = ImageTk.PhotoImage(img)
     ventana = tk.Toplevel()
     ventana.title("Árbol de búsqueda")
     panel = tk.Label(ventana, image=img)
     panel.image = img
     panel.pack()

# Crear la ventana principal
root = tk.Tk()
screen = screeninfo.get_monitors()[0]
width, height = screen.width, screen.height

# Establecer las dimensiones de la ventana principal
root.geometry("%dx%d" % (width, height))
root.title("Inteligencia Artificial 1")

# Crea el botón "Mostrar árbol" y lo añade a la ventana
boton_mostrar = tk.Button(root, text="Mostrar árbol", command=mostrar_arbol)
boton_mostrar.pack(padx=10, pady=10)

# Definir una función para eliminar el archivo de imagen
def eliminar_imagen():
    if os.path.exists("imgPrimeroAmplitud.png"):
        os.remove("imgPrimeroAmplitud.png")
    root.destroy()

# Vincular la función eliminar_imagen a la señal de cierre de la ventana principal
root.protocol("WM_DELETE_WINDOW", eliminar_imagen)

root.mainloop()