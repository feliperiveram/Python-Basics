# Importar funciones
import numpy as np
import Funciones as fx # Para luego llamarla en el programa sería fx.asientos_disponibles()

# Antes del programa
asientos = np.arange(1,43).reshape(7,6)
asientos = asientos.astype(str)
asientos_ocupados = asientos[:].copy()

lista_nombre = []
lista_rut = []
lista_fono = []
lista_asiento_comprado = []

# Programa
print("¡Bienvenid@!")
menu = 0
while menu != 5:
    print("¿Qué quieres hacer?\n1.- VER ASIENTOS DISPONIBLES\n2.- COMPRAR ASIENTO\n3.- ANULAR VUELO\n4.- MODIFICAR DATOS DE PASAJERO\n5.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu > 5 or menu < 1:
                menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    if menu == 1:
        print("Los asientos que no están marcados con 'X' son los que están disponibles:\n")
        fx.asientos_disponibles(asientos_ocupados)
    # Comprar un asiento
    elif menu == 2:
        asiento = input(f"\n{fx.asientos_disponibles(asientos_ocupados)}\nEscriba el número del asiento que desea reservar: ")
        while (asiento not in asientos_ocupados) or (asiento == 'X'):
            asiento = input("El asiento que ingresó no se encuentra disponible. Ingrese otro asiento: ")
        if asiento in asientos_ocupados:
            fx.reservar(asiento, asientos_ocupados,lista_nombre,lista_rut,lista_fono,lista_asiento_comprado)
    # Anular
    elif menu == 3:
        asiento = input("Ingrese el número de asiento que desea anular: ")
        while type(asiento) == str:
            try:
                asiento = int(asiento)
                if asiento > 42 or asiento < 1:
                    asiento = input("Valor ingresado no es válido. Ingrese nuevamente su número de asiento: ")
            except ValueError:
                asiento = input("Valor ingresado no es válido. Ingrese nuevamente su número de asiento: ")
        asiento = str(asiento)
        fx.anular(asiento,lista_asiento_comprado,asientos,asientos_ocupados,lista_nombre,lista_rut,lista_fono)
    # Modificar datos de pasajero
    elif menu == 4:
        asiento = input("Ingrese su número de asiento: ")
        while type(asiento) == str:
            try:
                asiento = int(asiento)
                if asiento > 42 or asiento < 1:
                    asiento = input("Valor ingresado no es válido. Ingrese nuevamente su número de asiento: ")
            except ValueError:
                asiento = input("Valor ingresado no es válido. Ingrese nuevamente su número de asiento: ")
        asiento = str(asiento)
        rut = input("Ingrese su RUT: ")
        while (asiento not in lista_asiento_comprado) or (rut not in lista_rut):
            print("Las credenciales no son correctas, por lo que no puede modificar sus datos. Inténtelo nuevamente.")
            asiento = input("Ingrese su número de asiento: ")
            while type(asiento) == str:
                try:
                    asiento = int(asiento)
                    if asiento > 42 or asiento < 1:
                        asiento = input("Valor ingresado no es válido. Ingrese nuevamente su número de asiento: ")
                except ValueError:
                    asiento = input("Valor ingresado no es válido. Ingrese nuevamente su número de asiento: ")
            asiento = str(asiento)
            rut = input("Ingrese su RUT: ")
        print("¿Qué desea modificar?:\n1.- NOMBRE\n2.- FONO")
        opcion = input("Ingrese su opción: ")
        while type(opcion) == str:
            try:
                opcion = int(opcion)
                if opcion > 2 or opcion < 1:
                    opcion = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
            except ValueError:
                opcion = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        # Modificar nombre
        if opcion == 1:
            nombre = input("Ingrese el nuevo nombre: ")
            i = 0
            while i <= (len(lista_rut)-1):
                if lista_rut[i] == rut:
                    posicion_rut = i
                i += 1
            i = 0
            while i <= (len(lista_asiento_comprado)-1):
                if lista_asiento_comprado[i] == asiento:
                    posicion_asiento = i
                i += 1
            if posicion_asiento == posicion_rut:
                lista_nombre[posicion_rut] = nombre
            # Actualizar nombre en cada compra donde haya usado el mismo RUT
            i = 0
            while i <= (len(lista_rut)-1):
                if (lista_rut[i] == rut) and (lista_nombre[i] != nombre):
                    lista_nombre[i] = nombre
                    i = 0
                i += 1
        # Modificar fono
        else:
            fono = input("Ingrese el nuevo fono: ")
            i = 0
            while i <= (len(lista_rut)-1):
                if lista_rut[i] == rut:
                    posicion_rut = i
                i += 1
            i = 0
            while i <= (len(lista_asiento_comprado)-1):
                if lista_asiento_comprado[i] == asiento:
                    posicion_asiento = i
                i += 1
            if posicion_asiento == posicion_rut:
                lista_fono[posicion_rut] = fono
            # Actualizar nombre en cada compra donde haya usado el mismo RUT
            i = 0
            while i <= (len(lista_rut)-1):
                if (lista_rut[i] == rut) and (lista_fono[i] != fono):
                    lista_fono[i] = fono
                    i = 0
                i += 1
    else:
        print("¡Gracias por haber usado el programa!")