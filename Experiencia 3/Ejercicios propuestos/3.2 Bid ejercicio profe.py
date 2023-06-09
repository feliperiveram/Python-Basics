import numpy as np

arreglo = np.arange(1,101).reshape((10,10))

#Mostrar valores 50 - 99 - 15 - 30 
#Mostrar todos los valores de la fila 5
#Mostrar 3 valores de fila 7 usando Slice (misma logica del bidimensional)

for y in range(10):
    for x in range(10):
        if (arreglo[y][x]) == (50):
            print(arreglo[y][x])
        if (arreglo[y][x]) == (99):
            print(arreglo[y][x])
        if (arreglo[y][x]) == (15):
            print(arreglo[y][x])
        if (arreglo[y][x]) == (30):
            print(arreglo[y][x])

print(arreglo)
print(arreglo[4:5:,::])

print(arreglo)
print(arreglo[6:7:,:3:])