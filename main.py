from Genlab import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import screeninfo
from ventanaPA import *
from tkinter import ttk


#no se utiliza!! 
# def mostrar_matriz(matriz):
#     size = (len(matriz[0])*20, len(matriz)*20)
#     # size = (200,200)
#     imagen = Image.new('RGB', size, color=(0, 0, 0))
#     # imagen = imagen.resize((300,300), resample=Image.BICUBIC)
#     draw = ImageDraw.Draw(imagen)
#     # font_size = 32
#     font_size = 16
#     font = ImageFont.truetype("arial.ttf", font_size)
#     # cuadro_size = 40
#     cuadro_size = 20
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
#     # Guarda la imagen 
#     imagen.save("temp.png")

def dibujar_laberinto(laberinto):
    alto = len(laberinto)
    ancho = len(laberinto[0])
    tamano_celda = 20  
    alto_imagen = alto * tamano_celda + 1
    ancho_imagen = ancho * tamano_celda + 1

    imagen = Image.new("RGB", (ancho_imagen, alto_imagen), color=(255, 255, 255))
    draw = ImageDraw.Draw(imagen)

    for fila in range(alto):
        for columna in range(ancho):
            celda = laberinto[fila][columna]
            x1 = columna * tamano_celda
            y1 = fila * tamano_celda
            x2 = x1 + tamano_celda
            y2 = y1 + tamano_celda

            if celda == 'x':  #pared
                draw.rectangle((x1, y1, x2, y2), fill=(0, 0, 0))
            elif celda == '0':  #espacio libre
                draw.rectangle((x1, y1, x2, y2), fill=(255, 250, 205))
            elif celda == 'F': 
                draw.rectangle((x1, y1, x2, y2), fill=(255, 0, 255)) #final
            elif celda == 'I': 
                draw.rectangle((x1, y1, x2, y2), fill=(153, 50, 204)) #inicio
            draw.line([(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1, y1)], fill=(0, 0, 0), width=1)

    imagen.save("temp.png")


matriz = generateMaze()
height = 10
width = 10
printMaze(matriz,height,width)
dibujar_laberinto(matriz)

ventana = tk.Tk()
screen = screeninfo.get_monitors()[0]
width, height = screen.width, screen.height
# width = ventana.winfo_screenwidth()
# height = ventana.winfo_screenheight()
# x = (width - ventana.winfo_reqwidth()) // 2
# y = (height - ventana.winfo_reqheight()) // 2

# Establecer las dimensiones de la ventana principal
ventana.geometry("%dx%d" % (width, height))
# ventana.geometry(f"{x}x{y}")
ventana.title("Inteligencia Artificial 1")

notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand=True)


# Definir estilo para las solapas
style = ttk.Style()
style.theme_create("custom_style", parent="alt", settings={
    "TNotebook": {
        "configure": {"background": "white"}
    },
    "TNotebook.Tab": {
        "configure": {"background": "white", "foreground": "black"},
        "map": {
            "background": [
                ("selected", "light blue"),
                ("!selected", "white")
            ],
            "foreground": [
                ("selected", "black"),
                ("!selected", "black")
            ]
        }
    },
    "TFrame": {
        "configure": {"background": "white"}
    }
})
style.theme_use("custom_style")
style.configure("TNotebook.Tab", font=("Arial", 14))

# Crear las solapas
inicio_tab = ttk.Frame(notebook)
ayuda_tab = ttk.Frame(notebook)

# Agregar las solapas al notebook
notebook.add(inicio_tab, text='    Inicio    ')
notebook.add(ayuda_tab, text='    Ayuda    ')


tk.Label(inicio_tab, text=' LABERINTO GENERADO ', font=("Arial", 14)).pack(pady=20)


# Carga la imagen en un objeto PhotoImage de Tkinter
imagen = ImageTk.PhotoImage(Image.open("temp.png"))

# Crea un widget Label para mostrar la imagen
label_imagen = tk.Label(inicio_tab, image=imagen)
label_imagen.pack(pady=20)

