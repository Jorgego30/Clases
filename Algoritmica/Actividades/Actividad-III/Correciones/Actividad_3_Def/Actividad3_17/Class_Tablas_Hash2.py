class TablaHash:
    def __init__(self):
        self.factorcargamax = 0.8 #Factor de carga maximo
        self.factorredimensionado = 1.5 #Tamanho de la tabla redimensionada
        self.tamano = 11 #Tamanho inicial de la tabla
        self.nitems = 0 #Inicializacion del numero de items en la tabla
        self.slots = [None] * self.tamano
        self.datos = [None] * self.tamano

    def agregar(self, clave, dato):
        if ((self.nitems+1)/self.tamano) > self.factorcargamax:           #Si el factor de carga se excede, se redimensiona la tabla
            tamanonuevo = round(self.tamano * self.factorredimensionado)
            print(f"Factor de carga excedido. Se comienza a redimensionar la tabla. El tamanho de la misma pasara de {self.tamano} posiciones a {tamanonuevo} posiciones.")
            listanuevaslots, listanuevadatos, nitemsnuevo = crearlistasredimensionadas(self.slots, self.datos, tamanonuevo)
            self.slots = listanuevaslots.copy()
            self.datos = listanuevadatos.copy()
            self.tamano = tamanonuevo
            self.nitems = nitemsnuevo


        valorHash = funcionHash(clave, len(self.slots))

        if self.slots[valorHash] == None:
            self.slots[valorHash] = clave
            self.datos[valorHash] = dato
            self.nitems+=1 #Aumento del numero de items de la tabla
        else:
            if self.slots[valorHash] == clave:
                self.datos[valorHash] = dato  # reemplazo
            else:
                proximaSlot = rehash(valorHash, len(self.slots))
                while self.slots[proximaSlot] != None and self.slots[proximaSlot] != clave:
                    proximaSlot = rehash(proximaSlot, len(self.slots))

                if self.slots[proximaSlot] == None:
                    self.slots[proximaSlot] = clave
                    self.datos[proximaSlot] = dato
                    self.nitems+=1 #Aumento del numero de items de la tabla
                else:
                    self.datos[proximaSlot] = dato  # reemplazo

    def obtener(self, clave):
        slotInicio = funcionHash(clave, len(self.slots))

        dato = None
        parar = False
        encontrado = False
        posicion = slotInicio
        while self.slots[posicion] != None and not encontrado and not parar:
            if self.slots[posicion] == clave:
                encontrado = True
                dato = self.datos[posicion]
            else:
                posicion = rehash(posicion, len(self.slots))
                if posicion == slotInicio:
                    parar = True
        return dato

    def __len__(self):
        return self.nitems
    def __getitem__(self, clave):
        return self.obtener(clave)

    def __setitem__(self, clave, dato):
        self.agregar(clave, dato)

def funcionHash(clave, tamano):
    return clave % tamano

def rehash(hashViejo, tamano):
    return (hashViejo+1) % tamano

def crearlistasredimensionadas(listaslots, listadatos, tamano):
    #Funcion que devuelve las listas de slots, datos y el numero de items de la nuevla tabla hash redimensionada
    listaslots_nueva = [None] * tamano
    listadatos_nueva = [None] * tamano
    nitems_nuevo = 0
    indicelista = -1
    for elemento in listaslots:
        indicelista += 1
        if elemento != None:
            valorHash = funcionHash(elemento, len(listaslots_nueva))
            clave = listaslots[indicelista]
            dato = listadatos[indicelista]
            if listaslots_nueva[valorHash] == None:
                listaslots_nueva[valorHash] = clave
                listadatos_nueva[valorHash] = dato
                nitems_nuevo+=1 #Aumento del numero de items de la tabla
            else:
                if listaslots_nueva[valorHash] == clave:
                    listadatos_nueva[valorHash] = dato  # reemplazo
                else:
                    proximaSlot = rehash(valorHash, len(listaslots_nueva))
                    while listaslots_nueva[proximaSlot] != None and listaslots_nueva[proximaSlot] != clave:
                        proximaSlot = rehash(proximaSlot, len(listaslots_nueva))

                    if listaslots_nueva[proximaSlot] == None:
                        listaslots_nueva[proximaSlot] = clave
                        listadatos_nueva[proximaSlot] = dato
                        nitems_nuevo+=1 #Aumento del numero de items de la tabla
                    else:
                        listadatos_nueva[proximaSlot] = dato  # reemplazo
    return listaslots_nueva, listadatos_nueva, nitems_nuevo