from Class_polinomio import *
# Ejemplo de uso:
polinomio1 = Polinomio([1, -3, 0, 2])  # Representa x^3 - 3x^2 + 2
polinomio2 = Polinomio([0, 1, -1])      # Representa x^2 - x

# Suma de polinomios
suma_resultado = polinomio1 + polinomio2
print("Suma:", suma_resultado)

# Resta de polinomios
resta_resultado = polinomio1 - polinomio2
print("Resta:", resta_resultado)

# Multiplicación de polinomios
multiplicacion_resultado = polinomio1 * polinomio2
print("Multiplicación:", multiplicacion_resultado)

# Evaluación del polinomio en x = 2
valor_evaluado = polinomio1.evaluar(2)
print("Evaluación en x=2:", valor_evaluado)