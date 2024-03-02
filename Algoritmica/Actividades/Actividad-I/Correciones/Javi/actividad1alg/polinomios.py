'''actividad7:Implementar con todos sus componentes la clase Polinomio, de manera que se puedan ejecutar todas las
operaciones sobre polinomios'''
class Polinomio:
    def __init__(self, coeficientes):
        if not isinstance(coeficientes, list):
            raise ValueError("Se requiere una lista de coeficientes para inicializar el polinomio.")

        self.coeficientes = coeficientes

    def __str__(self):
        resultado = ""
        for grado, coeficiente in enumerate(self.coeficientes[::-1]):
            if coeficiente != 0:
                resultado += f"{coeficiente}x^{grado} + "
        
        return resultado[:-3]

    def __add__(self, otro_polinomio):
        suma_coeficientes = [a + b for a, b in zip(self.coeficientes, otro_polinomio.coeficientes)]
        return Polinomio(suma_coeficientes)

    def __sub__(self, otro_polinomio):
        resta_coeficientes = [a - b for a, b in zip(self.coeficientes, otro_polinomio.coeficientes)]
        return Polinomio(resta_coeficientes)

    def __mul__(self, otro_polinomio):
        grado_resultante = len(self.coeficientes) + len(otro_polinomio.coeficientes) - 2
        producto_coeficientes = [0] * (grado_resultante + 1)

        for i, a in enumerate(self.coeficientes):
            for j, b in enumerate(otro_polinomio.coeficientes):
                producto_coeficientes[i + j] += a * b

        return Polinomio(producto_coeficientes)

    def evaluar(self, x):
        resultado = 0
        for i, coeficiente in enumerate(self.coeficientes):
            resultado += coeficiente * (x ** i)
        return resultado

