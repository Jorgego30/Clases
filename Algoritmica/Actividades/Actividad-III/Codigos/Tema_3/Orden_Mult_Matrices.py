# Dentro de la matriz m, la fila 0 y la columna 0 no se usan
# La matriz m es triangular superior: la diagonal principal
# esta llena de ceros y corresponde a s=0, la siguiente a s=1, etc.
# hasta la ultima (con un solo elemento), que corresponde a s=n-1
def orden_optimo_producto(d):
    # recorremos las diagonales, desde s=1 hasta s=n-1
    n = len(d)-1
    m = [[0 for i in range(n+1)] for i in range(n+1)]
    for s in range(1, n):
        # optimizacion del parentizado para m[i][i+s]
        for i in range(1, n-s+1):
            for k in range(i, i+s):
                n_prod = m[i][k] + m[k+1][i+s] + d[i-1]*d[k]*d[i+s]
                if k == i or n_prod < minimo:
                    minimo = n_prod
            m[i][i+s] = minimo
    return m[1][n]


# 4 matrices: A (13 × 5), B (5 × 89), C (89 × 3) y D (3 × 34)
d = [13, 5, 89, 3, 34]
print(orden_optimo_producto(d))
