import numpy as np

#Los valores pueden ser igual a 1 o 300
A = np.random.randint(1,300,size=(10))
B = np.random.randint(1,300,size=(10))
print(f"Matriz A: {A}")
print(f"Matriz B: {B}")
print(f"La suma de los elementos del arreglo A es {A.sum()} y la de los elementos del arreglo B es {B.sum()}.")
print(f"La suma de ambos arreglos es la siguiente matriz {A+B}.")
print(f"Tablas de multiplicar de los elementos impares de la matriz B:")
for x in range(10):
    i = 1
    #Filtrar números impares
    if (B[x] % 2) != 0:
        print(f"Tabla de multiplicar del {B[x]}:")
        while i <= 10:
            print(f"{B[x]} * {i} = {B[x]*i}")
            i += 1