class TablaHash:
    def __init__(self):
        self.tamano = 11
        self.slots = [[None]] * self.tamano
        self.datos = [[None]] * self.tamano

    def agregar(self, clave, dato):
        valorHash = self.funcionHash(clave, len(self.slots))
        #Si la posicion esta vacia, se anhade el elemento
        if self.slots[valorHash] == [None]:
            self.slots[valorHash] = [clave]
            self.datos[valorHash] = [dato]
        else:
            #En el caso de que ya exista la clave, se modifica el valor
            if clave in self.slots[valorHash]:
                indice = self.slots[valorHash].index(clave)
                self.datos[valorHash][indice] = dato
            else:
                #Si no existe la clave, se inserta ordenadamente
                indice = -1
                #Se recorre la lista hasta guardarlo
                guardado = False
                indice = -1
                while guardado == False:
                    indice += 1
                    #Si el indice no es el ultimo elemento de la lista:
                    if indice < len(self.slots[valorHash])-1:
                        if (self.slots[valorHash][indice] < clave) and (self.slots[valorHash][indice+1] > clave):
                            self.slots[valorHash].insert(indice+1, clave)
                            self.datos[valorHash].insert(indice+1, dato)
                            guardado = True
                    #Si el indice es el ultimo elemento de la lista:
                    else:
                        if self.slots[valorHash][indice] < clave:
                            self.slots[valorHash].insert(indice, clave)
                            self.datos[valorHash].insert(indice, dato)
                            guardado = True
                        else:
                            self.slots[valorHash].append(clave)
                            self.datos[valorHash].append(dato)
                            guardado = True

    def eliminar(self, clave):
        slot = self.funcionHash(clave, len(self.slots))
        #Si solo hay un elemento, el indice es 0
        if len(self.slots[slot]) == 1:
            indice = 0
        #Si hay mas de un elemento, hay que buscarlo
        else:
            indice = self.slots[slot].index(clave)
        #Si el slot tiene mas de un elemento, se elimina el indice
        if len(self.slots[slot]) > 1:
            del self.slots[slot][indice]
            del self.datos[slot][indice]
        #Si el slot solo tiene un elemento, se inicializa el slot
        else:
            self.slots[slot] = [None]
            self.datos[slot] = [None]

    def funcionHash(self, clave, tamano):
        return clave % tamano

    def rehash(self, hashViejo, tamano):
        return (hashViejo+1) % tamano

    def obtener(self, clave):
        slot = self.funcionHash(clave, len(self.slots))
        #Si solo hay un elemento, se devuelve ese elemento
        if len(self.slots[slot]) == 1:
            return self.datos[slot][0]
            
        #Si hay mas de un elemento, hay que buscarlo
        else:
            indice = self.slots[slot].index(clave)
            return self.datos[slot][indice]
        return dato

    def __getitem__(self, clave):
        return self.obtener(clave)

    def __setitem__(self, clave, dato):
        self.agregar(clave, dato)
