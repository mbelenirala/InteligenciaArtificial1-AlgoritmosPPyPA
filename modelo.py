class nodo :

    def __init__(self,fila,columna):
        self.fila = fila
        self.columna = columna

    def __eq__(self, other):
        if isinstance(other, nodo):
            return self.fila == other.fila and self.columna == other.columna
        return False

 
class arbol : 
    def __init__(self, padre,hijo):
        self.padre = padre
        self.hijo = hijo

