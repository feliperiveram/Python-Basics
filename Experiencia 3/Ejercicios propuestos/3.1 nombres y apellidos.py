x = range(3)
nombres = []
apellidos = []
for n in x:
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    nombres.append(nombre)
    apellidos.append(apellido)
print(nombres)
print(apellidos)
i = 0
while i <= (len(nombres)-1):
    print(f"{nombres[i]}  {apellidos[i]}")
    i += 1