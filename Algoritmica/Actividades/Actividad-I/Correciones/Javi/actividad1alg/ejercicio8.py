'''actividad8:Implementar con todos sus componentes la clase Complejo, de manera que se puedan ejecutar todas las
operaciones sobre complejos'''

from complejos import Complejo

# Ejemplo de uso de la clase Complejo sin tenerla escrita en este archivo

# Crear números complejos
complejo1 = Complejo(3, 2)  # Representa 3 + 2i
complejo2 = Complejo(1, -4)  # Representa 1 - 4i

# Suma de números complejos
resultado_suma = complejo1 + complejo2
print(f"Suma: {complejo1} + {complejo2} = {resultado_suma}")

# Resta de números complejos
resultado_resta = complejo1 - complejo2
print(f"Resta: {complejo1} - {complejo2} = {resultado_resta}")

# Multiplicación de números complejos
resultado_multiplicacion = complejo1 * complejo2
print(f"Multiplicación: {complejo1} * {complejo2} = {resultado_multiplicacion}")


