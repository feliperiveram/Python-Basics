# Definición de funciones
def dcto(valor_compra):
    return(round(valor_compra-valor_compra*0.1)) # Devuelve el monto de la compra con descuento

'''• Espresso $1.500• Capuchino $1.800• Latte $1.600• Moca $1.700'''
#Programa
print("¡Bienvenid@ al sistema de compras automatizado!")
menu = 0
total = 0
espresso = 0
capuchino = 0
latte = 0
moca = 0
while menu != 4:
    print ("¿Qué quieres realizar?\n1.- AÑADIR UN CAFÉ AL CARRITO DE COMPRAS\n2.- BORRAR CARRITO DE COMPRAS\n3.- IR A PAGAR\n4.- SALIR DEL PROGRAMA")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu > 4 or menu < 1:
                menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    if menu == 1:
        print ("¿Qué café deseas agregar?\n1.- ESPRESSO ($1.500)\n2.- CAPUCHINO ($1.800)\n3.- LATTE ($1.600)\n4.- MOCA ($1.700)")
        opcion = input("Ingrese su opción: ")
        while type(opcion) == str:
            try:
                opcion = int(opcion)
                if opcion > 4 or opcion < 1:
                    opcion = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
            except ValueError:
                opcion = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        if opcion == 1:
            cantidad = input("Ingrese la cantidad de CAFÉ ESPRESSO que desea: ")
            while type(cantidad) == str:
                try:
                    cantidad = int(cantidad)
                    if cantidad <= 0:
                        cantidad = input("La cantidad debe ser mayor a 0. Ingrese nuevamente la cantidad de CAFÉ ESPRESSO que desea: ")
                except ValueError:
                    cantidad = input("Valor ingresado no es válido. Ingrese nuevamente la cantidad de CAFÉ ESPRESSO que desea: ")
            total += 1500*cantidad
            espresso += cantidad
        elif opcion == 2:
            cantidad = input("Ingrese la cantidad de CAFÉ CAPUCHINO que desea: ")
            while type(cantidad) == str:
                try:
                    cantidad = int(cantidad)
                    if cantidad <= 0:
                        cantidad = input("La cantidad debe ser mayor a 0. Ingrese nuevamente la cantidad de CAFÉ CAPUCHINO que desea: ")
                except ValueError:
                    cantidad = input("Valor ingresado no es válido. Ingrese nuevamente la cantidad de CAFÉ CAPUCHINO que desea: ")
            total += 1800*cantidad
            capuchino += cantidad
        elif opcion == 3:
            cantidad = input("Ingrese la cantidad de CAFÉ LATTE que desea: ")
            while type(cantidad) == str:
                try:
                    cantidad = int(cantidad)
                    if cantidad <= 0:
                        cantidad = input("La cantidad debe ser mayor a 0. Ingrese nuevamente la cantidad de CAFÉ LATTE que desea: ")
                except ValueError:
                    cantidad = input("Valor ingresado no es válido. Ingrese nuevamente la cantidad de CAFÉ LATTE que desea: ")
            total += 1600*cantidad
            latte += cantidad
        else:
            cantidad = input("Ingrese la cantidad de CAFÉ MOCA que desea: ")
            while type(cantidad) == str:
                try:
                    cantidad = int(cantidad)
                    if cantidad <= 0:
                        cantidad = input("La cantidad debe ser mayor a 0. Ingrese nuevamente la cantidad de CAFÉ MOCA que desea: ")
                except ValueError:
                    cantidad = input("Valor ingresado no es válido. Ingrese nuevamente la cantidad de CAFÉ MOCA que desea: ")
            total += 1700*cantidad
            moca += cantidad
    elif menu == 2:
        total = 0
        espresso = 0
        capuchino = 0
        latte = 0
        moca = 0
    elif menu == 3:
        print("DETALLE DE COMPRA")
        print("________________________________________\n")
        if espresso != 0:
            print(f"{espresso} unidad(es) CAFÉ ESPRESSO = {espresso*1500}")
        if capuchino != 0:
            print(f"{capuchino} unidad(es) CAFÉ CAPUCHINO = {capuchino*1800}")
        if latte != 0:
            print(f"{latte} unidad(es) CAFÉ LATTE = {latte*1600}")
        if moca != 0:
            print(f"{moca} unidad(es) CAFÉ MOCA = {moca*1700}")
        print("________________________________________\n")
        if total >= 3000:
            print("Descuento del 10% aplicado")
            print(f"MONTO A PAGAR = {dcto(total)}")
        else:
            print(f"MONTO A PAGAR = {total}")
        total = 0
        espresso = 0
        capuchino = 0
        latte = 0
        moca = 0
    else:
        print("¡Gracias por haber usado el programa!")