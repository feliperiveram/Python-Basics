import numpy as np

arreglo_1 = np.random.randint(1,20,size=(3,3))
arreglo_2 = np.random.randint(1,20,size=(3,3))
print(f"Matriz 1:\n{arreglo_1}")
print(f"\nMatriz 2:\n{arreglo_2}")
print(f"\nMatriz 1 * Matriz 2:\n{arreglo_1*arreglo_2}")