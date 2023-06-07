import numpy as np

arreglo = np.arange(1,41).reshape(10,4)
print(arreglo)
lado_1 = arreglo[:11:,:2:]
lado_2 = arreglo[:11:,2:4:]

unos = np.full((10,1),0)
for x in range(10):
    unos[x][0]
print(unos)