def seleccionarSentido():
    if opcion.get() == 1:
        print("Opción 1 seleccionada")
    elif opcion.get() == 2:
        print("Opción 2 seleccionada")

def nuevoLaberinto():
    print("Generando nuevo laberinto...")
    global matriz 
    matriz = generateMaze()
    dibujar_laberinto(matriz)
    imagen = ImageTk.PhotoImage(Image.open("temp.png"))
    label_imagen.configure(image=imagen)
    label_imagen.image = imagen  

def mostrarArbol(alg):
    global matriz
    mostrar_arbol(matriz,alg, opcion.get())

def mostrar_Pasos(alg):
    global matriz
    mostrarPasos(matriz,alg,opcion.get())

def compararArboles():
    global matriz
    arbolBusqueda, por_visitar, texto = generar_laberinto_y_arbol(matriz,0,opcion.get())
    generarArbol(arbolBusqueda,por_visitar,0)
    arbolBusqueda, por_visitar, texto = generar_laberinto_y_arbol(matriz,1,opcion.get())
    generarArbol(arbolBusqueda,por_visitar,1)
    ventanaArboles = tk.Toplevel(ventana)
    ventanaArboles.title("ARBOLES")
    
    contenedorArbol = tk.Frame(ventanaArboles)
    contenedorArbol.pack(padx=10, pady=10)
    arbolPA= Image.open("imgPrimeroAmplitud.png")
    arbolPA = arbolPA.resize((700, 700), Image.LANCZOS)
    arbolPA = ImageTk.PhotoImage(arbolPA)
    frame_izq = tk.Frame(contenedorArbol)
    frame_izq.grid(row=0, column=0, padx=10, pady=10)
    label_imagen = tk.Label(frame_izq, image=arbolPA)
    label_imagen.pack()

    titulo_izquierdo = tk.Label(frame_izq, text="Árbol Algoritmo Primero Amplitud", font=("Arial", 14))
    titulo_izquierdo.pack(pady=10)
    
    arbolPP = Image.open("imgPrimeroProfundidad.png")
    arbolPP = arbolPP.resize((400, 700), Image.LANCZOS)
    arbolPP = ImageTk.PhotoImage(arbolPP)
    frame_der = tk.Frame(contenedorArbol)
    frame_der.grid(row=0, column=1, padx=10, pady=10)
    label_imagen2 = tk.Label(frame_der, image=arbolPP)
    label_imagen2.pack()

    titulo_derecho = tk.Label(frame_der, text="Árbol Algoritmo Primero Profundidad", font=("Arial", 14))
    titulo_derecho.pack(pady=10)

    ventanaArboles.mainloop()


