'''
• Amasado $1.500
• Molde $1.000
• Baguette $2.000
• Integral $3.000
Determine el total a pagar por un cliente, el cual puede comprar diferentes tipos y cantidad de pan.
Si el total de la venta es superior a $5000 el envío es gratis, sino se cobra el 10% adicional
'''
menu = 1
amasado = 0
molde = 0
baguette = 0
integral = 0
total = 0
while menu != 2:
    print("Indique el tipo de pan que desea llevar:\n1.- AMASADO ($1.500)\n2.- MOLDE ($1.000)\n3.- BAGUETTE ($2.000)\n4.- INTEGRAL ($3.000)")
    opcion = input("Ingrese su opción: ")
    while type(opcion) == str:
        try:
            opcion = int(opcion)
            if opcion>4 or opcion<1:
                opcion = input("El valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            opcion = input("El valor ingresado no es válido. Ingrese nuevamente su opción: ")
    #amasado 1500
    if opcion == 1:
        cant = input("Ingrese la cantidad que desee comprar: ")
        while type(cant) == str:
            try:
                cant = int(cant)
                if cant<1:
                    cant = input("La cantidad debe ser mayor o igual a 1. Ingrese nuevamente la cantidad que desee comprar: ")
            except ValueError:
                cant = input("El valor ingresado no es válido. Ingrese nuevamente la cantidad que desee comprar: ")
        amasado += cant
        total += cant*1500
    #molde 1000
    elif opcion == 2:
        cant = input("Ingrese la cantidad que desee comprar: ")
        while type(cant) == str:
            try:
                cant = int(cant)
                if cant<1:
                    cant = input("La cantidad debe ser mayor o igual a 1. Ingrese nuevamente la cantidad que desee comprar: ")
            except ValueError:
                cant = input("El valor ingresado no es válido. Ingrese nuevamente la cantidad que desee comprar: ")
        molde += cant
        total += cant*1000
    #baguette 2000
    elif opcion == 3:
        cant = input("Ingrese la cantidad que desee comprar: ")
        while type(cant) == str:
            try:
                cant = int(cant)
                if cant<1:
                    cant = input("La cantidad debe ser mayor o igual a 1. Ingrese nuevamente la cantidad que desee comprar: ")
            except ValueError:
                cant = input("El valor ingresado no es válido. Ingrese nuevamente la cantidad que desee comprar: ")
        baguette += cant
        total += cant*2000
    #integral 3000
    else:
        cant = input("Ingrese la cantidad que desee comprar: ")
        while type(cant) == str:
            try:
                cant = int(cant)
                if cant<1:
                    cant = input("La cantidad debe ser mayor o igual a 1. Ingrese nuevamente la cantidad que desee comprar: ")
            except ValueError:
                cant = input("El valor ingresado no es válido. Ingrese nuevamente la cantidad que desee comprar: ")
        integral += cant
        total += cant*3000
    print("¿Desea agregar otro producto?\n1.- SÍ\n2.- NO")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>2 or menu<1:
                menu = input("El valor ingresado no es válido. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("El valor ingresado no es válido. Ingrese nuevamente su opción: ")
#valor total
envio = 0
if total<5000:
    envio = int((0.1)*total)
    total += envio
#detalle compra
print("El detalle de su compra es el siguiente:")
if amasado != 0:
    print(f"{amasado} UNIDAD(ES) DE PAN AMASADO. SUBTOTAL = ${amasado*1500}")
if molde != 0:
    print(f"{molde} UNIDAD(ES) DE PAN DE MOLDE. SUBTOTAL = ${molde*1000}")
if baguette != 0:
    print(f"{baguette} UNIDAD(ES) DE BAGUETTE. SUBTOTAL = ${baguette*2000}")
if integral != 0:
    print(f"{integral} UNIDAD(ES) DE PAN INTEGRAL. SUBTOTAL = ${integral*3000}")
print(f"VALOR DE ENVÍO = ${envio}\nVALOR TOTAL DE LA COMPRA = ${total}")