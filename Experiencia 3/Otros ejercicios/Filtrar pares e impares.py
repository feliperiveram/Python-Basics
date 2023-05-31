menu = 1
lista = []
while menu != 5:
    print("1.- AGREGAR NÚMERO\n2.- FILTRAR NÚMEROS PARES\n3.- FILTRAR NÚMEROS IMPARES\n4.- BORRAR LISTA ACTUAL\n5.- SALIR DEL PROGRAMA")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>5 or menu<1:
                menu = input("Opción ingresada no es válida. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Opción ingresada no es válida. Ingrese nuevamente su opción: ")
    if menu == 1:
        num = input("Ingrese el número que desea agregar a la lista: ")
        while type(num) == str:
            try:
                num = int(num)
            except ValueError:
                num = input("Valor ingresado no es válida. Ingrese nuevamente su número: ")
        lista.append(num)
    #PARES
    elif menu == 2:
        pares = []
        for n in lista:
            if (n%2) == 0:
                pares.append(n)
        if len(pares) != 0:
            pares.sort()
            print(f"Los pares ingresados son {pares}.")
        else:
            print("No existen números pares en su lista.")
    #IMPARES
    elif menu == 3:
        impares = []
        for n in lista:
            if (n%2) != 0:
                impares.append(n)
        if len(impares) != 0:
            impares.sort()
            print(f"Los impares ingresados son {impares}.")
        else:
            print("No existen números impares en su lista.")
    elif menu == 4:
        lista = []
    else:
        print("Usted ha salido del programa. ¡Gracias por haberlo usado!")