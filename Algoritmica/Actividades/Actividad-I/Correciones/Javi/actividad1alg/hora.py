'''actividad6:Implementar la clase de uso común Clase Hora, de manera que sea robusta y completarla con métodos
necesarios'''
class Hora:
    def __init__(self, hora, minuto):
        # Validar que los valores proporcionados son enteros
        if not isinstance(hora, int) or not isinstance(minuto, int):
            raise ValueError("Hora y minuto deben ser enteros.")

        # Validar que los valores de hora y minuto estén en rangos válidos
        if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
            raise ValueError("Hora no válida.")

        self.hora = hora
        self.minuto = minuto

    def __str__(self):
        return f'{self.hora:02d}:{self.minuto:02d}'

# Ejemplo de uso de la clase Hora
mi_hora = Hora(14, 30)
print("Hora actual:", mi_hora)

