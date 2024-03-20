# Devuelve la solucion (o None, si no existe)
def devolver_cambio(monedas, M):
    n = len(monedas)  # numero de monedas distintas
    c = [[None for j in range(M+1)] for i in range(n)]
    c[0][0] = 0
    for j in range(1, M+1):
        if j >= monedas[0] and c[0][j-monedas[0]] != None:
            c[0][j] = 1+c[0][j-monedas[0]]
    for i in range(1, n):
        c[i][0] = 0
        for j in range(1, M+1):
            if j < monedas[i] or c[i][j-monedas[i]] == None:
                c[i][j] = c[i-1][j]
            elif c[i-1][j] != None:
                c[i][j] = min(c[i-1][j], 1+c[i][j-monedas[i]])
            else:
                c[i][j] = 1+c[i][j-monedas[i]]
    if c[n-1][M] == None:
        return None
    x = [0 for i in range(n)]  # RECUPERACION DE LA SOLUCION
    i = n-1
    j = M
    while i != 0 or j != 0:
        if i == 0 or c[i][j] != c[i-1][j]:
            x[i] += 1
            j -= monedas[i]
        else:
            i = i-1
    return x


print(devolver_cambio([4, 1, 6], 8))
