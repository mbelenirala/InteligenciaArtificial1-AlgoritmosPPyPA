class nodo :

    def __init__(self,fila,columna):
        self.fila = fila
        self.columna = columna

    def __eq__(self, nodo2):
        if isinstance(nodo2, nodo):
            return self.fila == nodo2.fila and self.columna == nodo2.columna
        return False

    def __str__(self):
        return f"({self.fila}, {self.columna})"
 
class arbol: 
    def __init__(self, padre, hijo):
        self.padre = padre
        self.hijo = hijo

