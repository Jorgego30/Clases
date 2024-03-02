'''actividad6:Implementar la clase de uso común Clase Hora, de manera que sea robusta y completarla con métodos
necesarios'''

from hora import Hora

try:
    # Ejemplo de uso de la clase Hora
    mi_hora = Hora(14, 30)
    print("Hora actual:", mi_hora)

    # Intentar crear una hora con valores no válidos (esto debería generar un error)
    hora_invalida = Hora(25, 70)

except ValueError as e:
    print(f"Error: {e}")

