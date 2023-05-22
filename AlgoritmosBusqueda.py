from Genlab import *
import graphviz
from graphviz import Graph
from PIL import Image
from modelo import *

#Algoritmo de Primero en Amplitud
def primeroAmplitud(matriz,sentido):
    inicio = nodo(9, 9)
    fin = nodo(0, 0)
    arbolBusqueda = []
    visitados = []
    porVisitar = []
    tiempo = 0
    porVisitar.append(arbol(inicio, inicio))
    Comienzo = False
    texto = []  # variable para guardar el texto de los prints
    texto.append(f"TIEMPO N°: {tiempo} SE AGREGA NODO INICIO: {inicio}")
    print("el sentido es: ", sentido)
    while porVisitar:
        tiempo += 1
        caminoAux = porVisitar.pop(0)
        porVisitar = eliminarNodosDuplicados(porVisitar)
        nodoActual = caminoAux.hijo
        if nodoActual not in visitados:
            texto.append("-------------------------------------------")
            texto.append(f"TIEMPO N°: {tiempo}")
            texto.append(f"PROCESANDO NODO: {nodoActual}")
            vecinos = []
            if Comienzo:
                arbolBusqueda.append(caminoAux)
            if nodoActual == fin:
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
            txtAgregados = "" # variable para guardar los nuevos nodos agregados al procesamiento
            for nodo_hijo in vecinos:
                if nodo_hijo not in visitados:
                    txtAgregados += " " + str(nodo_hijo)
                    porVisitar.append(arbol(nodoActual, nodo_hijo))
        txtCola = "" # variable para guardar la cola del procesamiento
        for nodoCola in porVisitar:
            txtCola += " " + str(nodoCola.hijo)
        texto.append(f"Cola: {txtCola}")
        texto.append(f"(Se agregan: {txtAgregados})")
        Comienzo=True
        
#Algoritmo de Primero en Profundidad
def primeroProfundidad(matriz,sentido):
    inicio = nodo(9, 9)
    fin = nodo(0, 0)
    arbolBusqueda = []
    visitados = []
    porVisitar = []
    tiempo = 0
    porVisitar.append(arbol(inicio, inicio))
    Comienzo = False
    texto = []  # variable para guardar el texto de los prints
    texto.append(f"TIEMPO N°: {tiempo} SE AGREGA NODO INICIO: {inicio}")
    print("el sentido es: ", sentido)
    while porVisitar:
        tiempo += 1
        caminoAux = porVisitar.pop(0)
        porVisitar = eliminarNodosDuplicados(porVisitar)
        nodoActual = caminoAux.hijo
        if nodoActual not in visitados:
            texto.append("-------------------------------------------")
            texto.append(f"TIEMPO N°: {tiempo}")
            texto.append(f"PROCESANDO NODO: {nodoActual}")
            vecinos = []
            if Comienzo:
                arbolBusqueda.append(caminoAux)
            if nodoActual == fin:
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
            txtAgregados = "" # variable para guardar los nuevos nodos agregados al procesamiento
            for nodo_hijo in vecinos:
                if nodo_hijo not in visitados:
                    txtAgregados += " " + str(nodo_hijo)
                    porVisitar.insert(0,arbol(nodoActual, nodo_hijo))
        txtCola = "" # variable para guardar la cola del procesamiento
        for nodoCola in porVisitar:
            txtCola += " " + str(nodoCola.hijo)
        texto.append(f"Cola: {txtCola}")
        texto.append(f"(Se agregan: {txtAgregados})")
        Comienzo=True

#Defincion del criterio sentido de busqueda para los algoritmos
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

#Elimina nodos duplicados de la lista a procesar
def eliminarNodosDuplicados (porVisitar):
	por_visitar = []
	nodoProcesados = []
    
	for nodoActual in porVisitar:
		if nodoActual.hijo not in nodoProcesados:
			por_visitar.append(nodoActual)
			nodoProcesados.append(nodoActual.hijo)
    
	return por_visitar

