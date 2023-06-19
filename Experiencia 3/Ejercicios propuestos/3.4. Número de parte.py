# Definición de funciones
def buscar(numero_parte):
    i = 0
    posicion = -1
    while i <= (len(lista_numero_parte)-1):
        if lista_numero_parte[i] == numero_parte:
            posicion = i
        i += 1
    if posicion == -1:
        print(f"Anteriormente no se ha guardado ningún producto cuyo número de parte sea {numero_parte}.")
    else:
        if (lista_precio_producto[posicion]) >= 500:
            print(f"Nombre del producto: {lista_nombre_producto[posicion]}.")
            print(f"Número de parte del producto: {numero_parte}.")
            print(f"Precio: ${lista_precio_producto[posicion]}.")
        else:
            print("Producto sin stock.")

# Programa
print ("¡Bienvenid@!")
menu = 0
lista_numero_parte = []
lista_nombre_producto = []
lista_precio_producto = []
while menu != 4:
    print ("¿Qué deseas realizar?:\n1.- GRABAR\n2.- BUSCAR\n3.- IMPRIMIR\n4.- SALIR DEL PROGRAMA")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu > 4 or menu < 1:
                menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    # Opción grabar
    if menu == 1:
        # Ingresar número de parte
        numero_parte = input("Ingrese el número de parte: ")
        numero_parte.upper()
        while numero_parte.upper() in lista_numero_parte:
            print(f"El número de parte {numero_parte} ya ha sido grabado anteriormente.")
            numero_parte = input("Ingrese nuevamente el número de parte: ")
            numero_parte = numero_parte.upper()
        lista_numero_parte.append(numero_parte.upper())
        # Ingresar nombre del producto
        nombre_producto = input(f"Ingrese el nombre del número de parte {numero_parte}: ")
        while len(nombre_producto) <= 6:
            print("El nombre del producto debe tener como mínimo 6 carácteres.")
            nombre_producto = input("Ingrese nuevamente el nombre del producto: ")
        lista_nombre_producto.append(nombre_producto)
        # Ingresar el precio del producto
        precio_producto = input("Ingrese el precio del producto: ")
        while type(precio_producto) == str:
            try:
                precio_producto = int(precio_producto)
                if precio_producto <= 0:
                    precio_producto = input("El precio del producto debe ser mayor que $0. Ingrese el precio del producto: ")
            except ValueError:
                precio_producto = input("Valor ingresado no es válido. Ingrese el precio del producto: ")
        lista_precio_producto.append(precio_producto)
        print("¡El grabado ha sido realizado correctamente!")
    # Opción buscar
    elif menu == 2:
        numero_parte = input ("Ingrese el número de parte del producto del que desea conocer su información: ")
        numero_parte = numero_parte.upper()
        buscar(numero_parte)
    elif menu == 3:
        print("Detalle de todos los productos almacenados:\n")
        print("____________________________________________\n")
        i = 0
        while i <= (len(lista_numero_parte)-1):
            print(f"Nombre del producto: {lista_nombre_producto[i]}.")
            print(f"Número de parte del producto: {lista_numero_parte[i]}.")
            print(f"Precio: ${lista_precio_producto[i]}.\n")
            i += 1
    else:
        print("¡Gracias por haber usado el programa!\nFelipe Rivera Versión 1.0")