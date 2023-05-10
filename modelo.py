class nodo :

    def __init__(self,fila,columna):
        self.fila = fila
        self.columna = columna

    def __eq__(actual, nodo2):
        if isinstance(nodo2, nodo):
            return actual.fila == nodo2.fila and actual.columna == nodo2.columna
        return False

 
class arbol: 
    def __init__(self, padre, hijo, tiempo):
        self.padre = padre
        self.hijo = hijo
        self.tiempo = tiempo
