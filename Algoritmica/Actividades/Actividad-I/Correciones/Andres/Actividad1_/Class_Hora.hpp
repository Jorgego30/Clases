#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

class Hora {
private:
    int horas;
    int minutos;
    int segundos;

public:
    Hora(int horas, int minutos, int segundos) {
        if (horas > 23 || horas < 0 || minutos < 0 || segundos < 0 || minutos > 59 || segundos > 59) {
            throw invalid_argument("Error en el valor introducido");
        }
        else {
            this->horas = horas;
            this->minutos = minutos;
            this->segundos = segundos;
        }
    }

    string toString() {
        return std::to_string(horas) + "/" + to_string(minutos) + "/" + to_string(segundos);
    }
};

        