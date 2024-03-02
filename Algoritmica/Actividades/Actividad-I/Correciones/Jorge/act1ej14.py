import timeit
import random

    
def prueba1():
  myList= [1,3,4,12,12,1,1,0,9]
  for item in myList:
    del myList[random.randrange(len(myList))]
    break


def prueba2():
  a_dictionary = {"one": 1, "two" : 2, "three": 3}

  desired_key = random.choice
  for key in a_dictionary.keys():
    if key == desired_key:
      del a_dictionary[key]
      break




    
t1 = timeit.Timer("prueba1()", "from __main__ import prueba1")
print("Tiempo requerido para eliminar elementos de la lista: ",t1.timeit(number=1000), "segundos")
t2 = timeit.Timer("prueba2()", "from __main__ import prueba2")
print("Tiempo requerido para eliminar elementos del diccionario: ",t2.timeit(number=1000), "segundos")
