from random import randint

n=int(input("numero de elementos q quieres q tenga la lista: "))
list=[]
for i in range(n):
    a=randint(1,100)
    list.append(a)


print(list)
listaa=[]
for i in range(n):
    cont=0
    for j in range(n):
        if list[i]==list[j]:
            cont+=1
    if cont>=2 and list[i] not in listaa:
        listaa.append(list[i])

                
print(listaa)
"""
La complejidad de esta funcion es de orden 𝑶(n) poruqe recorre una vez la lista
"""