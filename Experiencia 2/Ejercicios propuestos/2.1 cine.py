'''
estreno 4800 normal 2900 30% dcto si es de institucion (solo aplicable en entrada)
palomita pequeña 2500 mediana 4500 grande 7800
bebida pequeña 1000 mediana 1250 grande 2000
'''
menu=1
while menu != 2:
    total=0
    print("1.- PELÍCULA DE ESTRENO \n2.- PELÍCULA NORMAL")   
    tipo = int(input("Ingrese su opción: "))
    while tipo>2 or tipo<1:
        tipo = int(input("Valor ingresado no es válido. Ingrese nuevamente su opción: "))
    if tipo==1:
        total=4800
    else:
        total=2900
    print("¿Es perteneciente a la institución?: \n1.- SÍ \n2.- NO")   
    perteneciente = int(input("Ingrese su opción: "))
    while perteneciente>2 or perteneciente<1:
        perteneciente = int(input("Valor ingresado no es válido. Ingrese nuevamente su opción: "))
    if perteneciente==1:
        total=round(total-0.3*total)
    print("Ingrese su tamaño de palomita: \n1.- PEQUEÑA \n2.- MEDIANA \n3.- GRANDE \n4.- NO QUIERE")   
    palomita = int(input("Ingrese su opción: "))
    while palomita>4 or palomita<1:
        palomita = int(input("Valor ingresado no es válido. Ingrese nuevamente su opción: "))
    if palomita !=4:
        cant = int(input("Ingrese la cantidad de palomitas que desea: "))
        while cant<=0:
            cant = int(input("Valor ingresado no es válido. Ingrese nuevamente la cantidad: "))
        if palomita==1:
            total=total+2500*cant
        elif palomita==2:
            total=total+4500*cant
        elif palomita==3:
            total=total+7800*cant
    print("Ingrese su tamaño de bebida: \n1.- PEQUEÑA \n2.- MEDIANA \n3.- GRANDE \n4.- NO QUIERE")   
    bebida = int(input("Ingrese su opción: "))
    while bebida>4 or bebida<1:
        bebida = int(input("Valor ingresado no es válido. Ingrese nuevamente su opción: "))
    if bebida !=4:
        cant = int(input("Ingrese la cantidad de palomitas que desea: "))
        while cant<=0:
            cant = int(input("Valor ingresado no es válido. Ingrese nuevamente la cantidad: "))
        if bebida==1:
            total=total+1000*cant
        elif bebida==2:
            total=total+1250*cant
        elif bebida==3:
            total=total+2000*cant
    print(f"A pagar: ${total}")
    pago = int(input("Deme los billetes: "))
    while pago<=0:
        pago = int(input("Monto ingresado no válido. Deme los billetes: "))
    if pago<total:
        print("Con esto no alcanza. ¡Perderá la cabeza!")
    else:
        print(f"Su vuelto es de ${pago-total}. Disfrute la película.")
    print("1.- VENDER OTRA ENTRADA \n2.- SALIR")
    menu = int(input("Ingrese su opción: "))
    while menu>2 or menu<1:
        menu = int(input("Valor ingresado no es válido. Ingrese nuevamente su opción: "))