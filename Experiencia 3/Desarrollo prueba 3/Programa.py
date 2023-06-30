import Funciones as fx

menu = 0
print("¡Bienvenid@!")
while menu != 4:
    print("¿Qué deseas realizar?:\n1.- GRABAR\n2.- BUSCAR\n3.- IMPRIMIR CERTIFICADOS\n4.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu > 4 or menu < 1:
                menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    if menu == 1:
        fx.grabar()
    elif menu == 2:
        fx.buscar()
    elif menu == 3:
        fx.imprimir_certificado()
    else:
        print("¡Gracias por haber usado el programa!\n\nPowered by Felipe Rivera\nVersion 2.0")