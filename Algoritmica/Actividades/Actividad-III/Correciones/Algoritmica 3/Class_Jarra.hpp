
class Jarra {
private:
    int capacidad; // Capacidad total de la jarra
    int cantidad;  // Cantidad actual de agua en la jarra

public:
    // Constructor
    Jarra(int cap) : capacidad(cap), cantidad(0) {}

    // Métodos
    int getCapacidad() const {
        return capacidad;
    }

    int getCantidad() const {
        return cantidad;
    }

    void llenar() {
        cantidad = capacidad;
    }

    void vaciar() {
        cantidad = 0;
    }

    void transferirA(Jarra& otraJarra) {
        int espacioDisponible = otraJarra.getCapacidad() - otraJarra.getCantidad();
        if (cantidad <= espacioDisponible) {
            otraJarra.cantidad += cantidad;
            cantidad = 0;
        } else {
            cantidad -= espacioDisponible;
            otraJarra.llenar();
        }
    }

    bool estaVacia() const {
        return cantidad == 0;
    }

    bool estaLlena() const {
        return cantidad == capacidad;
    }
};