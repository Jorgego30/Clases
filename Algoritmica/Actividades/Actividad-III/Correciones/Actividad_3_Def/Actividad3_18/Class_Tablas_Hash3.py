import math

class TablaHash:
    def __init__(self):
        self.tamano = 11
        self.nitems = 0 #Inicializacion del numero de items en la tabla
        self.slots = [None] * self.tamano
        self.datos = [None] * self.tamano

    def agregar(self, clave, dato):
        valorHash = self.funcionHash(clave, len(self.slots))

        if self.slots[valorHash] == None:
            self.slots[valorHash] = clave
            self.datos[valorHash] = dato
            self.nitems+=1 #Aumento del numero de items de la tabla
        else:
            if self.slots[valorHash] == clave:
                self.datos[valorHash] = dato  # reemplazo
            else:
                proximaSlot, cuadrado = self.rehash(valorHash, 0) #calculo de rehash
                #En el caso de que el slot encontrado no se encuentre dentro del rango de la tabla, se lanzara una excepcion
                if proximaSlot > self.tamano - 1:
                    raise Exception("Slot de Rehash fuera de rango de tabla. Es necesario redimensionar. 1")
                while self.slots[proximaSlot] != None and self.slots[proximaSlot] != clave:
                    proximaSlot, cuadrado = self.rehash(valorHash, cuadrado) #calculo de rehach
                    #En el caso de que el slot encontrado no se encuentre dentro del rango de la tabla, se lanzara una excepcion
                    if proximaSlot > self.tamano - 1:
                        raise Exception("Slot de Rehash fuera de rango de tabla. Es necesario redimensionar. 2")

                if self.slots[proximaSlot] == None:
                    self.slots[proximaSlot] = clave
                    self.datos[proximaSlot] = dato
                    self.nitems+=1 #Aumento del numero de items de la tabla
                else:
                    self.datos[proximaSlot] = dato  # reemplazo

    def funcionHash(self, clave, tamano):
        return clave % tamano

    def rehash(self, slotinicial, cuadradoanterior):
        #Funcion que calcula el slot de rehash. Para ello, buscara un cuadrado perfecto mayor al del anterior rehash. En caso de que no haya anterior rehash, 'cuadradoanterior' sera 0
        n = cuadradoanterior
        cuadradoencontrado = False
        #Busca el cuadrado perfecto haciendo una raiz cuadrada y comprobando si es entero
        while cuadradoencontrado == False:
            n+=1
            raiz = math.sqrt(n)
            if raiz.as_integer_ratio()[1] == 1:
                cuadradoencontrado = True
        return slotinicial + n, n

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

    def __len__(self):
        return self.nitems
    def __getitem__(self, clave):
        return self.obtener(clave)

    def __setitem__(self, clave, dato):
        self.agregar(clave, dato)
