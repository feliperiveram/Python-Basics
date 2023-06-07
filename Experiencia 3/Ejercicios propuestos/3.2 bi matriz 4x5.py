import numpy as np

arreglo = np.random.randint(0,100,size=(5,4)).reshape(5,4)
print(f"El arreglo generado es:\n\n{arreglo}")

#COLUMNA (VERTICAL) FILA(HORIZONTAL)
#SUMA ELEMENTOS DE CADA FILA
for y in range(5):
    fila_actual = arreglo[y:y+1:,:4:]
    print(f"La suma de los elementos de la fila {y+1} es {fila_actual.sum()}")

#SUMA ELEMENTOS DE CADA COLUMNA
for x in range(4):
    columna_actual = arreglo[:5:,x:x+1:]
    print(f"La suma de los elementos de la columna {x+1} es {columna_actual.sum()}")

#NOMBRE_ARREGLO[VERTICAL][HORIZONTAL]
suma_diagonal = 0
for n in range(4):
    suma_diagonal += arreglo[n][n]
print(f"La suma de la diagonal principal es {suma_diagonal}")

print("Los elementos impares de la matriz son:\n")
for y in range(5):
    for x in range(4):
        if ((arreglo[y][x])%2) != 0:
            print(arreglo[y][x])