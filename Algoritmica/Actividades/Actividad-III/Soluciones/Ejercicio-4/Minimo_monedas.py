def devolver_cambio(monedas, M):
    n = len(monedas)  # número de monedas
    c = [[None for j in range(M + 1)] for i in range(n)]

    for j in range(M + 1):
        c[0][j] = j // monedas[0] if j % monedas[0] == 0 else None

    for i in range(1, n):
        for j in range(M + 1):
            if j < monedas[i]:
                c[i][j] = c[i - 1][j]
            else:
                if c[i - 1][j] is not None and c[i][j - monedas[i]] is not None:
                    c[i][j] = min(c[i - 1][j], 1 + c[i][j - monedas[i]])
                elif c[i][j - monedas[i]] is not None:
                    c[i][j] = 1 + c[i][j - monedas[i]]
                else:
                    c[i][j] = c[i - 1][j]

    return c[n - 1][M]


def devolver_cambio_con_moneda_extra(monedas, M):
    monedas.append(8)  # Agregamos la moneda extra de 8 céntimos
    return devolver_cambio(monedas, M)


def simulacion():
    monedas = [1, 2, 5, 10, 20, 50]  # Monedas usuales
    cantidades = [11, 33, 55]  # Distintas cantidades a devolver

    for cantidad in cantidades:
        min_monedas = devolver_cambio_con_moneda_extra(monedas, cantidad)
        print(f"Para devolver {cantidad} céntimos se necesitan {min_monedas} monedas.")


simulacion()
