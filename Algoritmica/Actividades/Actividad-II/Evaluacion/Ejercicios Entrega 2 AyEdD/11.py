from Class_Estructuras_lineales_P import ListaNoOrdenada

milista = ListaNoOrdenada()

lista = [4,7,6,8,2]
milista.anexar(lista)

print(milista.fin())
print(milista.primero())
print(milista.siguiente(2))
print(milista.anterior(2))