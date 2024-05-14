"""20. Utilizando la búsqueda en anchura, escribe un algoritmo que puede determinar la ruta más corta de cada
vértice a cada uno de los otros vértices. Esto se llama el problema de la ruta más corta de todas las parejas.
(Algoritmo de Floyd- Warshall)"""
INF = float('inf')

def floyd_warshall(grafo):
    n = len(grafo)
    distancias = [[INF] * n for _ in range(n)]

    # Inicializamos las distancias directas entre los vértices
    for i in range(n):
        distancias[i][i] = 0
        for j, peso in grafo[i]:
            distancias[i][j] = peso

    # Calculamos las distancias mínimas entre todos los pares de vértices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

    return distancias

def obtener_grafo():
    while True:
        try:
            # Solicitamos al usuario que ingrese el número de vértices en el grafo
            n = int(input("Ingrese el número de vértices en el grafo: "))

            # Inicializamos el grafo como una lista de adyacencia vacía
            grafo = [[] for _ in range(n)]

            # Solicitamos al usuario que ingrese las aristas del grafo
            while True:
                print("Ingrese una arista en el formato 'origen destino peso' (o escriba 'fin' para finalizar):")
                entrada = input().split()
                if entrada[0] == 'fin':
                    break
                origen, destino, peso = map(int, entrada)
                grafo[origen].append((destino, peso))

            return grafo

        except ValueError:
            print("¡Error! Ingrese un número válido para el número de vértices.")
        except IndexError:
            print("¡Error! El vértice ingresado está fuera de rango.")

def main():
    while True:
        grafo = obtener_grafo()

        # Aplicamos el algoritmo de Floyd-Warshall al grafo
        rutas_mas_cortas = floyd_warshall(grafo)

        # Mostramos las distancias mínimas entre todos los pares de vértices
        print("\nDistancias mínimas entre todos los pares de vértices:")
        for fila in rutas_mas_cortas:
            print(fila)

        continuar = input("\n¿Desea ingresar otro grafo? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
