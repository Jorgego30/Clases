from random import randint


n=int(input("numero de elementos q quieres q tenga la lista: "))
list=[]
for i in range(n+1):
    a=randint(1,100)
    list.append(a)

suma=0
print(list)
for i in list:
    suma+=i
print(suma)
"""
La complejidad de esta funcion es de orden 𝑶(n) poruqe recorre una vez la lista
"""