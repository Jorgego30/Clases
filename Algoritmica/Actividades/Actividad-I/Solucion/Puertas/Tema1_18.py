from Class_Puertas import *


def main():
    # c0 = PuertaNOT("C0")
    # print(f"La salida de la puerta NOT es: {c0.obtenerSalida()}")
    # c1 = PuertaAND("C1")
    # print(f"La salida de la puerta AND es: {c1.obtenerSalida()}")
    # c2 = PuertaNAND("C2")
    # print(f"La salida de la puerta NAND es: {c2.obtenerSalida()}")
    # c3 = PuertaOR("C3")
    # print(f"La salida de la puerta OR es: {c3.obtenerSalida()}")
    # c4 = PuertaNOR("C4")
    # print(f"La salida de la puerta NOR es: {c4.obtenerSalida()}")
    # c5 = PuertaXOR("C5")
    # print(f"La salida de la puerta XOR es: {c5.obtenerSalida()}")
    firstClaus = PuertaAND("Primera clausura")
    secondClaus = PuertaAND("Segunda clausura")
    firstDigit = firstClaus.ejecutarLogicaDePuerta() 
    secondDigit = secondClaus.ejecutarLogicaDePuerta() 
    NORClaus = PuertaNOR("Puerta NOR")
    NORDigit = NORClaus.ejecutarLogicaDePuerta()
    print(NORDigit)
    # final = PuertaNOR('C')
  
    # print(f"\nEl resultado de NOT((A AND B) OR (C AND D))")
# NOT(A and B) and NOT (C and D).
main()
