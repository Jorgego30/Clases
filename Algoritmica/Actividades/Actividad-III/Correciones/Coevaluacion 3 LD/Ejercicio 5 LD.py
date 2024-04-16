'''Supón que eres un científico de la computación/ladrón de arte que se ha colado en una galería de arte
importante. Dispones sólo de una mochila para sacar las obras de arte robadas, que sólo puede contener W
“kilos de arte”; no obstante, para cada pieza de arte conoces su valor y su peso. Escribe una función de
programación dinámica para maximizar tus ganancias, con distintas capacidades de la mochila y distintos
valores/pesos de los ítems. He aquí un ejemplo del problema que puedes usar para empezar: Supongamos
que la mochila aguanta un peso total de 20.'''

def maximizar_ganancias(capacidad_mochila, items):
    n = len(items)
    dp = [[0 for _ in range(capacidad_mochila + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        peso_i, valor_i = items[i - 1]
        for w in range(1, capacidad_mochila + 1):
            if peso_i > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - peso_i] + valor_i)

    return dp[n][capacidad_mochila]

# Realizar una simulación con una capacidad de mochila de 20 y los ítems dados
capacidad_mochila = 20
items = [(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)]

ganancia_maxima = maximizar_ganancias(capacidad_mochila, items)
print(f"La ganancia máxima que puedes obtener con una capacidad de mochila de {capacidad_mochila} es: {ganancia_maxima}")