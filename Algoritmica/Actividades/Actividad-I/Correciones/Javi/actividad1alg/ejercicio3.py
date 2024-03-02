'''actividad 6:denominador sean ambos enteros. Si alguno no es un entero, el constructor debe generar una excepción.
Implemente los métodos simples getNum y getDen eso devolverá el numerador y el denominador de una
fracción. Implementar los operadores relacionales restantes ( >, >=, <, <=, y !=)'''

from fracciones import Fraccion  # Asegúrate de que el nombre del archivo coincide

# Crear dos instancias de la clase Fraccion
fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(3, 4)

# Realizar algunas operaciones con las fracciones
suma = fraccion1 + fraccion2
resta = fraccion1 - fraccion2
multiplicacion = fraccion1 * fraccion2
division = fraccion1 / fraccion2

# Imprimir los resultados
print("Fracción 1:", fraccion1)
print("Fracción 2:", fraccion2)
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# Comparar las fracciones
print("¿Fracción 1 igual a Fracción 2?", fraccion1 == fraccion2)
print("¿Fracción 1 diferente de Fracción 2?", fraccion1 != fraccion2)
print("¿Fracción 1 menor que Fracción 2?", fraccion1 < fraccion2)
print("¿Fracción 1 menor o igual que Fracción 2?", fraccion1 <= fraccion2)
print("¿Fracción 1 mayor que Fracción 2?", fraccion1 > fraccion2)
print("¿Fracción 1 mayor o igual que Fracción 2?", fraccion1 >= fraccion2)
