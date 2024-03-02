'''actividad8:Implementar con todos sus componentes la clase Complejo, de manera que se puedan ejecutar todas las
operaciones sobre complejos'''

class Complejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        if self.imaginario >= 0:
            return f'{self.real} + {self.imaginario}i'
        else:
            return f'{self.real} - {abs(self.imaginario)}i'

    def __add__(self, otro_complejo):
        suma_real = self.real + otro_complejo.real
        suma_imaginario = self.imaginario + otro_complejo.imaginario
        return Complejo(suma_real, suma_imaginario)

    def __sub__(self, otro_complejo):
        resta_real = self.real - otro_complejo.real
        resta_imaginario = self.imaginario - otro_complejo.imaginario
        return Complejo(resta_real, resta_imaginario)

    def __mul__(self, otro_complejo):
        producto_real = self.real * otro_complejo.real - self.imaginario * otro_complejo.imaginario
        producto_imaginario = self.real * otro_complejo.imaginario + self.imaginario * otro_complejo.real
        return Complejo(producto_real, producto_imaginario)

# Ejemplo de uso de la clase Complejo
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

