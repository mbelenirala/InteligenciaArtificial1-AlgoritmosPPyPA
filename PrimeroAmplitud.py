from Genlab import *

matriz = generateMaze()
height = 10
width = 10
printMaze(matriz,height,width)
inicio = (9, 9)
final = (0, 0)


def PrimeroAmplitud(matriz, inicio, final, padre=None):
    visitados = []
    por_visitar = [(inicio, [inicio])]
    arbol = []

    while por_visitar:
        #Siguiente nodo a visitar y su camino
        nodo, camino = por_visitar.pop(0) 
        
        # Splo se visita el nodo si no fue visitado antes
        if nodo not in visitados and matriz[nodo[0]][nodo[1]] != 'x':
            visitados.append(nodo)

            #Si es la salida se retorna el arbol
            if nodo == final:

                if padre is not None:
                    arbol.append((padre, nodo))
                return arbol

            #Expandimos el nodo
            expandir_nodo = movimientos(nodo, matriz)

            # Recorremos los movimientos posibles
            for movimiento in expandir_nodo:
                #Si ya no fue recorrido el nodo del movimiento
                if movimiento not in visitados:
                    if padre is not None:
                        arbol.append((padre, movimiento))
                    por_visitar.append((movimiento, camino + [movimiento]))
                    padre = nodo

    #En caso que el laberinto no tenga salida valida
    return None



def movimientos(nodo, matriz):
    expandir_nodo = []
    fila, columna = nodo

    #Arriba
    if fila > 0 and matriz[fila-1][columna] != 'x':
        expandir_nodo.append((fila - 1, columna))

    #Abajo
    if fila < 9 and matriz[fila+1][columna] != 'x':
        
        expandir_nodo.append((fila + 1, columna))

    #Izquierda
    if columna > 0 and matriz[fila][columna-1] != 'x':
        expandir_nodo.append((fila, columna - 1))

    #Derecha
    if columna < 9 and matriz[fila][columna+1] != 'x':
        expandir_nodo.append((fila, columna + 1))

    return expandir_nodo


arbol = PrimeroAmplitud(matriz, inicio, final)

if arbol:
    for padre, hijo in arbol:
        print(f"{padre} -> {hijo}")
else:
    print("No se encontró un camino válido.")
