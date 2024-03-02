class NumeroComplejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        # Devuelve una representación de cadena del número complejo
        return f"{self.real} + {self.imaginario}i"

    def __add__(self, otro):
        # Suma de números complejos
        suma_real = self.real + otro.real
        suma_imaginario = self.imaginario + otro.imaginario
        return NumeroComplejo(suma_real, suma_imaginario)

    def __sub__(self, otro):
        # Resta de números complejos
        resta_real = self.real - otro.real
        resta_imaginario = self.imaginario - otro.imaginario
        return NumeroComplejo(resta_real, resta_imaginario)

    def __mul__(self, otro):
        # Multiplicación de números complejos
        producto_real = self.real * otro.real - self.imaginario * otro.imaginario
        producto_imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(producto_real, producto_imaginario)


