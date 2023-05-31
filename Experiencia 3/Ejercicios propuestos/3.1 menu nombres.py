menu = 0
lista = []
while menu != 2:
    print("1.- AGREGAR NOMBRE\n2.- SALIR Y ELIMINAR EL NOMBRE CON MENOS CARACTERES")
    menu = int(input("Ingrese su opción: "))
    if menu == 1:
        nombre = input("Ingrese el nombre: ")
        lista.append(nombre)
    else:
        i = 0
        menor = lista[0]
        while i <= (len(lista)-2):
            if len(lista[i]) > len(lista[i+1]):
                menor = lista[i+1]
            i += 1
        print(f"El nombre con menos caracteres es {menor} y será eliminado.")
        lista.remove(menor)
        print(f"La nueva lista es {lista}")