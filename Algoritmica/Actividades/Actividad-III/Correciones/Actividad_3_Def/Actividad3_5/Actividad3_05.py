#Definimos la función para calcular que obras es más rentable llevar:
def calcular_obras(peso,obras):
    #Creamos dos listas vacías:
    pesos=[]
    valor=[]
    #Metemos los valores necesarios en nuevas listas para que sean más accesibles:
    for i in range(0,len(obras)):
        pesos.append(obras[i][1])
        valor.append(obras[i][2])

    #Creamos una variable que es una tabla con tantas filas como obras de arte y tantas columnas como el peso total de la mochila
    tabla = [[0] * (peso + 1) for _ in range(len(obras) + 1)]
    
    for i in range(len(obras)): #Vamos recorriendo obra a obra (filas de)
        for j in range(peso+1): #Vamos recorriendo las columnas de la tabla
            if pesos[i]<=j: #Si el peso de la obra i es menor que el peso de esa columna ejecutamos esto:
                #En la fila de esa obra y la columna del peso que estamos comprobando metemos el número máximo entre los valores de abajo
                tabla[i][j] = max(tabla[i - 1][j], valor[i] + tabla[i - 1][j - pesos[i]])
            else:
                #En la fila de esa obra y la columna del peso que estamos comprobando metemos el valor que está en la casilla de encima:
                tabla[i][j] = tabla[i - 1][j]

    #Cogemos el último valor de la tabla que equivale al valor máximo de ganancias que se puede obtener
    valor_maximo = tabla[len(obras) - 1][peso]

    #Vemos que obras son las que se necesitan para maximizar las ganancias:
    peso_actual=peso
    obras_seleccionadas=[]
    #Recorremos las obras desde la última hasta la primera
    for i in range(len(obras) - 1, -1, -1):
        #Si en la fila de esa obra en la columna del peso actual el valor es distinto al de la casilla de encima se mete en la lista de obras_seleccionadas
        if tabla[i][peso_actual] != tabla[i - 1][peso_actual]:
            obras_seleccionadas.append(obras[i][0]) #Si metemos esa obra en la mochila metemos en esta lista su número de identificación
            peso_actual -= pesos[i] #Vamos actualizando el peso restante que puede entrar en la mochila
    
    #Invertimos la lista con el números de las obras que cogemos:
    obras_seleccionadas.reverse()

    #Devolvemos los resultados:
    return valor_maximo,obras_seleccionadas


#Creamos dos variables para el peso que aguanta la mochila y una lista con los datos de las obras:
peso=20
obras=[[1,2,3],[2,3,4],[3,4,8],[4,5,8],[5,9,10]]

#Llamamos a la función para saber que obras es más rentable llevar:
dinero,cuales=calcular_obras(peso,obras)

#Comunicamos los resultados:
print("Las obras disponibles son: ") #Creamos una tabla con las obras disponibles
for i in range(0,len(obras)):
    print("Obra ",obras[i][0]," peso: ",obras[i][1]," valor: ",obras[i][2])
print("El valor máximo de dinero que se puede ganar en este caso es: ",dinero)
print("Las obras seleccionadas son: ",cuales)


#Repetimos el ejercicio pero esta vez pidiendo valores iniciales:
while True:
    try:
        peso2=int(input("Dame el peso máximo que soporta la mochila: "))
        obras=int(input("Dame el número de obras disponibles que hay: "))
        obras2=[]

        for i in range(1,obras+1,1):
            try:
                lista_auxiliar=[]
                lista_auxiliar.append(i)
                print("Obra ",i,": ")
                peso_obra=int(input("Dame el peso de la obra: "))
                valor_obra=int(input("Dame el valor de la obra: "))
                lista_auxiliar.append(peso_obra)
                lista_auxiliar.append(valor_obra)
                obras2.append(lista_auxiliar)
            except:
                print("El valor debía ser numérico. Vuelva a introducirlo")
        break
    except:
        print("El valor debía ser numérico y sin decimales. Vuelva a introducirlo")

#Llamamos a la función para saber que obras es más rentable llevar:
dinero2,cuales2=calcular_obras(peso2,obras2)

#Comunicamos los resultados:
print("Las obras disponibles son: ") #Creamos una tabla con las obras disponibles
for i in range(0,len(obras2)):
    print("Obra ",obras2[i][0]," peso: ",obras2[i][1]," valor: ",obras2[i][2])
print("El valor máximo de dinero que se puede ganar en este caso es: ",dinero2)
print("Las obras seleccionadas son: ",cuales2)
