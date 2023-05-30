'''• Agua → $ 600• Azúcar→ $1200• Aceite → $1500• Arroz → $1250• Fideos → $ 790• Bebida→ $1780• Chocolate → $2500• Pan molde → $1340
'''
menu=1
while menu != 2:
    i=1
    suma=0
    while i<=8:
        if i == 1:
            cant = int(input("Elija las unidades de [Agua] que lleva: "))
            while cant<0:
                cant = int(input("La cantidad no puede ser negativa. Elija nuevamente las unidades de [Agua] que lleva: "))
            suma=suma+cant*600
        elif i == 2:
            cant = int(input("Elija las unidades de [Azúcar] que lleva: "))
            while cant<0:
                cant = int(input("La cantidad no puede ser negativa. Elija nuevamente las unidades de [Azúcar] que lleva: "))
            suma=suma+cant*1200
        elif i == 3:
            cant = int(input("Elija las unidades de [Aceite] que lleva: "))
            while cant<0:
                cant = int(input("La cantidad no puede ser negativa. Elija nuevamente las unidades de [Aceite] que lleva: "))
            suma=suma+cant*1500
        elif i == 4:
            cant = int(input("Elija las unidades de [Arroz] que lleva: "))
            while cant<0:
                cant = int(input("La cantidad no puede ser negativa. Elija nuevamente las unidades de [Arroz] que lleva: "))
            suma=suma+cant*1250
        elif i == 5:
            cant = int(input("Elija las unidades de [Fideos] que lleva: "))
            while cant<0:
                cant = int(input("La cantidad no puede ser negativa. Elija nuevamente las unidades de [Fideos] que lleva: "))
            suma=suma+cant*790
        elif i == 6:
            cant = int(input("Elija las unidades de [Bebida] que lleva: "))
            while cant<0:
                cant = int(input("La cantidad no puede ser negativa. Elija nuevamente las unidades de [Bebida] que lleva: "))
            suma=suma+cant*1780
        elif i == 7:
            cant = int(input("Elija las unidades de [Chocolate] que lleva: "))
            while cant<0:
                cant = int(input("La cantidad no puede ser negativa. Elija nuevamente las unidades de [Chocolate] que lleva: "))
            suma=suma+cant*2500
        else:
            cant = int(input("Elija las unidades de [Pan de Molde] que lleva: "))
            while cant<0:
                cant = int(input("La cantidad no puede ser negativa. Elija nuevamente las unidades de [Pan de Molde] que lleva: "))
            suma=suma+cant*1340
        i=i+1
    print("¿Es cliente preferente? \n1.- SÍ \n2.- NO")
    preferente = int(input("Elija su opción: "))
    while preferente >2 or preferente<1:
        preferente = int(input("Opción ingresada no es válida. Introduzca nuevamente su opción: "))
    if preferente==1:
        total = round(suma-0.25*suma)
        print(f"Debe pagar ${round(total)} por su compra.")
    else:
        total = suma
        print(f"Debe pagar ${total} por su compra.")
    pago = int(input("Deme los billetes: "))
    while pago<=0:
        pago = int(input("Ingrese nuevamente sus billetes: "))
    if pago>=total:
        vuelto=pago-total
        print(f"Su vuelto es de {vuelto}, gracias por comprar aquí.")
    else:
        print("Con esto no alcanza para pagar. ¡Al Jabberwocky!")
    print("1.- INGRESAR OTRA COMPRA \n2.- SALIR")
    menu = int(input("Elija su opción: "))
    while menu >2 or menu<1:
        menu = int(input("Opción ingresada no es válida. Introduzca nuevamente su opción: "))