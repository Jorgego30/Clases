from Class_Monticulos import *
#6. Utilizando el método construirMonticulo, escribe una función de ordenamiento que pueda ordenar una
#lista en tiempo 𝑶𝑶(𝒏𝒏𝒏𝒏𝒏𝒏𝒏𝒏𝒏𝒏). (Buscar heapsort)

#Indexamos la clase 

Monbi=MonticuloBinario()

lista = [12, 11, 13, 5, 6, 7]
#Creamos unmonticulo máximo
Monbi.construirMonticulo(lista)
print("Array ordenado es:")

#Aplicamosheapsort

print(Monbi.heapsort())