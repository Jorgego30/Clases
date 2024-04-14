class TablaHash:
    def __init__(self):
        self.tamano = 11
        self.slots = [None] * self.tamano
        self.datos = [None] * self.tamano
        self.cantidad_elementos = 0  # Contador de elementos

    def agregar(self, clave, dato):
        if (self.cantidad_elementos + 1) / self.tamano > 0.7:  # Umbral del factor de carga
            self.redimensionar()
        
        valorHash = self.funcionHash(clave, len(self.slots))

        if self.slots[valorHash] == None:
            self.slots[valorHash] = clave
            self.datos[valorHash] = dato
            self.cantidad_elementos += 1
        else:
            if self.slots[valorHash] == clave:
                self.datos[valorHash] = dato  # reemplazo
            else:
                proximaSlot = self.rehash(valorHash, len(self.slots))
                while self.slots[proximaSlot] != None and self.slots[proximaSlot] != clave:
                    proximaSlot = self.rehash(proximaSlot, len(self.slots))

                if self.slots[proximaSlot] == None:
                    self.slots[proximaSlot] = clave
                    self.datos[proximaSlot] = dato
                    self.cantidad_elementos += 1
                else:
                    self.datos[proximaSlot] = dato  # reemplazo

    def redimensionar(self):
        nuevo_tamano = self.tamano * 2  # Se duplica el tamaño
        nuevos_slots = [None] * nuevo_tamano
        nuevos_datos = [None] * nuevo_tamano

        for i in range(self.tamano):
            if self.slots[i] != None:
                valorHash = self.funcionHash(self.slots[i], nuevo_tamano)
                while nuevos_slots[valorHash] != None:
                    valorHash = self.rehash(valorHash, nuevo_tamano)
                nuevos_slots[valorHash] = self.slots[i]
                nuevos_datos[valorHash] = self.datos[i]

        self.slots = nuevos_slots
        self.datos = nuevos_datos
        self.tamano = nuevo_tamano

    def funcionHash(self, clave, tamano):
        return clave % tamano

    def rehash(self, hashViejo, tamano):
        return (hashViejo+1) % tamano

    def obtener(self, clave):
        slotInicio = self.funcionHash(clave, len(self.slots))

        dato = None
        parar = False
        encontrado = False
        posicion = slotInicio
        while self.slots[posicion] != None and not encontrado and not parar:
            if self.slots[posicion] == clave:
                encontrado = True
                dato = self.datos[posicion]
            else:
                posicion = self.rehash(posicion, len(self.slots))
                if posicion == slotInicio:
                    parar = True
        return dato

    def __getitem__(self, clave):
        return self.obtener(clave)

    def __setitem__(self, clave, dato):
        self.agregar(clave, dato)

    def __len__(self):
        return self.cantidad_elementos
