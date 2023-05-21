from Genlab import *
import graphviz
from graphviz import Graph
from PIL import Image
from modelo import *


def primeroAmplitud(matriz,sentido):
    inicio = nodo(9, 9)
    fin = nodo(0, 0)
    arbolBusqueda = []
    visitados = []
    porVisitar = []
    tiempo = 0
    porVisitar.append(arbol(inicio, inicio))
    Comienzo = False
    #print("TIEMPO N°: ",tiempo,"SE AGREGA NODO: ",inicio)
    texto = []  # variable para guardar el texto de los prints
    texto.append(f"TIEMPO N°: {tiempo} SE AGREGA NODO INICIO: {inicio}")
    print("el sentido es: ", sentido)
    while porVisitar:
        tiempo += 1
        caminoAux = porVisitar.pop(0)
        porVisitar = eliminarNodosDuplicados(porVisitar)
        nodoActual = caminoAux.hijo
        if nodoActual not in visitados:
            #print("-------------------------------------------")
            #print("TIEMPO N°: ",tiempo,"PROCESANDO NODO: ",nodoActual)
            texto.append("-------------------------------------------")
            texto.append(f"TIEMPO N°: {tiempo}")
            texto.append(f"PROCESANDO NODO: {nodoActual}")
            vecinos = []
            if Comienzo:
                arbolBusqueda.append(caminoAux)
            if nodoActual == fin:
                #print("TIEMPO N°: ",tiempo,"SE ENCONTRO EL NODO FIN ")
                texto.append(f"TIEMPO N°: {tiempo} SE ENCONTRO NODO FINAL")
                camino = [nodoActual]
                while nodoActual != inicio:
                    for caminoEnArbol in arbolBusqueda:
                        if caminoEnArbol.hijo == nodoActual:
                            nodoActual = caminoEnArbol.padre
                            camino.insert(0, nodoActual)
                return arbolBusqueda, camino, texto
            visitados.append(nodoActual)
            vecinos = movimientos(nodoActual, matriz,sentido)
            txtAgregados = ""
            for nodo_hijo in vecinos:
                if nodo_hijo not in visitados:
                    #print("TIEMPO N°: ",tiempo,"Se agregan a la lista: ",nodo_hijo)
                    txtAgregados += " " + str(nodo_hijo)
                    porVisitar.append(arbol(nodoActual, nodo_hijo))
        txtCola = ""
        for nodoCola in porVisitar:
            txtCola += " " + str(nodoCola.hijo)
        texto.append(f"Cola: {txtCola}")
        texto.append(f"(Se agregan: {txtAgregados})")
        Comienzo=True
        

def primeroProfundidad(matriz,sentido):
    inicio = nodo(9, 9)
    fin = nodo(0, 0)
    arbolBusqueda = []
    visitados = []
    porVisitar = []
    tiempo = 0
    porVisitar.append(arbol(inicio, inicio))
    Comienzo = False
    #print("TIEMPO N°: ",tiempo,"SE AGREGA NODO: ",inicio)
    texto = []  # variable para guardar el texto de los prints
    texto.append(f"TIEMPO N°: {tiempo} SE AGREGA NODO INICIO: {inicio}")
    print("el sentido es: ", sentido)
    while porVisitar:
        tiempo += 1
        caminoAux = porVisitar.pop(0)
        porVisitar = eliminarNodosDuplicados(porVisitar)
        nodoActual = caminoAux.hijo
        if nodoActual not in visitados:
            #print("-------------------------------------------")
            #print("TIEMPO N°: ",tiempo,"PROCESANDO NODO: ",nodoActual)
            texto.append("-------------------------------------------")
            texto.append(f"TIEMPO N°: {tiempo}")
            texto.append(f"PROCESANDO NODO: {nodoActual}")
            vecinos = []
            if Comienzo:
                arbolBusqueda.append(caminoAux)
            if nodoActual == fin:
                #print("TIEMPO N°: ",tiempo,"SE ENCONTRO EL NODO FIN ")
                texto.append(f"TIEMPO N°: {tiempo} SE ENCONTRO NODO FINAL")
                camino = [nodoActual]
                while nodoActual != inicio:
                    for caminoEnArbol in arbolBusqueda:
                        if caminoEnArbol.hijo == nodoActual:
                            nodoActual = caminoEnArbol.padre
                            camino.insert(0, nodoActual)
                return arbolBusqueda, camino, texto
            visitados.append(nodoActual)
            vecinos = movimientos(nodoActual, matriz,sentido)
            vecinos.reverse()
            txtAgregados = ""
            for nodo_hijo in vecinos:
                if nodo_hijo not in visitados:
                    #print("TIEMPO N°: ",tiempo,"Se agregan a la lista: ",nodo_hijo)
                    txtAgregados += " " + str(nodo_hijo)
                    porVisitar.insert(0,arbol(nodoActual, nodo_hijo))
        txtCola = ""
        for nodoCola in porVisitar:
            txtCola += " " + str(nodoCola.hijo)
        texto.append(f"Cola: {txtCola}")
        texto.append(f"(Se agregan: {txtAgregados})")
        Comienzo=True


def movimientos(nodoActual, matriz,sentido):
    expandir_nodo = []
    fila = nodoActual.fila
    columna = nodoActual.columna
    if (sentido == 1):
        #Sentido horario
         #Arriba
        if fila > 0 and matriz[fila-1][columna] != 'x':
            expandir_nodo.append(nodo(fila - 1, columna))

        #Derecha
        if columna < 9 and matriz[fila][columna+1] != 'x':
            expandir_nodo.append(nodo(fila, columna + 1))

        #Abajo
        if fila < 9 and matriz[fila+1][columna] != 'x':
            
            expandir_nodo.append(nodo(fila + 1, columna))

        #Izquierda
        if columna > 0 and matriz[fila][columna-1] != 'x':
            expandir_nodo.append(nodo(fila, columna - 1))
    elif (sentido == 2):
        #Sentido antihorario
        #Arriba
        if fila > 0 and matriz[fila-1][columna] != 'x':
            expandir_nodo.append(nodo(fila - 1, columna))

        #Izquierda
        if columna > 0 and matriz[fila][columna-1] != 'x':
            expandir_nodo.append(nodo(fila, columna - 1))

        #Abajo
        if fila < 9 and matriz[fila+1][columna] != 'x':
            
            expandir_nodo.append(nodo(fila + 1, columna))
        
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

