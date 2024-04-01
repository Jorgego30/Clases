class Conjunto:
    def __init__(self):
        self.elementos = []

    def inserta(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def elimina(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)

    def __str__(self):
        cadena = '{'
        if len(self.elementos) > 0:
            for elemento in self.elementos[:-1]:
                cadena += str(elemento) + ', '
            cadena += str(self.elementos[-1])
        return cadena + '}'

    def tamaño(self):
        return len(self.elementos)

    def pertenece(self, elemento):
        return elemento in self.elementos

    def unión(self, otro_conjunto):
        nuevo_conjunto = Conjunto()
        for elemento in self.elementos:
            nuevo_conjunto.inserta(elemento)
        for elemento in otro_conjunto.elementos:
            nuevo_conjunto.inserta(elemento)
        return nuevo_conjunto

    def intersección(self, otro_conjunto):
        nuevo_conjunto = Conjunto()
        for elemento in self.elementos:
            if elemento in otro_conjunto.elementos:
                nuevo_conjunto.inserta(elemento)
        return nuevo_conjunto

    def diferencia(self, otro_conjunto):
        nuevo_conjunto = Conjunto()
        for elemento in self.elementos:
            if elemento not in otro_conjunto.elementos:
                nuevo_conjunto.inserta(elemento)
        return nuevo_conjunto

    def incluye(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            if elemento not in self.elementos:
                return False
        return True
# Definir dos conjuntos
conjunto1 = Conjunto()
conjunto2 = Conjunto()

# Insertar elementos en los conjuntos
conjunto1.inserta(1)
conjunto1.inserta(2)
conjunto1.inserta(3)
conjunto1.inserta(4)

conjunto2.inserta(3)
conjunto2.inserta(4)
conjunto2.inserta(5)
conjunto2.inserta(6)

# Imprimir los conjuntos
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Realizar operaciones de conjuntos
print("Unión:", conjunto1.unión(conjunto2))
print("Intersección:", conjunto1.intersección(conjunto2))
print("Diferencia (Conjunto 1 - Conjunto 2):", conjunto1.diferencia(conjunto2))
print("Diferencia (Conjunto 2 - Conjunto 1):", conjunto2.diferencia(conjunto1))

# Verificar si un conjunto incluye a otro
print("¿El conjunto 1 incluye al conjunto 2?", conjunto1.incluye(conjunto2))
print("¿El conjunto 2 incluye al conjunto 1?", conjunto2.incluye(conjunto1))

# Eliminar un elemento de un conjunto
conjunto1.elimina(2)
print("Conjunto 1 después de eliminar el elemento 2:", conjunto1)

# Verificar pertenencia de un elemento
print("¿El elemento 5 pertenece al conjunto 1?", conjunto1.pertenece(5))

# Obtener tamaño de un conjunto
print("Tamaño del conjunto 1:", conjunto1.tamaño())
