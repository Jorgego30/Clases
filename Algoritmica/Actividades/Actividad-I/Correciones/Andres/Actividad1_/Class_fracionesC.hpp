#include <iostream>
#include <stdexcept> // Se agrega la librería para excepciones
using namespace std;

int gcd(int m, int n)
{
    while (m % n != 0)
    {
        int oldm = m;
        int oldn = n;

        m = oldn;
        n = oldm % oldn;
    }
    return n;
}

class Fraction
{
public:
    Fraction(int top, int bottom)
    {
        if (bottom == 0)
        {
            throw invalid_argument("El denominador no puede ser cero.");
        }
        num = top;
        den = bottom;
        simplify(); // Se simplifica la fracción al crearla
    }

    Fraction(int top) : num(top), den(1) {}

    Fraction() : num(1), den(1) {}

    Fraction operator+(const Fraction &otherFrac) const
    {
        int newnum = num * otherFrac.den + den * otherFrac.num;
        int newden = den * otherFrac.den;
        return Fraction(newnum, newden);
    }

    bool operator==(const Fraction &otherFrac) const
    {
        return num * otherFrac.den == otherFrac.num * den;
    }

    bool operator>=(const Fraction &otherFrac) const
    {
        return num * otherFrac.den >= otherFrac.num * den;
    }

    bool operator<=(const Fraction &otherFrac) const
    {
        return num * otherFrac.den <= otherFrac.num * den;
    }

    bool operator<(const Fraction &otherFrac) const
    {
        return num * otherFrac.den < otherFrac.num * den;
    }

    bool operator>(const Fraction &otherFrac) const
    {
        return num * otherFrac.den > otherFrac.num * den;
    }

    bool operator!=(const Fraction &otherFrac) const
    {
        return num * otherFrac.den != otherFrac.num * den;
    }

    int getNum() const // Se cambia a getNum
    {
        return num;
    }

    int getDen() const // Se cambia a getDen
    {
        return den;
    }

    friend ostream &operator<<(ostream &stream, const Fraction &fraction);

private:
    int num, den;

    void simplify()
    {
        int common = gcd(num, den);
        num /= common;
        den /= common;
    }
};

ostream &operator<<(ostream &stream, const Fraction &fraction)
{
    stream << fraction.num;
    if (fraction.den != 1)
    {
        stream << "/" << fraction.den;
    }
    return stream;
}
