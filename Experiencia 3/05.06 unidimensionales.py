import numpy as np
lista = [1,2,3,4,5]
arreglo = np.array(lista)
print(arreglo)

#ndim = número de dimensiones
print(arreglo.ndim)

#len = largo del arreglo
print(len(arreglo))

#slice -> nombre_arreglo[desde donde : hasta donde sin tomarlo en cuenta : step]
print(arreglo[1:3:1])
print(arreglo[:3:])

#crear arreglos
lista2 = [i for i in range(1,11)]
arreglo2 = np.array(lista2)
print(arreglo2)

print(np.arange(1,11,2))

#sumar
arreglo += 5
print (arreglo)

#suma de todos los valores
print (arreglo.sum())

#promedio de los valores
print (arreglo.mean())

#potencias
arreglo **= 2
print (arreglo)