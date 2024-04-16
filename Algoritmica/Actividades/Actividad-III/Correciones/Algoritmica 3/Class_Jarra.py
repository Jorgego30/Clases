class Jarras:
    def __init__(self, capacidad_x, capacidad_y):
        self.capacidad_x = capacidad_x
        self.capacidad_y = capacidad_y
        self.contenido_x = 0
        self.contenido_y = 0

    def llenar_x(self):
        self.contenido_x = self.capacidad_x

    def llenar_y(self):
        self.contenido_y = self.capacidad_y

    def vaciar_x(self):
        self.contenido_x = 0

    def vaciar_y(self):
        self.contenido_y = 0

    def transferir_x_a_y(self):
        espacio_disponible = self.capacidad_y - self.contenido_y
        if self.contenido_x <= espacio_disponible:
            self.contenido_y += self.contenido_x
            self.contenido_x = 0
        else:
            self.contenido_x -= espacio_disponible
            self.contenido_y = self.capacidad_y

    def transferir_y_a_x(self):
        espacio_disponible = self.capacidad_x - self.contenido_x
        if self.contenido_y <= espacio_disponible:
            self.contenido_x += self.contenido_y
            self.contenido_y = 0
        else:
            self.contenido_y -= espacio_disponible
            self.contenido_x = self.capacidad_x

    def obtener_x_medio(self):
        # Llenar la jarra de Y
        self.llenar_y()
        # Transferir el agua de Y a X hasta que X esté lleno o Y esté vacío
        while self.contenido_x < self.capacidad_x and self.contenido_y > 0:
            self.transferir_y_a_x()
        # Vaciar X si tiene más de X/2 litros
        if self.contenido_x > self.capacidad_x / 2:
            self.vaciar_x()
        # Transferir el agua de Y a X hasta que X tenga X/2 litros
        while self.contenido_x < self.capacidad_x / 2:
            self.transferir_y_a_x()
        return self.contenido_x
