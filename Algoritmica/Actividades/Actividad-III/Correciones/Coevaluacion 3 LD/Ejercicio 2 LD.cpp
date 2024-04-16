/*Escribe un programa de POO para resolver el siguiente problema:
Tienes dos jarras, una de 4 litros y otra de 3 litros. Ninguna de las jarras tiene marcas en ella. 
Hay una bomba que se puede utilizar para llenar las jarras con agua. ¿Cómo se pueden obtener exactamente 
dos litros de agua en la jarra de 4 litros?*/
#include <iostream>

class Jarra {
public:
    Jarra(int capacidad) : capacidad(capacidad), contenido(0) {}

    void llenar() {
        contenido = capacidad;
    }

    void vaciar() {
        contenido = 0;
    }

    void verterEn(Jarra& otra) {
        int total = contenido + otra.contenido;
        if (total <= otra.capacidad) {
            otra.contenido = total;
            contenido = 0;
        } else {
            contenido = total - otra.capacidad;
            otra.contenido = otra.capacidad;
        }
    }

    int getContenido() const {
        return contenido;
    }

private:
    int capacidad;
    int contenido;
};

int main() {
    Jarra jarra4(4);
    Jarra jarra3(3);

    jarra3.llenar();
    jarra3.verterEn(jarra4);
    jarra3.llenar();
    jarra3.verterEn(jarra4);
    jarra4.vaciar();
    jarra3.verterEn(jarra4);
    jarra3.llenar();
    jarra3.verterEn(jarra4);

    std::cout << "Contenido de la jarra de 4 litros: " << jarra4.getContenido() << " litros\n";

    return 0;
}
