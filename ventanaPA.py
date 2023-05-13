import tkinter as tk
from PrimeroAmplitud import *
from PIL import Image, ImageTk
from networkx.drawing.nx_agraph import graphviz_layout
import screeninfo
import os

# Define la función para generar el laberinto y el árbol
def generar_laberinto_y_arbol(matriz,algoritmo):
    if algoritmo:
        arbolBusqueda, por_visitar, texto= primeroProfundidad(matriz)
    else:
        arbolBusqueda, por_visitar, texto= primeroAmplitud(matriz)
    cont = 0
    #for e in arbolBusqueda:
    #                print("TIEMPO: ",cont,"Nodo:",e.padre.fila,e.padre.columna) #ESTO NO ANDA COMO DEBERIA :c
    #               cont = cont+1
    return arbolBusqueda, por_visitar, texto

def generarArbol(arbolBusqueda,por_visitar,algoritmo):
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
    if algoritmo:
        g.render('imgPrimeroProfundidad')
    else:
        g.render('imgPrimeroAmplitud')


def mostrar_arbol(matriz,algoritmo):
     arbolBusqueda, por_visitar, texto = generar_laberinto_y_arbol(matriz,algoritmo)
     generarArbol(arbolBusqueda,por_visitar,algoritmo)
     if algoritmo:
        nombre_archivo = 'imgPrimeroProfundidad.png'
     else:
        nombre_archivo = 'imgPrimeroAmplitud.png'

     img = Image.open(nombre_archivo)
     img = img.resize((700, 700), Image.LANCZOS)
     img = ImageTk.PhotoImage(img)
     ventana = tk.Toplevel()
     if algoritmo:
        ventana.title("ALGORITMO PRIMERO PROFUNDIDAD")
     else:
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

def mostrarPasos(matriz,algoritmo):
    arbolBusqueda, por_visitar, texto = generar_laberinto_y_arbol(matriz,algoritmo)
    ventana = Tk()
    ventana.title("Texto")
    
    # Crear un widget de Texto
    widget_texto = Text(ventana, height=30, width=50)
    widget_texto.pack()

    # Agregar el contenido de la variable texto al widget de Texto
    for linea in texto:
        widget_texto.insert("end", linea + "\n")

    ventana.mainloop()

