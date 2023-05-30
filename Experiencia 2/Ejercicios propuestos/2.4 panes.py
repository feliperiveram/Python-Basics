'''En un delivery se venden 4 tipos de pan:
• Amasado $1.500
• Molde $1.000
• Baguette $2.000
• Integral $3.000'''
menu = 1
suma = 0
while menu != 2:
    print("Seleccione su tipo de pan:\n1.- AMASADO ($1.500)\n2.- MOLDE ($1.000)\n3.- BAGUETTE ($2.000)\n4.- INTEGRAL ($3.000)")
    opcion = input("Ingrese su opción: ")
    while type(opcion) == str:
        try:
            opcion = int(opcion)
            if opcion>4 or opcion<1:
                opcion = input("Opción ingresada no es válida, ingrese nuevamente su opción: ")
        except ValueError:
                opcion = input("Opción ingresada no es válida, ingrese nuevamente su opción: ") 
    if opcion==1:
        cantidad = input("Ingrese la cantidad: ")
        while type(cantidad) == str:
            try:
                cantidad = int(cantidad)
                if cantidad<=0:
                    cantidad = input("La cantidad debe ser mayor o igual que 1, ingrese nuevamente su opción: ")
            except ValueError:
                    cantidad = input("Opción ingresada no es válida, ingrese nuevamente su opción: ")
        suma += cantidad*1500
    elif opcion==2:
        cantidad = input("Ingrese la cantidad: ")
        while type(cantidad) == str:
            try:
                cantidad = int(cantidad)
                if cantidad<=0:
                    cantidad = input("La cantidad debe ser mayor o igual que 1, ingrese nuevamente su opción: ")
            except ValueError:
                    cantidad = input("Opción ingresada no es válida, ingrese nuevamente su opción: ")
        suma += cantidad*1000
    elif opcion==3:
        cantidad = input("Ingrese la cantidad: ")
        while type(cantidad) == str:
            try:
                cantidad = int(cantidad)
                if cantidad<=0:
                    cantidad = input("La cantidad debe ser mayor o igual que 1, ingrese nuevamente su opción: ")
            except ValueError:
                    cantidad = input("Opción ingresada no es válida, ingrese nuevamente su opción: ")
        suma += cantidad*2000
    else:
        cantidad = input("Ingrese la cantidad: ")
        while type(cantidad) == str:
            try:
                cantidad = int(cantidad)
                if cantidad<=0:
                    cantidad = input("La cantidad debe ser mayor o igual que 1, ingrese nuevamente su opción: ")
            except ValueError:
                    cantidad = input("Opción ingresada no es válida, ingrese nuevamente su opción: ")
        suma += cantidad*3000
    print("1.- AGREGAR MÁS PRODUCTOS \n2.- IR A PAGAR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>2 or menu<1:
                menu = input("Opción ingresada no es válida, ingrese nuevamente su opción: ")
        except ValueError:
                menu = input("Opción ingresada no es válida, ingrese nuevamente su opción: ")
if suma>5000:
     print(f"El monto total de su compra es de {suma}, por lo que no debe pagar envío.")
else:
     print(f"El monto total de su compra es de {round(suma+0.1*suma)}, ya que debe pagar {round(0.1*suma)} adicionalmente por concepto de envío.")