from Class_Colas import *

cola1 = Cola()

print(cola1.estaVacia())

cola1.agregar(1)
cola1.agregar(2)
cola1.agregar(3)

print(cola1.estaVacia())
print(f"La primera cola es {cola1}\nTiene un tamaño de {cola1.tamano()}\nSu primer elemento es: {cola1.frente()}\nSu ultimo elemento es: {cola1.ultimo()}")
print(cola1.avanzar())


cola2 = Cola()
cola2.agregar(3)
cola2.agregar(4)

print(f"La segunda cola es {cola2}")


cola1.concatenacion(cola2)

print(f"La concatenacion de ambas colas es: {cola1}") 