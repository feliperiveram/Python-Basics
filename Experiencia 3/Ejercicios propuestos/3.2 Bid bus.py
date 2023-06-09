import numpy as np

asientos = np.arange(1,41).reshape(10,4)
primera_columna = asientos[::,:2:]
segunda_columna = asientos[::,2:4:]
pasillo = np.zeros((10,2))
bus = np.concatenate((primera_columna,pasillo),axis=1)
bus = np.concatenate((bus,segunda_columna),axis=1)
print ("Los '0.' representan el pasillo del bus:\n")
print (bus)

# OTRA INTERPRETACIÓN DEL EJERCICIO
asientos = np.arange(1,41).reshape(10,4)
primera_columna = asientos[::,:2:]
segunda_columna = asientos[::,2:4:]
bus = np.concatenate((primera_columna,segunda_columna), axis=1 )
print (f"\n{bus}")