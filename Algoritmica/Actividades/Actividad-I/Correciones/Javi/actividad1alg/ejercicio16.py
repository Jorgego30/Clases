'''ejercicio 16: ¿Puedes mejorar el algoritmo del problema anterior para que sea lineal? Explica. Este codigo utiliza un diccionario contador y luego mira el k-esimo mas pequeño utilizando listas por esto va a ser lineal. '''

def seleccion_lineal_con_repeticiones(lista, k):
    contador = {}
    
    for elemento in lista:
        if elemento not in contador:
            contador[elemento] = 1
    
    elementos_unicos = list(contador.keys())

    # Verificar si k es válido
    if 0 <= k < len(elementos_unicos):
        return elementos_unicos[k]
    else:
        return None

# Ejemplo de uso
try:
    # Solicitar al usuario la entrada de la lista de números
    entrada_usuario = input("Introduce la lista de números separados por espacios: ")
    mi_lista = list(map(int, entrada_usuario.split()))

    # Solicitar al usuario el valor de k
    k = int(input("Introduce el valor de k:"))

    # Calcular el k-ésimo elemento más pequeño
    resultado = seleccion_lineal_con_repeticiones(mi_lista, k)

    if resultado is not None:
        print(f'El {k}-ésimo número más pequeño contando los repetidos como uno solo es: {resultado}')
    else:
        print('El valor de k no es válido para la longitud de la lista.')

except ValueError:
    print('Entrada inválida. Asegúrate de ingresar una lista de números y un valor de k válido.')
