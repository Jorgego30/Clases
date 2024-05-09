from Class_MonticuloMax import *

def imprimir_monticulo_maximo(monticulo):
    print("Montículo máximo construido:", monticulo.listaMonticulo[1:])

# Crear un montículo máximo y probar los métodos
monticulo_maximo = MonticuloMaximo()
lista_desordenada = [9, 5, 7, 2, 3, 6, 1, 8, 4]

# Construir el montículo máximo
monticulo_maximo.construir_monticulo(lista_desordenada)

# Imprimir el montículo máximo
imprimir_monticulo_maximo(monticulo_maximo)

# Eliminar y imprimir el máximo repetidamente para ordenar la lista
lista_ordenada = []
while monticulo_maximo.tamanoActual > 0:
    lista_ordenada.append(monticulo_maximo.eliminar_maximo())
print("Lista ordenada:", lista_ordenada)