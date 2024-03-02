from sympy import principal_branch
from Class_horas import *

x = horas(23, 20,50)
y = horas(2, 50,20)

print('Suma de horas ', x + y)
print('Resta de horas', x - y)
print('La hora {0} es mayor que {1}:  {2}'.format(x,y,x>y))
print('La hora {0} es igual que {1}:  {2}'.format(x,y,x==y))
print('La hora {0} es menor que {1}:  {2}'.format(x,y,x<y))
print('La hora {0} es mayor igual que {1}:  {2}'.format(x,y,x>=y))
print('La hora {0} es menor igual que {1}:  {2}'.format(x,y,x<=y))
print('Hora pasada a am o pm',x.pasarhora())