#include <iostream>
using namespace std;

int gcd(int m, int n){
    while (m % n != 0){
        int oldm = m;
        int oldn = n;

        m = oldn;
        n = oldm % oldn;
    }
    return n;
}

class Fraction{
    public:

        Fraction(float top, float bottom){
            try{
                if (top-int(top)==0 && bottom-int(bottom)==0){
                    num = top;
                    if (bottom!=0){
                        den = bottom;
                    }else {
                        throw 1;
                    }
                }else {
                    throw 2;
                }
            }catch(int x){
                if (x==2){
                    cout << "El numerador y el denominador deben ser enteros" << endl;
                    exit(-1);
                }
                else if (x==1)
                    cout << "El denominador no puede ser 0" << endl;
                    exit(-1);
            }
        }

        Fraction(float top){
            try{
                if(top-int(top)==0){
                    num = top;
                }else {
                    throw 1;
                }
            }catch(...){
                cout << "El numerador debe ser enteros" << endl;
                exit(-1);
            }

            den = 1;
        }

        Fraction(){
            num = 1;
            den = 1;
        }

        int getNum(){
            return num;
        }

        int getDen(){
            return den;
        }

        Fraction operator+(Fraction otherFrac){
            int newnum = num * otherFrac.den + den * otherFrac.num;
            int newden = den * otherFrac.den;
            int common = gcd(newnum, newden);

            return Fraction(newnum / common, newden / common);
        }

        Fraction operator-(Fraction otherFrac){
            int newnum = num * otherFrac.den - den * otherFrac.num;
            int newden = den * otherFrac.den;
            int common = gcd(newnum, newden);

            return Fraction(newnum / common, newden / common);
        }

        Fraction operator*(Fraction otherFrac){
            int newnum = num * otherFrac.num;
            int newden = den * otherFrac.den;
            int common = gcd(newnum, newden);

            return Fraction(newnum / common, newden / common);
        }

        Fraction operator/(Fraction otherFrac){
            int newnum = num * otherFrac.den;
            int newden = den * otherFrac.num;
            int common = gcd(newnum, newden);

            return Fraction(newnum / common, newden / common);
        }

        bool operator==(Fraction &otherFrac){
            int firstnum = num * otherFrac.den;
            int secondnum = otherFrac.num * den;

            return firstnum == secondnum;
        }

        bool operator<(Fraction &otherFrac){
            int firstnum = num * otherFrac.den;
            int secondnum = otherFrac.num * den;

            return firstnum < secondnum;
        }

        bool operator<=(Fraction &otherFrac){
            int firstnum = num * otherFrac.den;
            int secondnum = otherFrac.num * den;

            return firstnum <= secondnum;
        }

        bool operator>(Fraction &otherFrac){
            int firstnum = num * otherFrac.den;
            int secondnum = otherFrac.num * den;

            return firstnum > secondnum;
        }

        bool operator>=(Fraction &otherFrac){
            int firstnum = num * otherFrac.den;
            int secondnum = otherFrac.num * den;

            return firstnum >= secondnum;
        }

        bool operator!=(Fraction &otherFrac){
            int firstnum = num * otherFrac.den;
            int secondnum = otherFrac.num * den;

            return firstnum != secondnum;
        }

        friend ostream &operator<<(ostream &stream, const Fraction &fraction);

    private:
        int num, den;
};

ostream &operator<<(ostream &stream, const Fraction &fraction){

    stream << fraction.num << "/" << fraction.den;

    return stream;
}
