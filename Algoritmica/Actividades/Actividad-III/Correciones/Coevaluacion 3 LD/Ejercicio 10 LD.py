'''Utilizando las fórmulas de desempeño de la tabla hash que se dan en el Tema 4, calcula el número promedio
de comparaciones necesarias cuando la tabla está
10% completa
25% completa
50% completa
75% completa
90% completa
99% completa
¿En qué punto crees que la tabla hash es demasiado pequeña? Explícalo'''

def calcular_num_comparaciones(alpha):
    return 0.5 * (1 + 1 / (1 - alpha))

niveles_ocupacion = [0.1, 0.25, 0.5, 0.75, 0.9, 0.99]

for nivel in niveles_ocupacion:
    num_comparaciones = calcular_num_comparaciones(nivel)
    if nivel >= 0.9:
        mensaje = "Tabla hash demasiado pequeña"  # Identificar cuando la tabla es demasiado pequeña
    else:
        mensaje = ""
    print(f"Nivel de ocupación: {nivel * 100}% - Número promedio de comparaciones: {num_comparaciones:.2f} - {mensaje}")