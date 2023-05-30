'''calculadora de descuentos'''
menu = 0
while menu != 2:
    print("Ingrese lo que desea realizar:\n1.- REALIZAR UN DESCUENTO\n2.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>2 or menu<1:
                menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    if menu == 1:
        num = input("Ingrese el valor al que desea realizarle un descuento: ")
        while type(num) == str:
            try:
                num = float(num)
                if num == 0:
                    num = input("Valor no puede ser 0. Ingrese nuevamente su número: ")
            except ValueError:
                num = input("Valor ingresado no es válido. Ingrese nuevamente su número: ")
        descuento = input("Ingrese el valor del descuento que desea realizar: ")
        while type(descuento) == str:
            try:
                descuento = float(descuento)
                if descuento == 0:
                    descuento = input("Valor no puede ser 0. Ingrese nuevamente su número: ")
            except ValueError:
                descuento = input("Valor ingresado no es válido. Ingrese nuevamente su número: ")
        descuentoconv = descuento/100
        descontado = num-descuentoconv*num
        print(f"{num} menos el {descuento}% es {descontado}.")
    else:
        print("¡Gracias por usar el programa!")