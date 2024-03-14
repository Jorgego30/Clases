"""
---------------------|-------------------------|
Expresiones infijas  |   Expresiones prefijas  |
(A+B)*(C+D)*(E+F)    |   *(+AB)*(+CD)(+EF)*     |
A+((B+C)*(D+E))      |   +A(*(+BC)(+DE))       |
A*B*C*D+E+F          |   *AB*CD++E+F            |
---------------------|-------------------------|
"""