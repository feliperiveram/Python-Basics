'''convertidor de unidades'''
menu = 0
while menu != 3:
    print("1.- CM A M\n2.- M A CM\n3.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>3 or menu<1:
                menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    if menu == 1:
        num = input("Ingrese los centímetros que desea convertir a metros: ")
        while type(num) == str:
            try:
                num = float(num)
            except ValueError:
                num = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        metros = num/100
        print(f"{num} [cm] corresponden a {metros} [m].")
    elif menu == 2:
        num = input("Ingrese los centímetros que desea convertir a metros: ")
        while type(num) == str:
            try:
                num = float(num)
            except ValueError:
                num = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        centimetros = num*100
        print(f"{num} [m] corresponden a {centimetros} [cm].")
    else:
        print("¡Gracias por usar el programa!")