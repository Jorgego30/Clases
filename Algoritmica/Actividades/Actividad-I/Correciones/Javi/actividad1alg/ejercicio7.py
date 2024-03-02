'''actividad7:Implementar con todos sus componentes la clase Polinomio, de manera que se puedan ejecutar todas las
operaciones sobre polinomios'''
from polinomios import Polinomio

# Ejemplo de uso de la clase Polinomio sin tenerla escrita en este archivo

# Crear polinomios
polinomio1 = Polinomio([1, -2, 0, 3])  # Representa x^3 - 2x^2 + 3
polinomio2 = Polinomio([0, 1, 4, -1])  # Representa x^3 + 4x^2 - x

# Suma de polinomios
resultado_suma = polinomio1 + polinomio2
print(f"Suma: {polinomio1} + {polinomio2} = {resultado_suma}")

# Resta de polinomios
resultado_resta = polinomio1 - polinomio2
print(f"Resta: {polinomio1} - {polinomio2} = {resultado_resta}")

# Multiplicación de polinomios
resultado_multiplicacion = polinomio1 * polinomio2
print(f"Multiplicación: {polinomio1} * {polinomio2} = {resultado_multiplicacion}")

# Evaluación del polinomio en x = 2
valor_x = 2
resultado_evaluacion = polinomio1.evaluar(valor_x)
print(f"Evaluación de {polinomio1} en x = {valor_x}: {resultado_evaluacion}")

