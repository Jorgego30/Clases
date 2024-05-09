class MonticuloMaximo:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def flotar_arriba(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i] > self.listaMonticulo[i // 2]:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]
            i = i // 2

    def insertar(self, k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.flotar_arriba(self.tamanoActual)

    def hundir_abajo(self, i):
        while (i * 2) <= self.tamanoActual:
            hijo_maximo = self.hijo_maximo(i)
            if self.listaMonticulo[i] < self.listaMonticulo[hijo_maximo]:
                self.listaMonticulo[i], self.listaMonticulo[hijo_maximo] = self.listaMonticulo[hijo_maximo], self.listaMonticulo[i]
            i = hijo_maximo

    def hijo_maximo(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2] > self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminar_maximo(self):
        maximo = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.hundir_abajo(1)
        return maximo

    def construir_monticulo(self, una_lista):
        i = len(una_lista) // 2
        self.tamanoActual = len(una_lista)
        self.listaMonticulo = [0] + una_lista[:]
        while (i > 0):
            self.hundir_abajo(i)
            i = i - 1

# Ejemplo de uso
monticulo_maximo = MonticuloMaximo()
lista_desordenada = [9, 5, 7, 2, 3, 6, 1, 8, 4]
monticulo_maximo.construir_monticulo(lista_desordenada)

# Imprimir el montículo máximo
print("Montículo máximo construido:", monticulo_maximo.listaMonticulo[1:])

# Eliminar y imprimir el máximo repetidamente para ordenar la lista
lista_ordenada = []
while monticulo_maximo.tamanoActual > 0:
    lista_ordenada.append(monticulo_maximo.eliminar_maximo())
print("Lista ordenada:", lista_ordenada)
