class TablaHash:
    def __init__(self):
        self.tamano = 11
        self.slots = [None] * self.tamano
        self.datos = [None] * self.tamano

    def agregar(self, clave, dato):
        valorHash = self.funcionHash(clave, len(self.slots))
        proximaSlot = valorHash
        intento = 1
        while self.slots[proximaSlot] is not None and self.slots[proximaSlot] != clave:
            proximaSlot = self.rehashCuadratico(valorHash, len(self.slots), intento)
            intento += 1

            if proximaSlot == valorHash:
                raise ValueError("Tabla llena, no se puede agregar más elementos.")

        self.slots[proximaSlot] = clave
        self.datos[proximaSlot] = dato

    def funcionHash(self, clave, tamano):
        return clave % tamano

    def rehashCuadratico(self, hashViejo, tamano, intento):
        return (hashViejo + intento**2) % tamano

    def obtener(self, clave):
        slotInicio = self.funcionHash(clave, len(self.slots))

        dato = None
        parar = False
        encontrado = False
        posicion = slotInicio
        intento = 1  # Agrega un contador de intentos aquí
        while self.slots[posicion] is not None and not encontrado and not parar:
            if self.slots[posicion] == clave:
                encontrado = True
                dato = self.datos[posicion]
            else:
                posicion = self.rehashCuadratico(posicion, len(self.slots), intento)  # Pasa el intento aquí
                intento += 1  # Incrementa el intento

                if posicion == slotInicio:
                    parar = True
        return dato

    def __getitem__(self, clave):
        return self.obtener(clave)

    def __setitem__(self, clave, dato):
        self.agregar(clave, dato)
