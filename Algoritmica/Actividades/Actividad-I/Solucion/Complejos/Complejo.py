from ClassComplejo import *

# complejo1 = Complejo(10,-20)
# print(f"Tu complejo es: {complejo1}")

# parteReal = float(input("Dime la parte real del numero (con el signo): "))
# parteImaginaria = float(input("Dime la parte imaginaria del numero (con el signo): "))

# complejo2 = Complejo(parteReal,parteImaginaria)
# print(f"Tu complejo es: {complejo2}")
complejo1 = Complejo(5, -2)
complejo2 = Complejo(2, -3)


if(complejo1 < complejo2):
    print(f"{complejo1} es menor que {complejo2}")
elif(complejo1 <= complejo2):
    print(f"{complejo1} es menor o igual que {complejo2}")
elif(complejo1 > complejo2):
    print(f"{complejo1} es mayor que {complejo2}")
elif(complejo1 >= complejo2):
    print(f"{complejo1} es mayor o igual que {complejo2}")
elif(complejo1 == complejo2):
    print(f"{complejo1} es igual que {complejo2}")

sumaComplex = complejo1 + complejo2
restaComplex = complejo1 - complejo2
multiplicacionComplex = complejo1 * complejo2
divisionComplex = complejo1 / complejo2
potenciaComplex = complejo1 * complejo1

print(f"La suma del complejo {complejo1} y el complejo {complejo2} es {sumaComplex}")
print(f"La resta del complejo {complejo1} y el complejo {complejo2} es {restaComplex}")
print(f"La multiplicacion del complejo {complejo1} y el complejo {complejo2} es {multiplicacionComplex}")
print(f"La division del complejo {complejo1} y el complejo {complejo2} es {divisionComplex}")
print(f"La potencia del complejo {complejo1} es {potenciaComplex}")
print(f"El valor absoluto del complejo {complejo1} es {complejo1.valor_absoluto()}")
print(f"El conjugado del complejo {complejo1} es {complejo1.conjugado()}")
print(f"La parte real del complejo {complejo1} es {complejo1.getReal()} la parte imaginaria es {complejo1.getImaginary()}")