x = range(3)
lista = []
for n in x:
    nombre = input("Ingrese el nombre: ")
    lista.append(nombre)
i = 0
mayor = lista[0]
while i <= (len(lista)-2):
    if len(lista[i]) < len(lista[i+1]):
        mayor = lista[i+1]
    i += 1
print(f"El nombre con más caracteres es {mayor}.")