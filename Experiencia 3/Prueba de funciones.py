import numpy as np

arreglo = np.random.randint(1,101,size=(10))
print(f"Arreglo 1:\n{arreglo}\n")

arreglo2 = np.arange(1,101,10)
print(f"Arreglo 2:\n{arreglo2}\n")
print(f"El promedio del arreglo 2 es {arreglo2.mean()}")

arreglo3 = np.array([1,2,3,4])
print(arreglo3)

lista = [i for i in range(1,11)]
print(lista)
arreglo4 = np.array(lista)
print(arreglo4)

print(arreglo4[:2:])

arreglo = np.arange(4)
arreglo_copia = arreglo[:]
arreglo[0] = 100
print(arreglo)
print(arreglo_copia)

arreglo = np.array([[1,2,3],[4,5,6],[7,8,9]]).reshape(3,3)
print(arreglo)
print(arreglo[2][2])

for n in range(3):
    for m in range(3):
        print(arreglo[n][m])

for n in range (3):
    print(f"Fila número {n+1}: {arreglo[ n , : ]}")

# COLUMNA VERTICAL
for m in range (3):
    print(f"Columna número {m+1}:\n{arreglo[  :  ,m :m+1: ]}")

# COLUMNA HORIZONTAL
for m in range (3):
    print(f"Columna número {m+1}:\n{arreglo[  :  , m ]}")

print(arreglo.size)