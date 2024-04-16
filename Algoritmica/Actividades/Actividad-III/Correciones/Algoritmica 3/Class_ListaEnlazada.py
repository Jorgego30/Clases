class NodoListaEnlazada:
    def __init__(self, valor=0, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def invertir_lista_enlazada(nodo):
    # Caso base: Si la lista está vacía o solo tiene un elemento, se devuelve el mismo nodo
    if nodo is None or nodo.siguiente is None:
        return nodo
    
    # Se invierte recursivamente el resto de la lista
    lista_invertida = invertir_lista_enlazada(nodo.siguiente)
    
    # Se cambia el enlace del nodo actual para apuntar al nodo siguiente
    nodo.siguiente.siguiente = nodo
    nodo.siguiente = None
    
    # Se devuelve el nuevo inicio de la lista invertida
    return lista_invertida
