'''actividad5: Reescribir la clase común Clase Fecha, de manera que sea robusta y completarla con métodos necesarios'''

class Fecha:
    def __init__(self, dia, mes, año):
        if not isinstance(dia, int) | not isinstance(mes, int) | not isinstance(año, int):
            raise ValueError("Día, mes y año deben ser enteros.")

        if mes < 1 | mes > 12 | dia < 1 | dia > self.dias_en_mes(mes, año):
            raise ValueError("Fecha no válida.")

        self.dia = dia
        self.mes = mes
        self.año = año

    def __str__(self):
        return f'{self.dia:02d}/{self.mes:02d}/{self.año}'

    def bisiesto(self):
        return self.año % 4 == 0 & (self.año % 100 != 0 | self.año % 400 == 0)

    def es_menor(self, fecha1):
        if self.año < fecha1.año:
            return True
        elif self.año > fecha1.año:
            return False
        if self.mes < fecha1.mes:
            return True
        elif self.mes > fecha1.mes:
            return False
        return self.dia < fecha1.dia

    def dias_en_mes(self, mes, año):
        dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if mes == 2 & self.bisiesto():
            return 29
        return dias_por_mes[mes]

