'''actividad4:En la definición de fracciones asumimos que las fracciones negativas tienen un numerador negativo y un
denominador positivo. El uso de un denominador negativo haría que algunos de los operadores relacionales
dieran resultados incorrectos. En general, ésta es una restricción innecesaria. Modifique el constructor para
permitir que el usuario pase un denominador negativo y que todos los operadores continúen funcionando
correctamente.'''
# Ejemplo de uso de las clases Fraccion

# Importar la clase Fraccion
from fraccion import Fraccion

try:
    fraccion1 = Fraccion(3, 4)
    fraccion2 = Fraccion(2, -5)  # Denominador negativo

    # Prueba de los métodos getNum y getDen
    print("Numerador de fraccion1:", fraccion1.getNum())
    print("Denominador de fraccion1:", fraccion1.getDen())

    # Pruebas de operadores relacionales
    if fraccion1 == fraccion2:
        print("Las fracciones son iguales.")
    else:
        print("Las fracciones no son iguales.")

    if fraccion1 > fraccion2:
        print("fraccion1 es mayor que fraccion2.")
    else:
        print("fraccion1 no es mayor que fraccion2.")

    # Más pruebas y operaciones con las fracciones...

except ValueError as e:
    print(f"Error: {e}")


