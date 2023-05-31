menu = 1
lista = []
while menu != 4:
    print("1.- AGREGAR NÚMERO\n2.- BORRAR LISTA Y COMENZAR NUEVAMENTE\n3.- ELIMINAR DUPLICADOS\n4.- SALIR")
    menu = input("Ingrese su opción: ")
    while type(menu) == str:
        try:
            menu = int(menu)
            if menu>4 or menu<1:
                menu = input("Opción ingresada no es válida. Ingrese nuevamente su opción: ")
        except ValueError:
            menu = input("Opción ingresada no es válida. Ingrese nuevamente su opción: ")
    if menu == 1:
        num = input("Ingrese el número que desea agregar a la lista: ")
        while type(num) == str:
            try:
                num = float(num)
            except ValueError:
                num = input("Valor ingresado no es válida. Ingrese nuevamente su número: ")
        lista.append(num)
    elif menu == 2:
        lista = []
    elif menu == 3:
        lista_nueva = []
        for n in lista:
            if n not in lista_nueva:
                lista_nueva.append(n)
        print(f"La lista {lista} sin duplicados corresponde a {lista_nueva}.")
        lista = []
    else:
        print("Usted ha salido del programa. ¡Gracias por haberlo usado!")