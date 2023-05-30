'''4 tipos sandwiches y cupón de dcto'''
menu=1
suma=0
conteo=0
while menu != 2:
    print("1.- CHURRASCO ($1.500) \n2.- COMPLETO ($1.000) \n3.- VEGETARIANO ($2.000) \n4.- BARROS LUCO ($3.000)")
    opcion = int(input("Ingrese su opción: "))
    while opcion>4 or opcion<1:
        opcion = int(input("Opción no válida, vuelva a ingresar su opción: "))
    if opcion == 1:
        cantidad = int(input("Elija la cantidad: "))
        suma=suma+1500*cantidad
    if opcion == 2:
        cantidad = int(input("Elija la cantidad: "))
        suma=suma+1000*cantidad
    if opcion == 3:
        cantidad = int(input("Elija la cantidad: "))
        suma=suma+2000*cantidad
    if opcion == 4:
        cantidad = int(input("Elija la cantidad: "))
        suma=suma+3000*cantidad
    print("1.- AGREGAR MÁS \n2.- TERMINAR COMPRA")
    conteo=conteo+cantidad
    menu = int(input("Ingrese su opción: "))
    while menu>2 or menu<1:
        menu = int(input("Opción no válida, vuelva a ingresar su opción: "))
print("¿TIENE CUPÓN DE DESCUENTO? \n1.- SÍ \n2.- NO")
cupon = int(input("Ingrese su opción: "))
while cupon>2 or cupon<1:
    opcion = int(input("Opción no válida, vuelva a ingresar su opción: "))
if cupon == 1:
    print(f"Por un total de {conteo} elementos, debe pagar ${suma-0.1*suma}.")
else:
    print(f"Por un total de {conteo} elementos, debe pagar ${suma}.")