import tkinter as tk
from PrimeroAmplitud import *
from PIL import Image, ImageTk
from networkx.drawing.nx_agraph import graphviz_layout
import screeninfo
import os

# Define la función para generar el laberinto y el árbol
def generar_laberinto_y_arbol():
   matriz = generateMaze()
   height = 10
   width = 10
   printMaze(matriz,height,width)
   arbolBusqueda, por_visitar= primeroAmplitud(matriz)
   cont = 0
   for e in arbolBusqueda:
                    print("TIEMPO: ",e.tiempo,"Nodo:",e.padre.fila,e.padre.columna) #ESTO NO ANDA COMO DEBERIA :c
                    cont = cont+1
   return arbolBusqueda, por_visitar

def generarArbol(arbolBusqueda, por_visitar):
    g = Graph(engine='sfdp')
    g = graphviz.Digraph(format='png')
    for n in arbolBusqueda:
        nodo_padre = (n.padre.fila,n.padre.columna)
        nodo_hijo = (n.hijo.fila,n.hijo.columna)
        g.edge(str(nodo_padre), str(nodo_hijo))
        if nodo_padre == (9,9):
            g.node(str(nodo_padre), style='filled', fillcolor='blue')
        if nodo_hijo == (0,0):
            g.node(str(nodo_hijo), style='filled', fillcolor='green')
        for x in por_visitar:
             if(n.hijo == x ):
                  g.node(str(nodo_hijo), style='filled', fillcolor='green')
    g.render('imgPrimeroAmplitud')


def mostrar_arbol():
     arbolBusqueda, por_visitar = generar_laberinto_y_arbol()
     generarArbol(arbolBusqueda, por_visitar)
     nombre_archivo = 'imgPrimeroAmplitud.png'

     img = Image.open(nombre_archivo)
     img = img.resize((700, 700), Image.LANCZOS)
     img = ImageTk.PhotoImage(img)
     ventana = tk.Toplevel()
     ventana.title("ALGORITMO PRIMERO AMPLITUD")

     # Crear un canvas para contener la imagen y agregar un scrollbar
     canvas = tk.Canvas(ventana, width=700, height=700)
     scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
     scrollable_frame = tk.Frame(canvas)

     # Configurar el canvas y el scrollbar
     canvas.configure(yscrollcommand=scrollbar.set)
     canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
     scrollbar.pack(side="right", fill="y")
     canvas.pack(side="left", fill="both", expand=True)

     # Agregar la imagen al scrollable_frame
     panel = tk.Label(scrollable_frame, image=img)
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