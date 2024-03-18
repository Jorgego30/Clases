from Class_Conjuntos import *

conj = Conjunto()
conj.inserta(12)
conj.inserta(1)
conj.inserta(2)
conj.inserta(112)
conj.inserta(22)

print(f"El conjunto es: {conj}\nTiene {conj.tamaño()} elementos")

comprobante = int(input("Dime el numero que quieres comprobar si esta en el conjunto: "))

if(conj.pertenece(comprobante)==True):
    print(f"El numero {comprobante} pertenenece al conjunto")
else:
    print(f"El numero {comprobante} no pertenenece al conjunto")

conj.elimina(4)
conj.elimina(2)

print(f"El conjunto es: {conj}\n")

conjSec = Conjunto()
conjSec.inserta(3)
conjSec.inserta(31)
conjSec.inserta(22)
conjSec.inserta(132)
conjSec.inserta(32)
conjSec.inserta('a')


print(f"El segundo conjunto es: {conjSec}\nTiene {conjSec.tamaño()} elementos")


union = (conj.union(conjSec))
print(f"La union de los conjuntos {conj} y {conjSec} es: {union}")

interseccion = (conj.interseccion(conjSec))
print(f"La interseccion de los conjuntos {conj} y {conjSec} es: {interseccion}")

diferencia = (conj.diferencia(conjSec))
print(f"La diferencia de los conjuntos {conj} y {conjSec} es: {diferencia}")

print(conj.incluye(conjSec))
