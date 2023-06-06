import numpy as np
import random

matriz1 = np.random.randint(1,101,size=(3,3)).reshape(3,3)
print(f"Matriz 1:\n{matriz1}")
matriz2 = np.random.randint(1,101,size=(3,3)).reshape(3,3)
print(f"Matriz 2:\n{matriz2}")
print(f"La suma de ambas matrices es:\n{(matriz1+matriz2).reshape(3,3)}")