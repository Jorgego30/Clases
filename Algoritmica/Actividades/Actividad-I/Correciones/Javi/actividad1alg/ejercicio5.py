'''actividad5: Reescribir la clase común Clase Fecha, de manera que sea robusta y completarla con métodos necesarios'''

from fecha import Fecha

# Ejemplo de uso de la clase Fecha
mi_fecha = Fecha(35, 1, 2022)
print("Fecha actual:", mi_fecha)

otra_fecha = Fecha(15, 6, 2023)

# Comparar fechas
if mi_fecha.es_menor(otra_fecha):
    print("La fecha actual es anterior a la otra fecha.")
else:
    print("La fecha actual es posterior a la otra fecha.")

