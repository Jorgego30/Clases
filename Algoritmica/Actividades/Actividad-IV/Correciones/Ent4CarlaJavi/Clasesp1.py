class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def numNodos(self):
        return self._numNodosRecursivo(self.raiz)

    def _numNodosRecursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._numNodosRecursivo(nodo.izquierda) + self._numNodosRecursivo(nodo.derecha)

    def numHojas(self):
        return self._numHojasRecursivo(self.raiz)

    def _numHojasRecursivo(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        return self._numHojasRecursivo(nodo.izquierda) + self._numHojasRecursivo(nodo.derecha)

    def profundidad(self):
        return self._profundidadRecursivo(self.raiz)

    def _profundidadRecursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._profundidadRecursivo(nodo.izquierda), self._profundidadRecursivo(nodo.derecha))

    def espejo(self):
        return self._espejoRecursivo(self.raiz)

    def _espejoRecursivo(self, nodo):
        if nodo is None:
            return None
        espejo = Nodo(nodo.valor)
        espejo.izquierda = self._espejoRecursivo(nodo.derecha)
        espejo.derecha = self._espejoRecursivo(nodo.izquierda)
        return espejo
