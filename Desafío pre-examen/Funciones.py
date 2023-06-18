import numpy as np

# Función imprimir asientos disponibles (vista usuario)
def asientos_disponibles(nombre_lista_asientos_ocupados):
    np.savetxt('arreglo.txt',nombre_lista_asientos_ocupados, fmt='%-2s', delimiter='  ')
    with open('arreglo.txt', 'r') as file:
        contenido = file.read()
        print(contenido)

# Función pago asiento
def reservar(asiento, asientos_ocupados,lista_nombre,lista_rut,lista_fono,lista_asiento_comprado):
    for m in range(7):
        for n in range(6):
            if asiento == asientos_ocupados[m][n]:
                if int(asientos_ocupados[m][n]) >= 31:
                    print("El valor del asiento es de $240.000. ¿Lo acepta?\n1.- SÍ\n2.- NO")
                    opcion = input("Ingrese su opción: ")
                    while type(opcion) == str:
                        try:
                            opcion = int(opcion)
                            if opcion > 2 or opcion < 1:
                                opcion = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
                        except ValueError:
                            opcion = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
                    if opcion == 1:
                        nombre = input("Ingrese su nombre: ")
                        rut = input("Ingrese su rut: ")
                        fono = input("Ingrese su número de teléfono: ")
                        print ("Banco:\n1.- BANCO DUOC UC\n2.- OTRO BANCO")
                        banco = input("Ingrese su opción: ")
                        while type(banco) == str:
                            try:
                                banco = int(banco)
                                if banco > 2 or banco < 1:
                                    banco = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
                            except ValueError:
                                banco = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
                        if banco == 1:
                            print(f"Debe pagar ${round(240000-240000*0.15)} por su asiento por el convenio de bancos.")
                        else:
                            print("Debe pagar $240.000 por su asiento ya que su banco no tiene convenios con esta aerolínea.")
                        lista_nombre.append(nombre.upper())
                        lista_rut.append(rut.upper())
                        lista_fono.append(fono)
                        lista_asiento_comprado.append(asiento)
                        asientos_ocupados[m][n] = 'X'
                else:
                    print("El valor del asiento es de $78.900. ¿Lo acepta?\n1.- SÍ\n2.- NO")
                    opcion = input("Ingrese su opción: ")
                    while type(opcion) == str:
                        try:
                            opcion = int(opcion)
                            if opcion > 2 or opcion < 1:
                                opcion = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
                        except ValueError:
                            opcion = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
                    if opcion == 1:
                        nombre = input("Ingrese su nombre: ")
                        rut = input("Ingrese su rut: ")
                        fono = input("Ingrese su número de teléfono: ")
                        print ("Banco:\n1.- BANCO DUOC UC\n2.- OTRO BANCO")
                        banco = input("Ingrese su opción: ")
                        while type(banco) == str:
                            try:
                                banco = int(banco)
                                if banco > 2 or banco < 1:
                                    banco = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
                            except ValueError:
                                banco = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
                        if banco == 1:
                            print(f"Debe pagar ${round(78900-78900*0.15)} por su asiento por el convenio de bancos.")
                        else:
                            print("Debe pagar $78.900 por su asiento ya que su banco no tiene convenios con esta aerolínea.")
                        lista_nombre.append(nombre.upper())
                        lista_rut.append(rut.upper())
                        lista_fono.append(fono)
                        lista_asiento_comprado.append(asiento)
                        asientos_ocupados[m][n] = 'X'

# Función anular pasaje
def anular(asiento,lista_asiento_comprado,asientos,asientos_ocupados,lista_nombre,lista_rut,lista_fono):
    if asiento in lista_asiento_comprado:
        i = 0
        while i <= (len(lista_asiento_comprado)-1):
            if asiento == lista_asiento_comprado[i]:
                posicion = i
            i += 1
        for m in range(7):
            for n in range(6):
                if asientos[m][n] == lista_asiento_comprado[posicion]:
                    asientos_ocupados[m][n] = asientos[m][n]
        lista_asiento_comprado.pop(posicion)
        lista_fono.pop(posicion)
        lista_nombre.pop(posicion)
        lista_rut.pop(posicion)
        print("Se ha anulado la reserva de forma correcta.")
    else:
        print("Ese asiento no ha sido comprado")

# Función modificar datos