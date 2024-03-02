#include "Class_Hora.hpp"
using namespace std;
int main() {
    try {
        Hora hora(12, 30, 45);
        std::cout << hora.toString() << std::endl;
    }
    catch (const std::invalid_argument& e) {
        std::cerr << e.what() << std::endl;
    }

    return 0;
}