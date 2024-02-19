from ClassPolinomio import *

firstCoeficientes = [2,3]
firstPolinomio = Polinomio(firstCoeficientes)
print(f"El primer polinomio es: \n{firstPolinomio}")


coeficientes = str(input("Introduce los coeficientes del polinomio por orden de grado de mayor a menor (en caso de saltar algun grado introduzca 0 en su posicion): "))
nuevosCoeficientes = []
for i in (coeficientes.split()):
    nuevosCoeficientes.append(int(i))

secondPolinomio = Polinomio(nuevosCoeficientes)
print(f"El segundo polinomio es: \n{secondPolinomio}")

sumaPolinomio = firstPolinomio + secondPolinomio
restaPolinomio = firstPolinomio - secondPolinomio
multiplicacionPolinomio = firstPolinomio * secondPolinomio
divisionPolinomio = firstPolinomio / secondPolinomio

print(f"La suma de los polinomios \n{firstPolinomio} \ny \n{secondPolinomio} es: \n{sumaPolinomio}")
print(f"La resta de los polinomios \n{firstPolinomio} \ny \n{secondPolinomio} es: \n{restaPolinomio}")
print(f"La multiplicacion de los polinomios \n{firstPolinomio} \ny \n{secondPolinomio} es: \n{multiplicacionPolinomio}")
print(f"La division de los polinomios \n{firstPolinomio} \ny \n{secondPolinomio} es: \n{divisionPolinomio}")
