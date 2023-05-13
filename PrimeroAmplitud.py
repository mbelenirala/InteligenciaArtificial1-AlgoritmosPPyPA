from Genlab import *
import graphviz
from graphviz import Graph
from PIL import Image
from modelo import *


def primeroAmplitud(matriz):
    inicio = nodo(9, 9)
    fin = nodo(0, 0)
    arbolBusqueda = []
    visitados = []
    porVisitar = []
    tiempo = 0
    porVisitar.append(arbol(inicio, inicio))
    Comienzo = False
    print("TIEMPO N°: ",tiempo,"SE AGREGA NODO: ",inicio)
    texto = []  # variable para guardar el texto de los prints
    texto.append(f"TIEMPO N°: {tiempo} SE AGREGA NODO: {inicio}")
    while porVisitar:
        tiempo += 1
        caminoAux = porVisitar.pop(0)
        porVisitar = eliminarNodosDuplicados(porVisitar)
        nodoActual = caminoAux.hijo
        if nodoActual not in visitados:
            print("-------------------------------------------")
            print("TIEMPO N°: ",tiempo,"PROCESANDO NODO: ",nodoActual)
            texto.append("-------------------------------------------")
            texto.append(f"TIEMPO N°: {tiempo} PROCESANDO NODO: {nodoActual}")
            vecinos = []
            if Comienzo:
                arbolBusqueda.append(caminoAux)
            if nodoActual == fin:
                print("TIEMPO N°: ",tiempo,"SE ENCONTRO EL NODO FIN ")
                texto.append(f"TIEMPO N°: {tiempo} SE ENCONTRO NODO FINAL")
                camino = [nodoActual]
                while nodoActual != inicio:
                    for caminoEnArbol in arbolBusqueda:
                        if caminoEnArbol.hijo == nodoActual:
                            nodoActual = caminoEnArbol.padre
                            camino.insert(0, nodoActual)
                return arbolBusqueda, camino, texto
            visitados.append(nodoActual)
            vecinos = movimientos(nodoActual, matriz)
            for nodo_hijo in vecinos:
                if nodo_hijo not in visitados:
                    print("TIEMPO N°: ",tiempo,"Se agregan a la lista: ",nodo_hijo)
                    texto.append(f"TIEMPO N°: {tiempo} Se agregan a la lista: {nodo_hijo}")
                    porVisitar.append(arbol(nodoActual, nodo_hijo))
        Comienzo=True
        

def primeroProfundidad(matriz):
    inicio = nodo(9, 9)
    fin = nodo(0, 0)
    arbolBusqueda = []
    visitados = []
    porVisitar = []
    tiempo = 0
    porVisitar.append(arbol(inicio, inicio))
    Comienzo = False
    print("TIEMPO N°: ",tiempo,"SE AGREGA NODO: ",inicio)
    texto = []  # variable para guardar el texto de los prints
    texto.append(f"TIEMPO N°: {tiempo} SE AGREGA NODO: {inicio}")
    while porVisitar:
        tiempo += 1
        caminoAux = porVisitar.pop(0)
        porVisitar = eliminarNodosDuplicados(porVisitar)
        nodoActual = caminoAux.hijo
        if nodoActual not in visitados:
            print("-------------------------------------------")
            print("TIEMPO N°: ",tiempo,"PROCESANDO NODO: ",nodoActual)
            texto.append("-------------------------------------------")
            texto.append(f"TIEMPO N°: {tiempo} PROCESANDO NODO: {nodoActual}")
            vecinos = []
            if Comienzo:
                arbolBusqueda.append(caminoAux)
            if nodoActual == fin:
                print("TIEMPO N°: ",tiempo,"SE ENCONTRO EL NODO FIN ")
                texto.append(f"TIEMPO N°: {tiempo} SE ENCONTRO NODO FINAL")
                camino = [nodoActual]
                while nodoActual != inicio:
                    for caminoEnArbol in arbolBusqueda:
                        if caminoEnArbol.hijo == nodoActual:
                            nodoActual = caminoEnArbol.padre
                            camino.insert(0, nodoActual)
                return arbolBusqueda, camino, texto
            visitados.append(nodoActual)
            vecinos = movimientos(nodoActual, matriz)
            vecinos.reverse()
            for nodo_hijo in vecinos:
                if nodo_hijo not in visitados:
                    print("TIEMPO N°: ",tiempo,"Se agregan a la lista: ",nodo_hijo)
                    texto.append(f"TIEMPO N°: {tiempo} Se agregan a la lista: {nodo_hijo}")
                    porVisitar.insert(0,arbol(nodoActual, nodo_hijo))
        Comienzo=True


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


def eliminarNodosDuplicados (porVisitar):
	por_visitar = []
	nodoProcesados = []
    
	for nodoActual in porVisitar:
		if nodoActual.hijo not in nodoProcesados:
			por_visitar.append(nodoActual)
			nodoProcesados.append(nodoActual.hijo)
    
	return por_visitar

