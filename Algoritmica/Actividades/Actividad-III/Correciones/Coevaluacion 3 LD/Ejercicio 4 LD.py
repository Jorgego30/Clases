'''Usando el algoritmo de programación dinámica para dar las vueltas, encuentra el menor número de
monedas que se podrían usar para completar unas vueltas de 33 céntimos. Además de las monedas usuales,
supón que disponemos de una moneda de 8 céntimos. Realizar una simulación con distintas cantidades a
devolver y distintos valores de monedas.'''

def min_monedas(vueltas, monedas):
    n = len(monedas)
    dp = [float('inf')] * (vueltas + 1)
    dp[0] = 0

    for i in range(1, vueltas + 1):
        for j in range(n):
            if monedas[j] <= i:
                dp[i] = min(dp[i], dp[i - monedas[j]] + 1)

    return dp[vueltas]

# Realizar una simulación con distintas cantidades y monedas
cantidades = [33, 50, 72]
monedas = [1, 5, 10, 25, 8]

for cantidad in cantidades:
    num_monedas = min_monedas(cantidad, monedas)
    print(f"Para devolver {cantidad} céntimos se necesitan {num_monedas} monedas.")