#include "Class_Puertas_Logicas.hpp"
#include <iostream>
#include <cstdlib>

using namespace std;

int main(){
    char stopme;

    //Ejercicio1
    AndGate Xor(" XOR1 ");
    Xorgate Xor2("Xor2");
    OrGate Or("Or1");
    Nandgate Nand("Nand1");

    //Peticion de pines y resultados
    cout<<Xor.getPinA()<<Xor.getPinB()<<endl<<Xor.getOutput()<<endl;
    cout<<Xor2.getPinA()<<Xor2.getPinB()<<Xor2.getOutput()<<endl;
    cout<<Or.getPinA()<<Or.getPinB()<<Or.getOutput()<<endl;
    cout<<Nand.getPinA()<<Nand.getPinB()<<Nand.getOutput()<<endl;


    //Ejercicio2
    bool A=rand()%2;
    bool B=rand()%2;
    bool C=rand()%2;
    bool D=rand()%2;
    cout<<A<<B<<C<<D<<endl;

    AndGate andGate1("AndGate1");
    AndGate andGate2("AndGate2");
    OrGate orGate("OrGate");
    NotGate notGate("NotGate");

    // Conectar las puertas lógicas apropiadamente
    Connector connector1(&andGate1, &andGate2);
    Connector connector2(&andGate2, &orGate);
    Connector connector3(&orGate, &notGate);
    
    // Establecer las entradas de las puertas lógicas
    andGate1.setNextPin(A);
    andGate1.setNextPin(B);
    andGate2.setNextPin(C);
    andGate2.setNextPin(D);


    // Obtener y mostrar la salida
    bool output = notGate.getOutput();
    cout << "Output: " << output << endl;

    // Definir las puertas lógicas y conectarlas
    AndGate andGat1("AndGate1");
    AndGate andGat2("AndGate2");
    NotGate notGat1("NotGate1");
    NotGate notGat2("NotGate2");

    // Conectar las puertas lógicas apropiadamente
    Connector conector1(&andGat1, &notGat1);
    Connector conector2(&andGat2, &notGat2);

    // Establecer las entradas de las puertas lógicas
    andGate1.setNextPin(A);
    andGate1.setNextPin(B);
    andGate2.setNextPin(C);
    andGate2.setNextPin(D);

    // Obtener y mostrar la salida
    bool otput = notGat1.getOutput() && notGat2.getOutput();
    cout << "Output: " << otput << endl;

    return 0;

    

}
