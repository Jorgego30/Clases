def knapsack(capacidad_mochila, pesos, valores):
    n = len(pesos)
    tabla = [[0] * (capacidad_mochila + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidad_mochila + 1):
            if pesos[i - 1] <= w:
                tabla[i][w] = max(valores[i - 1] + tabla[i - 1][w - pesos[i - 1]], tabla[i - 1][w])
            else:
                tabla[i][w] = tabla[i - 1][w]

    seleccionados = []
    peso_actual = capacidad_mochila
    for i in range(n, 0, -1):
        if tabla[i][peso_actual] != tabla[i - 1][peso_actual]:
            seleccionados.append(i - 1)
            peso_actual -= pesos[i - 1]

    return tabla[n][capacidad_mochila], seleccionados

# Datos de entrada
capacidad_mochila = 20
pesos = [2, 3, 4, 5, 9]
valores = [3, 4, 8, 8, 10]

# Calcular el valor máximo y los elementos seleccionados
max_valor, elementos_seleccionados = knapsack(capacidad_mochila, pesos, valores)

# Imprimir resultados
print("Valor máximo que se puede obtener:", max_valor)
print("Elementos seleccionados (índices):", elementos_seleccionados)
