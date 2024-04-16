#Definimos una función que calcule el número mínimo necesario de cada moneda para dar el cambio:
def min_monedas(vuelta, monedas):
    #Inicializamos todos los valores en infinito porque debe ser un valor alto para que no falle el código
    tabla=[float('inf')]*(vuelta+1) 
    #Creamos una tabla para guardar cuantas monedas de cada tipo necesitamos
    monedas_utilizadas = [[] for _ in range(vuelta + 1)] 
    tabla[0]=0 #Damos valor 0 al primer elemento de la tabla  

    #Entramos en un bucle:
    for i in range(1,vuelta+1):
        for moneda in monedas: #Entramos en otro bucle para cada valor de moneda disponible
            if moneda<=i: #Si el valor de la moneda es menor que i ejecutamos lo siguiente
                if tabla[i - moneda] + 1 < tabla[i]: 
                    #Si al usar la moneda actual se obtiene un resultado mejor que el anterior,
                    # actualizamos la tabla con el nuevo valor.
                    tabla[i] = tabla[i - moneda] + 1 
                    #Actualizamos las monedas utilizadas para la vuelta actual
                    monedas_utilizadas[i] = monedas_utilizadas[i - moneda] + [moneda]
    #Devolvemos los resultados:
    return tabla[vuelta],monedas_utilizadas[vuelta]


#Creamos dos variables con las monedas que tenemos disponibles para el cambio y el total a devolver:
monedas=[1,2,5,8,10,20]
vuelta=33

#Llamamos a la función para que nos de el mínimo de monedas necesarias y cuantas de cada valor se necesitan:
cantidad_monedas,monedas_vuelta=min_monedas(vuelta, monedas)

#Pasamos los resultados obtenidos a un diccionario para facilitar dar los resultados:
conteo_monedas={moneda: monedas_vuelta.count(moneda) for moneda in set(monedas_vuelta)}

#Comunicamos los resultados:
print("Devolución de 33 céntimos: ")
print("Cantidad mínima de monedas necesarias:", cantidad_monedas)
print("Monedas utilizadas y su cantidad:")
for moneda, cantidad in conteo_monedas.items():
    print(moneda, "céntimos:", cantidad)


#Preguntamos los datos esta vez y repetimos el proceso:
#Creamos dos variables con las monedas que tenemos disponibles para el cambio y el total a devolver:
monedas2=[]
while True:
    try:
        vuelta2=int(input("Dame la vuelta que quieres que devuelvan (en céntimos): "))
        moneda=-1
        while moneda!="":
            try:
                moneda=str(input("Dame el valor de una moneda que se pueda devolver en el cambio (Pulsa ENTER para dejar de añadir): "))
                if int(moneda)<=0:
                    print("Moneda no válida, debe ser positiva")
                else:
                    monedas2.append(int(moneda))
            except:
                print("Debía ser un valor numérico")
        break
    except:
        print("El valor debía ser numérico. Vuelva a introducirlo")


#Llamamos a la función para que nos de el mínimo de monedas necesarias y cuantas de cada valor se necesitan:
cantidad_monedas2,monedas_vuelta2=min_monedas(vuelta2, monedas2)

#Pasamos los resultados obtenidos a un diccionario para facilitar dar los resultados:
conteo_monedas2={moneda2: monedas_vuelta2.count(moneda2) for moneda2 in set(monedas_vuelta2)}

#Comunicamos los resultados:
print("Devolución de ",vuelta2," céntimos: ")
print("Cantidad mínima de monedas necesarias:", cantidad_monedas2)
print("Monedas utilizadas y su cantidad:")
for moneda2, cantidad2 in conteo_monedas2.items():
    print(moneda2, "céntimos:", cantidad2)