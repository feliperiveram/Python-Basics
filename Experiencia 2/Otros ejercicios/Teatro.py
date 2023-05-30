'''realizar venta de entradas
vip 25000
platea 15000
tribuna 10000
galeria 5000
estudiantes 20% de dcto
socio teatro 30%'''
vip = 0
pla = 0
tri = 0
gal = 0
est = 0
soc = 0
persona = 0
totalventas = 0
menu = 0
while menu!= 2:
    total = 0
    persona += 1
    print("Bienvenid@ al Teatro Disidencias. ¿Qué tipo de entrada desea?:\n1.- VIP\n2.- PLATEA\n3.- TRIBUNA\n4.- GALERÍA")
    op = input("Ingrese su tipo de entrada: ")
    while type(op) == str:
        try:
            op = int(op)
            if op>4 or op<1:
                op = input("La opción ingresada no es válida. Ingrese nuevamente su opción: ")
        except ValueError:
            op = input("Valor ingresado no es válido. Ingrese nuevamente su opción: ")
    #vip 25000
    if op == 1:
        cant = input("Ingrese la cantidad deseada de entradas tipo VIP: ")
        while type(cant) == str:
            try:
                cant = int(cant)
                if cant<1:
                    cant = input("La cantidad de entradas debe ser mayor a 0. Ingrese nuevamente la cantidad de entradas tipo VIP que desea: ")
            except ValueError:
                cant = input("Valor ingresado no es válido. Ingrese nuevamente la cantidad de entradas tipo VIP que desea: ")
        vip += cant
        print("¿Es estudiante o socio del teatro?:\n1.- ESTUDIANTE\n2.- SOCIO\n3.- NINGUNA DE LAS ANTERIORES")
        usuario = input("Ingrese la opción que corresponda: ")
        while type(usuario) == str:
            try:
                usuario = int(usuario)
                if usuario<1 or usuario>3:
                    usuario = input("Opción ingresada no es válida. Vuelva a intentarlo: ")
            except ValueError:
                usuario = input("Valor ingresado no es válido. Vuelva a intentarlo: ")
        if usuario == 1:
            est += 1
            total = round(0.8*(cant*25000))
        elif usuario == 2:
            soc += 1
            total = round(0.7*(cant*25000))
        else:
            total = cant*25000
        print(f"Por {cant} entrada(s) tipo VIP, debe pagar: ${total}. ¡Gracias por su compra, que disfrute su función!")
        totalventas += total
    #platea 15000
    elif op == 2:
        cant = input("Ingrese la cantidad deseada de entradas tipo PLATEA: ")
        while type(cant) == str:
            try:
                cant = int(cant)
                if cant<1:
                    cant = input("La cantidad de entradas debe ser mayor a 0. Ingrese nuevamente la cantidad de entradas tipo PLATEA que desea: ")
            except ValueError:
                cant = input("Valor ingresado no es válido. Ingrese nuevamente la cantidad de entradas tipo PLATEA que desea: ")
        pla += cant
        print("¿Es estudiante o socio del teatro?:\n1.- ESTUDIANTE\n2.- SOCIO\n3.- NINGUNA DE LAS ANTERIORES")
        usuario = input("Ingrese la opción que corresponda: ")
        while type(usuario) == str:
            try:
                usuario = int(usuario)
                if usuario<1 or usuario>3:
                    usuario = input("Opción ingresada no es válida. Vuelva a intentarlo: ")
            except ValueError:
                usuario = input("Valor ingresado no es válido. Vuelva a intentarlo: ")
        if usuario == 1:
            est += 1
            total = round(0.8*(cant*15000))
        elif usuario == 2:
            soc += 1
            total = round(0.7*(cant*15000))
        else:
            total = cant*15000
        print(f"Por {cant} entrada(s) tipo PLATEA, debe pagar: ${total}. ¡Gracias por su compra, que disfrute su función!")
        totalventas += total
    #tribuna 10000
    elif op == 3:
        cant = input("Ingrese la cantidad deseada de entradas tipo TRIBUNA: ")
        while type(cant) == str:
            try:
                cant = int(cant)
                if cant<1:
                    cant = input("La cantidad de entradas debe ser mayor a 0. Ingrese nuevamente la cantidad de entradas tipo TRIBUNA que desea: ")
            except ValueError:
                cant = input("Valor ingresado no es válido. Ingrese nuevamente la cantidad de entradas tipo TRIBUNA que desea: ")
        tri += cant
        print("¿Es estudiante o socio del teatro?:\n1.- ESTUDIANTE\n2.- SOCIO\n3.- NINGUNA DE LAS ANTERIORES")
        usuario = input("Ingrese la opción que corresponda: ")
        while type(usuario) == str:
            try:
                usuario = int(usuario)
                if usuario<1 or usuario>3:
                    usuario = input("Opción ingresada no es válida. Vuelva a intentarlo: ")
            except ValueError:
                usuario = input("Valor ingresado no es válido. Vuelva a intentarlo: ")
        if usuario == 1:
            est += 1
            total = round(0.8*(cant*10000))
        elif usuario == 2:
            soc += 1
            total = round(0.7*(cant*10000))
        else:
            total = cant*10000
        print(f"Por {cant} entrada(s) tipo TRIBUNA, debe pagar: ${total}. ¡Gracias por su compra, que disfrute su función!")
        totalventas += total
    #galeria 5000
    else:
        cant = input("Ingrese la cantidad deseada de entradas tipo GALERÍA: ")
        while type(cant) == str:
            try:
                cant = int(cant)
                if cant<1:
                    cant = input("La cantidad de entradas debe ser mayor a 0. Ingrese nuevamente la cantidad de entradas tipo GALERÍA que desea: ")
            except ValueError:
                cant = input("Valor ingresado no es válido. Ingrese nuevamente la cantidad de entradas tipo GALERÍA que desea: ")
        gal += cant
        print("¿Es estudiante o socio del teatro?:\n1.- ESTUDIANTE\n2.- SOCIO\n3.- NINGUNA DE LAS ANTERIORES")
        usuario = input("Ingrese la opción que corresponda: ")
        while type(usuario) == str:
            try:
                usuario = int(usuario)
                if usuario<1 or usuario>3:
                    usuario = input("Opción ingresada no es válida. Vuelva a intentarlo: ")
            except ValueError:
                usuario = input("Valor ingresado no es válido. Vuelva a intentarlo: ")
        if usuario == 1:
            est += 1
            total = round(0.8*(cant*5000))
        elif usuario == 2:
            soc += 1
            total = round(0.7*(cant*5000))
        else:
            total = cant*5000
        print(f"Por {cant} entrada(s) tipo GALERÍA, debe pagar: ${total}. ¡Gracias por su compra, que disfrute su función!")
        totalventas += total
    print("1.- VENDER OTRA ENTRADA\n2.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu<1 or menu>2:
                menu = input("Opción ingresada no es válida. Vuelva a intentarlo: ")
        except ValueError:
            menu = input("Valor ingresado no es válido. Vuelva a intentarlo: ")
print(f"REPORTE DE VENTAS\n-------------------------------\nEn total se vendieron {vip+tri+gal+pla} entradas, de las cuales {vip} fueron de tipo VIP, {tri} fueron de tipo TRIBUNA, {gal} fueron de tipo GALERÍA, {pla} fueron de tipo PLATEA.")
print(f"{persona} personas compraron entradas, de las cuales {est} fueron estudiantes y {soc} fueron socios.")
print(f"En total se recaudaron ${totalventas}.")