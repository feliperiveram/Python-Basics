import numpy as np
import random

lista = []
for x in range(10):
    num = random.randint(0,1000)
    lista.append(num)

arreglo_1 = np.array(lista)
print(arreglo_1)

print("Los elementos del arreglo son:")
for n in range(10):
    print(arreglo_1[n])

pares = 0
for n in range(10):
    if (arreglo_1[n])%2 == 0:
        pares += 1
print(f"Hay {pares} elementos pares en el arreglo.")

suma_impares = 0
for y in range(10):
    if (arreglo_1[y])%2 == 0:
        suma_impares += arreglo_1[y]
print(f"La suma de elementos impares del arreglo es {suma_impares}.")

#PRIMOS
primos = []
print("Los elementos primos del arreglo son:")
for n in range(10):
    divisores = 0
    i = 1
    while i <= (arreglo_1[n]):
        if ((arreglo_1[n]) != 1) and (((arreglo_1[n])%i) == 0):
            divisores += 1
        i += 1
    if divisores == 2:
        primos.append(arreglo_1[n])
for x in primos:
    print(x)