def mostrar_Laberinto(algoritmo):
    global matriz, imgLaberinto, imgLaberintoPP
    ventanaLaberinto = tk.Toplevel(ventana)
    ventanaLaberinto.title("LABERINTO")
    
    contenedor = tk.Frame(ventanaLaberinto)
    contenedor.pack(padx=10, pady=10)

    if algoritmo == 0:
        dibujarLaberintoSolucion(matriz, algoritmo,opcion.get())
        ventanaLaberinto.title("LABERINTO: PRIMERO AMPLITUD")
        imgLaberinto = ImageTk.PhotoImage(Image.open("PA.png"))
        frame_izquierdo = tk.Frame(contenedor)
        frame_izquierdo.pack(side="left", padx=10, pady=10)
        label_imagen = tk.Label(frame_izquierdo, image=imgLaberinto)
        label_imagen.pack()

        titulo_izquierdo = tk.Label(frame_izquierdo, text="Laberinto Algoritmo Primero Amplitud", font=("Arial", 14))
        titulo_izquierdo.pack(pady=10)
    elif algoritmo == 1:
        dibujarLaberintoSolucion(matriz, algoritmo,opcion.get())
        ventanaLaberinto.title("LABERINTO: PRIMERO PROFUNDIDAD")
        imgLaberintoPP = ImageTk.PhotoImage(Image.open("PP.png"))
        frame_derecho = tk.Frame(contenedor)
        frame_derecho.pack(side="right", padx=10, pady=10)
        label_imagen = tk.Label(frame_derecho, image=imgLaberintoPP)
        label_imagen.pack()

        titulo_derecho = tk.Label(frame_derecho, text="Laberinto Algoritmo Primero Profundidad", font=("Arial", 14))
        titulo_derecho.pack(pady=10)
    elif algoritmo == 3:
        dibujarLaberintoSolucion(matriz, 0,opcion.get())
        dibujarLaberintoSolucion(matriz, 1,opcion.get())
        ventanaLaberinto.title("COMPARAR ALGORITMOS")
        imgLaberinto = ImageTk.PhotoImage(Image.open("PA.png"))
        frame_izquierdo = tk.Frame(contenedor)
        frame_izquierdo.grid(row=0, column=0, padx=10, pady=10)
        label_imagen = tk.Label(frame_izquierdo, image=imgLaberinto)
        label_imagen.pack()

        titulo_izquierdo = tk.Label(frame_izquierdo, text="Laberinto Algoritmo Primero Amplitud", font=("Arial", 14))
        titulo_izquierdo.pack(pady=10)

        imgLaberintoPP = ImageTk.PhotoImage(Image.open("PP.png"))
        frame_derecho = tk.Frame(contenedor)
        frame_derecho.grid(row=0, column=1, padx=10, pady=10)
        label_imagen2 = tk.Label(frame_derecho, image=imgLaberintoPP)
        label_imagen2.pack()

        titulo_derecho = tk.Label(frame_derecho, text="Laberinto Algoritmo Primero Profundidad", font=("Arial", 14))
        titulo_derecho.pack(pady=10)

    ventanaLaberinto.mainloop()

#Botones
#Botón para generar nuevo laberinto
tk.Button(inicio_tab, text='Generar nuevo laberinto', command=nuevoLaberinto, width=35).pack(pady=(20))

# Crear el frame para las opciones
frame_opciones = tk.Frame(inicio_tab)
frame_opciones.pack(pady=(5))

# Variable para almacenar la opción seleccionada
opcion = tk.IntVar(value=1)

# Crear los Radiobutton con las opciones
tk.Label(frame_opciones, text='Sentido de búsqueda para la solución', font=("Arial", 14)).pack(pady=(5,0))

opcion_1 = tk.Radiobutton(frame_opciones, text="Sentido horario", variable=opcion, value=1, command=seleccionarSentido)
opcion_1.pack(pady=5)

opcion_2 = tk.Radiobutton(frame_opciones, text="Sentido antihorario", variable=opcion, value=2, command=seleccionarSentido)
opcion_2.pack(pady=0)

#Crea los frames para agrupar los botones
frame_amplitud = tk.LabelFrame(inicio_tab, text=' Algoritmo búsqueda primero amplitud ',font=("Arial", 14))
frame_amplitud.configure(bg='white')
frame_amplitud.pack(side='left', padx=10, pady=10, fill='x', expand=True)

frame_profundidad = tk.LabelFrame(inicio_tab, text=' Algoritmo búsqueda primero profundidad ',font=("Arial", 14))
frame_profundidad.pack(side='left', padx=10, pady=10, fill='x', expand=True)
frame_profundidad.configure(bg='white')

frame_comparaciones = tk.LabelFrame(inicio_tab, text=' Comparaciones',font=("Arial", 14))
frame_comparaciones.configure(bg='white')
frame_comparaciones.pack(side='left', padx=10, pady=10, fill='x', expand=True)

#Botones del frame_amplitud
tk.Button(frame_amplitud, text='Solución árbol primero amplitud', command=lambda: mostrarArbol(0), width=35).pack(pady=(10, 0))
tk.Button(frame_amplitud, text='Solución laberinto primero amplitud', command=lambda: mostrar_Laberinto(0), width=35).pack(pady=(10, 0))
tk.Button(frame_amplitud, text='Mostrar pasos primero amplitud', command=lambda: mostrar_Pasos(0), width=35).pack(pady=(10, 10))

