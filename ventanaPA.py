import tkinter as tk
from PrimeroAmplitud import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
from networkx.drawing.nx_agraph import graphviz_layout
import screeninfo
import os

def generar_laberinto_y_arbol(matriz,algoritmo,sentido):
    if algoritmo:
        arbolBusqueda, por_visitar, texto= primeroProfundidad(matriz,sentido)
    else:
        arbolBusqueda, por_visitar, texto= primeroAmplitud(matriz,sentido)
    return arbolBusqueda, por_visitar, texto

def generarArbol(arbolBusqueda,por_visitar,algoritmo):
    g = Graph(engine='sfdp')
    g = graphviz.Digraph(format='png')
    for n in arbolBusqueda:
        nodo_padre = (n.padre.fila,n.padre.columna)
        nodo_hijo = (n.hijo.fila,n.hijo.columna)
        g.edge(str(nodo_padre), str(nodo_hijo))
        if nodo_padre == (9,9):
            g.node(str(nodo_padre), style='filled', fillcolor='#9932CC')
        for x in por_visitar:
             if(n.hijo == x ):
                  g.node(str(nodo_hijo), style='filled', fillcolor='green')
        if (n.hijo == nodo(0,0)):
            g.node(str(nodo_hijo), style='filled', fillcolor='#FF00FF')
    if algoritmo:
        g.render('imgPrimeroProfundidad')
    else:
        g.render('imgPrimeroAmplitud')


def mostrar_arbol(matriz, algoritmo, sentido):
    arbolBusqueda, por_visitar, texto = generar_laberinto_y_arbol(matriz, algoritmo, sentido)
    generarArbol(arbolBusqueda, por_visitar, algoritmo)
    if algoritmo:
        nombre_archivo = 'imgPrimeroProfundidad.png'
        img = Image.open(nombre_archivo)
        img = img.resize((400, 700), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
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

    canvas = tk.Canvas(ventana, width=700, height=700)
    scrollable_frame = tk.Frame(canvas)

    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.pack(side="left", fill="both", expand=True)

    panel = tk.Label(scrollable_frame, image=img)
    panel.image = img
    panel.pack()

    contenedor = tk.Frame(ventana)
    contenedor.pack(fill="both", expand=True)
    frame_titulo = tk.Frame(contenedor)
    frame_titulo.pack(fill="x")
    titulo = tk.Label(frame_titulo, text="Pasos para encontrar la salida", font=("Arial", 14))
    titulo.pack(pady=10)
    frame_texto = tk.Frame(contenedor, width=500, height=100)
    frame_texto.pack(side="left")

    # Agregar scrollbar al widget de texto
    scrollbar_texto = tk.Scrollbar(frame_texto)
    scrollbar_texto.pack(side="right", fill="y")

    widget_texto = tk.Text(frame_texto)
    widget_texto.pack(fill="both", expand=True)

    # Vincular el scrollbar con el widget de texto
    scrollbar_texto.configure(command=widget_texto.yview)
    widget_texto.configure(yscrollcommand=scrollbar_texto.set)

    for linea in texto:
        widget_texto.insert("end", linea + "\n")



def mostrarPasos(matriz,algoritmo,sentido):
    arbolBusqueda, por_visitar, texto = generar_laberinto_y_arbol(matriz,algoritmo,sentido)
    ventana = Tk()
    if (algoritmo == 0):
        ventana.title("PASOS: PRIMERO AMPLITUD")
    else: 
        ventana.title("PASOS: PRIMERO PROFUNDIDAD")
    widget_texto = Text(ventana, height=30, width=50, state="disabled")
    widget_texto.pack()
    widget_texto.config(state="normal")
    for linea in texto:
        widget_texto.insert("end", linea + "\n")

    widget_texto.config(state="disabled")

    ventana.mainloop()

imagen_tk = None

#no se utiliza!!
# def mostrarLaberintoSolucion(matriz,algoritmo,sentido):
#     global imagen_tk
#     arbolBusqueda, por_visitar, texto = generar_laberinto_y_arbol(matriz, algoritmo,sentido)
#     size = (len(matriz[0]) * 40, len(matriz) * 40)
#     imagen = Image.new('RGB', size, color=(0, 0, 0))
#     draw = ImageDraw.Draw(imagen)
#     font_size = 32
#     font = ImageFont.truetype("arial.ttf", font_size)
#     cuadro_size = 40

#     for i in range(len(matriz)):
#         for j in range(len(matriz[0])):
#             if matriz[i][j] == 'x':
#                 draw.text((j*cuadro_size, i*cuadro_size), 'x', font=font, fill=(255, 0, 0), stroke_width=1, stroke_fill=(255, 0, 0))
#             elif matriz[i][j] == '0':
#                 draw.text((j*cuadro_size, i*cuadro_size), '0', font=font, fill=(0, 255, 0))
#             elif matriz[i][j] == 'F':
#                 draw.text((j*cuadro_size, i*cuadro_size), 'F', font=font, fill=(0, 0, 255), stroke_width=2, stroke_fill=(0, 0, 255))
#             elif matriz[i][j] == 'I':
#                 draw.text((j*cuadro_size, i*cuadro_size), 'I', font=font, fill=(0, 0, 255), stroke_width=2, stroke_fill=(0, 0, 255))
#             if (nodo(i, j) in por_visitar and nodo(i,j)!=nodo(0,0)and nodo(i,j)!=nodo(9,9)):
#                draw.text((j*cuadro_size, i*cuadro_size), '//', font=font, fill=(255, 255, 0), stroke_width=2,stroke_fill=(255, 255, 0))

#     if (algoritmo == 0): imagen.save("PA.png")
#     else: imagen.save("PP.png")


def dibujarLaberintoSolucion(matriz,algoritmo,sentido):
    global imagen_tk
    arbolBusqueda, por_visitar, texto = generar_laberinto_y_arbol(matriz, algoritmo,sentido)
    alto = len(matriz)
    ancho = len(matriz[0])
    tamano_celda = 20
    alto_imagen = alto * tamano_celda + 1
    ancho_imagen = ancho * tamano_celda + 1

    imagen = Image.new("RGB", (ancho_imagen, alto_imagen), color=(255, 255, 255))
    draw = ImageDraw.Draw(imagen)

    for fila in range(alto):
        for columna in range(ancho):
            celda = matriz[fila][columna]
            x1 = columna * tamano_celda
            y1 = fila * tamano_celda
            x2 = x1 + tamano_celda
            y2 = y1 + tamano_celda

            if celda == 'x':  # Pared
                draw.rectangle((x1, y1, x2, y2), fill=(0, 0, 0))
            elif celda == '0':  # Espacio libre
                if nodo(fila, columna) in por_visitar:
                    draw.rectangle((x1, y1, x2, y2), fill=(0, 255, 0))  # Color para por_visitar
                else:
                    draw.rectangle((x1, y1, x2, y2), fill=(255, 250, 205))
            elif celda == 'F': 
                draw.rectangle((x1, y1, x2, y2), fill=(255, 0, 255)) #final
            elif celda == 'I': 
                draw.rectangle((x1, y1, x2, y2), fill=(153, 50, 204)) #inicio

            draw.line([(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1, y1)], fill=(0, 0, 0), width=1)

    if (algoritmo == 0): imagen.save("PA.png")
    else: imagen.save("PP.png")


