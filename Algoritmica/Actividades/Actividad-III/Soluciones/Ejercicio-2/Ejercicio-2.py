from Class_Jarras import *

# Ejercicio 2
def ejercicio2():
    # Se establece que x e y son 4 y 3 respectivamente pues es lo que manda el ejercicio 2
    x = 4
    y = 3

    # Se pasan las capacidades de las jarras como objetos
    jarra4Litros = Jarra(4)
    jarra3Litros = Jarra(3)

    # Se hace la transposicion de liquidos como viene definida en la clase
    jarra4Litros.transpose(jarra3Litros,2)

def validacion():
    #Se definen x e y
    x = 0
    y = 0
    #Se hace la validacion
    while x <= y:
        try:
        # Se le pide al usuario que indique las capacidades de las jarras
            x = int(input("Indique la capacidad de la primera jarra: "))
            y = int(input("Indique la capacidad de la segunda jarra: "))

            #Se lanzan las excepciones
            if x <= 0 or y <= 0:
                x = 0
                y = 0
                raise Exception("Ambos valores deben ser positivos")
            if x%2 != 0:
                x=0
                raise Exception("La primera jarra deber tener una capacidad de numero par ya que buscamos que termine con la mitad de su liquido")

        except ValueError:
            print("Ambos valores deben ser números enteros")
        except Exception as e:
            print("Error:", e)
            continue
        
    return x,y

# Ejercicio 8
def ejercicio8():
    x,y = validacion()

    primerJarra = Jarra(x)
    segundaJarra = Jarra(y)

    primerJarra.transpose(segundaJarra,x/2)


print("Ejercicio 2:\n")
ejercicio2()

print("\nEjercicio 8:\n")
ejercicio8()