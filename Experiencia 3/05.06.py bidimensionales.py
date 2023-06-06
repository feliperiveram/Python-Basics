import numpy as np

lista = [[1,2,3],[4,5,6],[7,8,9]]
arreglo = np.array(lista)
print(arreglo)

#nombre_arreglo[vertical][horizontal]
print(arreglo[1][1])
print(arreglo[-3][-3])

arr = np.arange(1,101).reshape(10,10)
print(arr)

#mostrar todos los valores de la matriz
for x in range(10):
    for y in range(10):
        print(arr[x][y])

for y in range(10):
    for x in range(10):
        if (arr[y][x]) == 55:
            print(arr[y][x])

print(arreglo.ndim)

#slice -> (nombre_arreglo[::,::])

print(arr)
print(arr[3:6:,:5:])