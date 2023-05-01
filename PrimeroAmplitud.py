from Genlab import *
import graphviz
from graphviz import Graph
from PIL import Image
from modelo import *




def PrimeroAmplitud(matriz):
    inicio = nodo(9, 9)
    final = nodo(0, 0)
    visitados = []
    por_visitar = []
    arbolBusqueda = []
    por_visitar.append(inicio)  #se asigna el inicio

    while por_visitar:
        #Siguiente nodo a visitar y su camino
        nodoActual = por_visitar.pop(0) 
        
        # Splo se visita el nodo si no fue visitado antes
        if nodoActual not in visitados:
            visitados.append(nodoActual)

            #Si es la salida se retorna 
            if nodoActual == final:
                return arbolBusqueda

            #Expandimos el nodo
            movimientosPosibles = movimientos(nodoActual, matriz)

            # Recorremos los movimientos posibles
            for movimiento in movimientosPosibles:
                #Si ya no fue recorrido el nodo del movimiento
                if movimiento not in visitados:
                    por_visitar.append(movimiento)
                    arbolBusqueda.append(arbol(nodoActual,movimiento))
    
    #En caso que el laberinto no tenga salida valida
    return None



def movimientos(nodoActual, matriz):
    expandir_nodo = []
    fila = nodoActual.fila
    columna = nodoActual.columna

    #Arriba
    if fila > 0 and matriz[fila-1][columna] != 'x':
        expandir_nodo.append(nodo(fila - 1, columna))

    #Abajo``
    if fila < 9 and matriz[fila+1][columna] != 'x':
        
        expandir_nodo.append(nodo(fila + 1, columna))

    #Izquierda
    if columna > 0 and matriz[fila][columna-1] != 'x':
        expandir_nodo.append(nodo(fila, columna - 1))

    #Derecha
    if columna < 9 and matriz[fila][columna+1] != 'x':
        expandir_nodo.append(nodo(fila, columna + 1))

    return expandir_nodo


