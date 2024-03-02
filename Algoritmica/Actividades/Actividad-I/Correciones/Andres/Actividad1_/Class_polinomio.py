class Polinomio:
    def __init__(self, coeficientes):
        # Inicializa el polinomio con una lista de coeficientes
        self.coeficientes = coeficientes

    def __str__(self):
        # Devuelve una representación de cadena del polinomio
        return " + ".join(f"{coef}x^{exp}" for exp, coef in enumerate(self.coeficientes[::-1]))

    def __len__(self):
        # Devuelve el grado del polinomio
        return len(self.coeficientes) - 1

    def __add__(self, other):
        # Suma de polinomios
        max_len = max(len(self.coeficientes), len(other.coeficientes))
        result_coefs = [0] * max_len

        for i in range(len(self.coeficientes)):
            result_coefs[i] += self.coeficientes[i]

        for i in range(len(other.coeficientes)):
            result_coefs[i] += other.coeficientes[i]

        return Polinomio(result_coefs)

    def __sub__(self, other):
        # Resta de polinomios
        max_len = max(len(self.coeficientes), len(other.coeficientes))
        result_coefs = [0] * max_len

        for i in range(len(self.coeficientes)):
            result_coefs[i] += self.coeficientes[i]

        for i in range(len(other.coeficientes)):
            result_coefs[i] -= other.coeficientes[i]

        return Polinomio(result_coefs)

    def __mul__(self, other):
        # Multiplicación de polinomios
        result_coefs = [0] * (len(self) + len(other) + 1)

        for i in range(len(self.coeficientes)):
            for j in range(len(other.coeficientes)):
                result_coefs[i + j] += self.coeficientes[i] * other.coeficientes[j]

        return Polinomio(result_coefs)

    def evaluar(self, x):
        # Evalúa el polinomio en un punto dado x
        result = 0
        for exp, coef in enumerate(self.coeficientes):
            result += coef * (x ** exp)
        return result


