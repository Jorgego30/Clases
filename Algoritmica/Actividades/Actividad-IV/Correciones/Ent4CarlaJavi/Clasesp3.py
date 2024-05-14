class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, valor)
        return nodo

    def recorrido_preorden(self):
        self._recorrido_preorden_recursivo(self.raiz)
        print()

    def _recorrido_preorden_recursivo(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self._recorrido_preorden_recursivo(nodo.izquierda)
            self._recorrido_preorden_recursivo(nodo.derecha)

    def recorrido_inorden(self):
        self._recorrido_inorden_recursivo(self.raiz)
        print()

    def _recorrido_inorden_recursivo(self, nodo):
        if nodo:
            self._recorrido_inorden_recursivo(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._recorrido_inorden_recursivo(nodo.derecha)

    def recorrido_postorden(self):
        self._recorrido_postorden_recursivo(self.raiz)
        print()

    def _recorrido_postorden_recursivo(self, nodo):
        if nodo:
            self._recorrido_postorden_recursivo(nodo.izquierda)
            self._recorrido_postorden_recursivo(nodo.derecha)
            print(nodo.valor, end=" ")

    def recorrido_anchura(self):
        if self.raiz is None:
            return

        cola = []
        cola.append(self.raiz)

        while len(cola) > 0:
            nodo_actual = cola.pop(0)
            print(nodo_actual.valor, end=" ")

            if nodo_actual.izquierda:
                cola.append(nodo_actual.izquierda)
            if nodo_actual.derecha:
                cola.append(nodo_actual.derecha)

    def cantidad_nodos(self):
        return self._cantidad_nodos_recursivo(self.raiz)

    def _cantidad_nodos_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._cantidad_nodos_recursivo(nodo.izquierda) + self._cantidad_nodos_recursivo(nodo.derecha)

    def cantidad_hojas(self):
        return self._cantidad_hojas_recursivo(self.raiz)

    def _cantidad_hojas_recursivo(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        return self._cantidad_hojas_recursivo(nodo.izquierda) + self._cantidad_hojas_recursivo(nodo.derecha)

    def profundidad(self):
        return self._profundidad_recursivo(self.raiz)

    def _profundidad_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._profundidad_recursivo(nodo.izquierda), self._profundidad_recursivo(nodo.derecha))
