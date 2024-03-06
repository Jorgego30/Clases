/*actividad2:Cree una serie de puertas que demuestren que la siguiente ecuación NOT((A and B) or (C and D)) es
equivalente a NOT(A and B) and NOT (C and D). Asegúrese de usar algunas de sus nuevas puertas en la
simulación.*/
#include <iostream>

class PuertaAND {
public:
    PuertaAND(bool input1, bool input2) : input1(input1), input2(input2) {}

    bool operacion_and() {
        return input1 && input2;
    }

private:
    bool input1;
    bool input2;
};

class PuertaNOT {
public:
    PuertaNOT(bool input) : input(input) {}

    bool operacion_not() {
        return !input;
    }

private:
    bool input;
};

int main() {
    // Entradas
    bool A = true;
    bool B = false;
    bool C = true;
    bool D = false;

    // NOT((A and B) or (C and D))
    PuertaAND puerta_and1(A, B);
    PuertaAND puerta_and2(C, D);

    bool resultado_or = PuertaNOR(puerta_and1.operacion_and(), puerta_and2.operacion_and()).operacion_nor();
    bool resultado_not_or = PuertaNOT(resultado_or).operacion_not();

    // NOT(A and B) and NOT(C and D)
    bool resultado_not_A_and_B = PuertaNOT(PuertaAND(A, B).operacion_and()).operacion_not();
    bool resultado_not_C_and_D = PuertaNOT(PuertaAND(C, D).operacion_and()).operacion_not();

    // Verificar la equivalencia
    if (resultado_not_or == (resultado_not_A_and_B && resultado_not_C_and_D)) {
        std::cout << "Las expresiones son equivalentes." << std::endl;
    } else {
        std::cout << "Las expresiones no son equivalentes." << std::endl;
    }

    return 0;
}

