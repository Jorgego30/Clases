'''actividad 1:Cree dos nuevas clases de puertas, una llamada PuertaNOR y otra llamada PuertaNAND. Las puertas NAND
funcionan como puertas AND que tienen una NOT conectada a la salida. Las puertas NOR funcionan como
puertas OR que tienen una NOT conectada a la salida. Cree la clase XOR'''

#include <iostream>

// Definición de la clase PuertaNOR
class PuertaNOR {
public:
    // Constructor que toma dos entradas booleanas
    PuertaNOR(bool input1, bool input2) : input1(input1), input2(input2) {}

    // Método para realizar la operación NOR
    bool operacion_nor() {
        // La operación NOR es la negación de la operación OR
        return !(input1 || input2);
    }

private:
    bool input1;
    bool input2;
};

// Definición de la clase PuertaNAND
class PuertaNAND {
public:
    // Constructor que toma dos entradas booleanas
    PuertaNAND(bool input1, bool input2) : input1(input1), input2(input2) {}

    // Método para realizar la operación NAND
    bool operacion_nand() {
        // La operación NAND es la negación de la operación AND
        return !(input1 && input2);
    }

private:
    bool input1;
    bool input2;
};

// Definición de la clase XOR que utiliza PuertasNOR y PuertasNAND
class XOR {
public:
    // Constructor que toma dos entradas booleanas
    XOR(bool input1, bool input2) : input1(input1), input2(input2) {}

    // Método para realizar la operación XOR utilizando PuertasNOR y PuertasNAND
    bool operacion_xor() {
        // XOR = (A NAND B) NAND (A NOR B)
        PuertaNAND puerta_nand1(input1, input2);
        PuertaNOR puerta_nor1(input1, input2);

        bool resultado_nand1 = puerta_nand1.operacion_nand();
        bool resultado_nor1 = puerta_nor1.operacion_nor();

        PuertaNAND puerta_nand2(resultado_nand1, resultado_nor1);
        return puerta_nand2.operacion_nand();
    }

private:
    bool input1;
    bool input2;
};

int main() {
    // Ejemplo de uso
    bool entrada1 = true;
    bool entrada2 = false;

    XOR puerta_xor(entrada1, entrada2);
    bool resultado = puerta_xor.operacion_xor();

    std::cout << "XOR de " << entrada1 << " y " << entrada2 << " es " << resultado << std::endl;

    return 0;
}
