/*Escribe la especificación informal del TAD Conjunto. Enriquece la clase Conjunto con:
 Un método elimina que borre del conjunto un elemento dado
 Un método unión que devuelva el conjunto resultante de unir dos conjuntos
 Un método intersección que devuelva un conjunto con la intersección de dos
conjuntos
 Un método diferencia que devuelva un conjunto con la diferencia entre dos
conjuntos
 Un método incluye que consulta si un conjunto dado está incluido en el
conjunto*/


//Importamos las librerias necesarias 

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Conjunto {
private:
    vector<int> elementos;
public:
    Conjunto() {}

    void inserta(int elemento) { //añade elemento al conjunto requerimiento: conjunto, elemento
        if (!pertenece(elemento)) {
            elementos.push_back(elemento);
        }
    }

    void elimina(int elemento) { //elimina elemento del conjunto requerimiento: conjunto, elemento
        for (auto it = elementos.begin(); it != elementos.end(); ++it) {
            if (*it == elemento) {
                elementos.erase(it);
                break;
            }
        }
    }

    Conjunto unionConjuntos(const Conjunto& otroConjunto) const { //une dos conjuntos, requerimiento: 2 conjuntos
        Conjunto resultado;
        for (int elemento : elementos) {
            resultado.inserta(elemento);
        }
        for (int elemento : otroConjunto.elementos) {
            resultado.inserta(elemento);
        }
        return resultado;
    }

    Conjunto interseccionConjuntos(const Conjunto& otroConjunto) const { // compara dos conjuntos y devuelve los elementos que se repiten en los dos, requerimiento: dos conjuntos
        Conjunto resultado;
        for (int elemento : elementos) {
            if (otroConjunto.pertenece(elemento)) {
                resultado.inserta(elemento);
            }
        }
        return resultado;
    }

    Conjunto diferenciaConjuntos(const Conjunto& otroConjunto) const {// compara dos conjuntos y devuelve los elementos que aparezcan en uno y no en el otro, requerimiento: dos conjuntos
        Conjunto resultado;
        
        for (int elemento : elementos) {
            if (!otroConjunto.pertenece(elemento)) {
                resultado.inserta(elemento);
            }
        }
        return resultado;
    }

    bool incluye(const Conjunto& otroConjunto) const {
        for (int elemento : otroConjunto.elementos) {
            if (!pertenece(elemento)) {
                return false;
            }
        }
        return true;
    }

    bool pertenece(int elemento) const { //devuelve false si el argumento no pertenece al conjunto y true si es al revés, requerimientos: argumento y conjunto.
        for (int i = 0; i < elementos.size(); ++i) {
            if (elementos[i] == elemento) {
                return true;
            }
        }
        return false;
    }

    int tamaño() const { //deevuelve el tamaño del conjunto, requerimiento: conjunto 
        return elementos.size();
    }

    friend ostream& operator<<(ostream& os, const Conjunto& conjunto);
};

ostream& operator<<(ostream& os, const Conjunto& conjunto) {
    os << "{";
    if (conjunto.tamaño() > 0) {
        for (int i = 0; i < conjunto.tamaño() - 1; ++i) {
            os << conjunto.elementos[i] << ", ";
        }
        os << conjunto.elementos[conjunto.tamaño() - 1];
    }
    os << "}";
    return os;
}

int main() {
    
    Conjunto conjunto1;
    conjunto1.inserta(1);
    conjunto1.inserta(2);
    conjunto1.inserta(8);

    Conjunto conjunto2;
    conjunto2.inserta(2);
    conjunto2.inserta(3);
    conjunto2.inserta(4);
    conjunto2.inserta(5);
    conjunto2.elimina(3);
    Conjunto x=conjunto2.diferenciaConjuntos(conjunto1);
    Conjunto y=conjunto1.diferenciaConjuntos(conjunto2);
    cout << "Conjunto 1: " << conjunto1 << endl;
    cout << "Conjunto 2: " << conjunto2 << endl;
    cout << "Diferencia de conjuntos 1 y 2: " << x << endl;
    cout << "Diferencia de conjuntos 2 y 1: " << y << endl;
    
    Conjunto unionConjuntos = conjunto1.unionConjuntos(conjunto2);
    cout << "Unión de conjuntos: " << unionConjuntos << endl;

    Conjunto interseccionConjuntos = conjunto1.interseccionConjuntos(conjunto2);
    cout << "Intersección de conjuntos: "<<interseccionConjuntos<<endl;
    return 0;
}