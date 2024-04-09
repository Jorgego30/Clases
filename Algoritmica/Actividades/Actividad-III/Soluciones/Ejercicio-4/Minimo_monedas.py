# monedas: vector con los valores de las monedas (distintas)
# M: valor a devolver
# devuelve el numero minimo de monedas necesario (o None)
def devolver_cambio(monedas, M):
    n = len(monedas)  # numero de monedas
    c = [[None for j in range(M+1)] for i in range(n)]
    c[0][0] = 0
    for j in range(1, M+1):
        if j >= monedas[0] and c[0][j-monedas[0]] != None:
            c[0][j] = 1+c[0][j-monedas[0]]
            # print(c)
    for i in range(1, n):
        c[i][0] = 0
        for j in range(1, M+1):
            if j < monedas[i] or c[i][j-monedas[i]] == None:
                c[i][j] = c[i-1][j]
            elif c[i-1][j] != None:
                c[i][j] = min(c[i-1][j], 1+c[i][j-monedas[i]])
            else:
                c[i][j] = 1+c[i][j-monedas[i]]

    return c[n-1][M]


print(devolver_cambio([4, 1, 6], 8))