#Botones del frame_profundidad
tk.Button(frame_profundidad, text='Solución árbol primero profundidad', command=lambda: mostrarArbol(1), width=35).pack(pady=(0, 0))
tk.Button(frame_profundidad, text='Solución laberinto profundidad', command=lambda: mostrar_Laberinto(1), width=35).pack(pady=(10, 0))
tk.Button(frame_profundidad, text='Mostrar pasos primero profundidad', command=lambda: mostrar_Pasos(1), width=35).pack(pady=(10, 10))

#Botones del frame_comparaciones
tk.Button(frame_comparaciones, text='Comparar árboles de búsqueda',  command=lambda: compararArboles(),width=35).pack(pady=(0, 0))
tk.Button(frame_comparaciones, text='Comparar laberintos solución',command=lambda: mostrar_Laberinto(3), width=35).pack(pady=(10, 10))

#Contenido de la solapa "Ayuda"
tk.Label(ayuda_tab, text='REFERENCIAS',font=("Arial", 14)).pack()

#Frame en Ayuda de Laberinto
frame_ref_laberinto = tk.LabelFrame(ayuda_tab, text='Sobre el LABERINTO: ', font=("Arial", 14))
frame_ref_laberinto.configure(bg='white')
frame_ref_laberinto.pack(side='left', padx=10, pady=10, fill='x', expand=True)

tk.Label(frame_ref_laberinto, text='Laberinto: ',bg='white').pack(pady=(0, 0))
img_lab = tk.PhotoImage(file="img/laberintoGenerado.png")
tk.Label(frame_ref_laberinto, image=img_lab).pack()

tk.Label(frame_ref_laberinto, text='Inicio: ',bg='white').pack(pady=(0, 0))
img_lab_inicio = tk.PhotoImage(file="img/inicio_lab.PNG")
tk.Label(frame_ref_laberinto, image=img_lab_inicio).pack()

tk.Label(frame_ref_laberinto, text='Fin: ',bg='white').pack(pady=(0, 0))
img_lab_fin = tk.PhotoImage(file="img/fin_lab.PNG")
tk.Label(frame_ref_laberinto, image=img_lab_fin).pack()

tk.Label(frame_ref_laberinto, text='Lugar accesible: ',bg='white').pack(pady=(0, 0))
img_lab_camino = tk.PhotoImage(file="img/camino_lab.PNG")
tk.Label(frame_ref_laberinto, image=img_lab_camino).pack()

tk.Label(frame_ref_laberinto, text='Lugar bloqueado: ',bg='white').pack(pady=(0, 0))
img_lab_bloqueado = tk.PhotoImage(file="img/bloqueado_lab.PNG")
tk.Label(frame_ref_laberinto, image=img_lab_bloqueado).pack()

#Frame en Ayuda de los Árboles
frame_ref_arbol = tk.LabelFrame(ayuda_tab, text='Sobre los ÁRBOLES: ', font=("Arial", 14))
frame_ref_arbol.configure(bg='white')
frame_ref_arbol.pack(side='left', padx=10, pady=10, fill='x', expand=True)

tk.Label(frame_ref_arbol, text='Nodo Inicio: ',bg='white').pack(pady=(0, 0))
img_arb_inicio = tk.PhotoImage(file="img/inicio_arb.PNG")
tk.Label(frame_ref_arbol, image=img_arb_inicio).pack()

tk.Label(frame_ref_arbol, text='Nodo Fin: ',bg='white').pack(pady=(0, 0))
img_arb_fin = tk.PhotoImage(file="img/fin_arb.PNG")
tk.Label(frame_ref_arbol, image=img_arb_fin).pack()

tk.Label(frame_ref_arbol, text='Nodo expandido pero no camino solución: ',bg='white').pack(pady=(0, 0))
img_arb_expansion = tk.PhotoImage(file="img/expansion_arb.PNG")
tk.Label(frame_ref_arbol, image=img_arb_expansion).pack()

tk.Label(frame_ref_arbol, text='Nodo expandido y camino solución: ',bg='white').pack(pady=(0, 0))
img_arb_solucion = tk.PhotoImage(file="img/solucion_arb.PNG")
tk.Label(frame_ref_arbol, image=img_arb_solucion).pack()

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
