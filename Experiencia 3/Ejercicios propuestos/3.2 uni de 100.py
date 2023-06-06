import numpy as np

arregloA = np.random.randint(1,501,size=(100))
print(arregloA)
for x in range(100):
    if (x%2) == 0:
        print(arregloA[x])
mayor = arregloA[0]
for x in range(100):
    if arregloA[x] > mayor:
        mayor = arregloA[x]
        indice = x
print(f"El elemento mayor del arreglo es {arregloA.max()} y su índice de posición es {indice}. El elemento menor es {arregloA.min()}.")

arregloB = arregloA[:].copy()
print(arregloB)
multiplicado = arregloB*3
print(multiplicado)
print(f"La suma de los elementos del segundo arreglo es {multiplicado.sum()} y el promedio de estos elementos es {multiplicado.mean()}.")