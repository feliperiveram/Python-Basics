menu=1
while menu != 2:
    cant = int(input("Introduzca el número de mascarillas que desea: "))
    while cant <= 0:
        cant = int(input("El valor ingresado no es válido. Introduzca nuevamente el número de mascarillas que desea: "))
    print("Seleccione su comuna: ")
    print("1.- MISMA COMUNA \n2.- COMUNA ALEDAÑA \n3.- OTRA")
    comuna = int(input("Elija su comuna: "))
    while comuna>3 or comuna<1:
        comuna = int(input("Opción escogida no es válida. Elija nuevamente su comuna: "))
    if comuna == 1:
        total=500*cant+1000
        print(f"Su total es de {total}.")
    elif comuna == 2:
        total=500*cant+2000
        print(f"Su total es de {total}.")
    else:
        total=500*cant+3000
        print(f"Su total es de {total}.")
    print("1.- REALIZAR OTRA COTIZACIÓN \n2.- SALIR")
    menu = int(input("Elija su opción: "))
    while menu>2 or menu<1:
        menu = int(input("La opción ingresada no es válida. Elija nuevamente su opción: "))