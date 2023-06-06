import numpy as np
arregloA = np.random.randint(1,501,size=(10,10)).reshape(10,10)
print(arregloA)
for y in range(10):
    if (y%2) == 0:
        for x in range(10):
            if (x%2) == 0:
                print(arregloA[y][x])
maximo = arregloA[0][0]
print(maximo)
for y in range(10):
    for x in range(10):
            if (arregloA[y][x]) > maximo:
                 maximo = arregloA[y][x]
                 ejex = y
                 ejey = x

print(f"El elemento mayor del arreglo es {arregloA.max()} y sus indices de posición son arregloA[{ejex}][{ejey}]")