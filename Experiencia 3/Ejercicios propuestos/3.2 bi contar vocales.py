import numpy as np
import string

abecedario = list(string.ascii_lowercase)
vocales = "aeiou"
arreglo = np.random.choice(abecedario,size=(4,4))
print(f"El arreglo creado es el siguiente:\n\n{arreglo}")
suma_vocales = 0
lista_vocales = []
for x in range(4):
    for y in range(4):
        if (arreglo[x][y]) in vocales:
            suma_vocales += 1
            lista_vocales.append(arreglo[x][y])
if suma_vocales != 0:
    print(f"\nEn tal arreglo hay {suma_vocales} vocal(es), la(s) cual(es) es(son): {lista_vocales}.")